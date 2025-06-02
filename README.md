# Login Platform Backend

Este es un backend para una plataforma de login que implementa las siguientes funcionalidades:
- Gestión de usuarios (administrador y usuarios comunes)
- Almacenamiento seguro de contraseñas usando PBKDF2
- Sistema de autenticación con JWT
- Registro de última fecha/hora de login

## Requisitos
- Python 3.8+
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar el servidor:
```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

## Documentación de la API

La documentación interactiva de la API estará disponible en:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints Principales

### Usuarios Comunes
- `POST /token` - Login de usuario
- `POST /users/` - Crear nuevo usuario
- `GET /users/me/last-login` - Consultar última fecha de login
- `POST /users/me/change-password` - Cambiar contraseña

### Administrador
- `GET /admin/users` - Listar todos los usuarios
- `DELETE /admin/users/{username}` - Eliminar usuario
- `POST /admin/users/{username}/reset-password` - Resetear contraseña de usuario

## Notas Importantes
- El primer usuario creado será automáticamente el administrador
- Solo puede existir un administrador en el sistema
- Las contraseñas se almacenan de forma segura usando PBKDF2 con salt
- Se utiliza autenticación JWT para proteger los endpoints 