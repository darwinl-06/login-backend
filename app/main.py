from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List
from app import models
from app import schemas
from app import security
from app.database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware
import pytz
from pydantic import BaseModel
from typing import Optional

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Login Platform API",
    description="API para gestión de usuarios y autenticación",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dependency to get current user
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = security.verify_token(token)
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
        )
    return user

# Dependency to verify admin status
async def get_current_admin(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos suficientes",
        )
    return current_user

class LastLoginResponse(BaseModel):
    fecha: str
    hora: str
    zona_horaria: str

@app.post("/auth/login", response_model=schemas.Token, tags=["Autenticación"])
async def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Iniciar sesión y obtener token de acceso (usando JSON)
    
    Ejemplo de body:
    ```json
    {
        "username": "tu_usuario",
        "password": "tu_contraseña"
    }
    ```
    """
    return await authenticate_user(user_data.username, user_data.password, db)

async def authenticate_user(username: str, password: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not security.verify_password(password, user.salt, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
        )
    
    # Guardar hora en UTC con tzinfo  
    current_time = datetime.now(timezone.utc).replace(microsecond=0)
    user.last_login = current_time
    db.commit()
    
    access_token = security.create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "expires_in": f"{security.ACCESS_TOKEN_EXPIRE_MINUTES // 60} horas"
    }

# Rutas de usuarios
@app.post("/api/users", response_model=schemas.UserResponse, tags=["Usuarios"])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Crear un nuevo usuario
    """
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está registrado")
    
    # Check if this is the first user (will be admin)
    is_first_user = db.query(models.User).first() is None
    
    salt = security.create_salt()
    hashed_password = security.hash_password(user.password, salt)
    
    db_user = models.User(
        username=user.username,
        hashed_password=hashed_password,
        salt=salt,
        is_admin=is_first_user
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/api/users/me", response_model=schemas.UserResponse, tags=["Usuarios"])
async def get_current_user_info(current_user: models.User = Depends(get_current_user)):
    """
    Obtener información del usuario actual
    """
    return current_user

import pytz

@app.get("/api/users/me/last-login", response_model=LastLoginResponse, tags=["Usuarios"])
async def get_last_login(current_user: models.User = Depends(get_current_user)):
    if current_user.last_login:
        # Verifica si last_login tiene tzinfo
        dt = current_user.last_login
        if dt.tzinfo is None:
            # Si es naive, asumimos que está en UTC y hacemos tzaware
            dt = dt.replace(tzinfo=timezone.utc)
        
        tz = pytz.timezone('America/Bogota')
        local_dt = dt.astimezone(tz)
        
        fecha = local_dt.strftime("%d de %B de %Y")
        hora = local_dt.strftime("%I:%M %p").replace("AM", "a. m.").replace("PM", "p. m.")
        
        meses = {
            'January': 'enero', 'February': 'febrero', 'March': 'marzo',
            'April': 'abril', 'May': 'mayo', 'June': 'junio',
            'July': 'julio', 'August': 'agosto', 'September': 'septiembre',
            'October': 'octubre', 'November': 'noviembre', 'December': 'diciembre'
        }
        for mes_en, mes_es in meses.items():
            fecha = fecha.replace(mes_en, mes_es)
        
        return {
            "fecha": fecha,
            "hora": hora,
            "zona_horaria": "Colombia (UTC-5)"
        }
    return {
        "fecha": "Nunca",
        "hora": "Nunca",
        "zona_horaria": "Colombia (UTC-5)"
    }


@app.put("/api/users/me/password", tags=["Usuarios"])
async def change_password(
    password_change: schemas.ChangePassword,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Cambiar la contraseña del usuario actual
    """
    if not security.verify_password(
        password_change.current_password,
        current_user.salt,
        current_user.hashed_password
    ):
        raise HTTPException(status_code=400, detail="Contraseña actual incorrecta")
    
    new_salt = security.create_salt()
    new_hashed_password = security.hash_password(password_change.new_password, new_salt)
    
    current_user.salt = new_salt
    current_user.hashed_password = new_hashed_password
    db.commit()
    return {"message": "Contraseña actualizada correctamente"}

# Rutas de administración
@app.get("/api/admin/users", response_model=List[schemas.UserResponse], tags=["Administración"])
async def list_users(
    current_admin: models.User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Listar todos los usuarios (solo administradores)
    """
    users = db.query(models.User).all()
    return users

@app.delete("/api/admin/users/{username}", tags=["Administración"])
async def delete_user(
    username: str,
    current_admin: models.User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Eliminar un usuario (solo administradores)
    """
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if user.is_admin:
        raise HTTPException(status_code=400, detail="No se puede eliminar al usuario administrador")
    
    db.delete(user)
    db.commit()
    return {"message": f"Usuario {username} eliminado correctamente"}

@app.post("/api/admin/users/{username}/reset-password", tags=["Administración"])
async def reset_password(
    username: str,
    current_admin: models.User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Resetear la contraseña de un usuario (solo administradores)
    
    Esta función resetea la contraseña del usuario especificado a una contraseña temporal: 'Temporal123!'
    El usuario deberá cambiar esta contraseña en su próximo inicio de sesión.
    """
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Set temporary password
    temp_password = "Temporal123!"
    new_salt = security.create_salt()
    new_hashed_password = security.hash_password(temp_password, new_salt)
    
    user.salt = new_salt
    user.hashed_password = new_hashed_password
    db.commit()
    return {
        "message": f"Contraseña reseteada para el usuario {username}",
        "temp_password": temp_password,
        "warning": "Por favor, cambie esta contraseña temporal inmediatamente después de iniciar sesión"
    } 