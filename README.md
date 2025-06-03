# 🚀 Plataforma de Autenticación Completa

Una aplicación web moderna de autenticación construida con **FastAPI** (backend) y **Next.js** (frontend), implementando un sistema completo de gestión de usuarios con autenticación JWT, panel de administración y diseño responsivo.

## Uso de Inteligencia Artificial

Sí se utilizó Inteligencia Artificial (IA) durante el desarrollo del proyecto, específicamente para comprender el funcionamiento del algoritmo PBKDF2 y su implementación en Python. Los siguientes fueron los prompts utilizados:

* **Prompt 1**: *¿Qué es PBKDF2? - ANÁLISIS*
* **Prompt 2**: *¿Cómo podemos implementar el algoritmo PBKDF2 para el hashing de contraseñas en Python? - ANÁLISIS*
* **Prompt 3**: *¿Qué es salt, cómo se utiliza? - ANÁLISIS*

La información obtenida nos permitió aplicar buenas prácticas de seguridad en el almacenamiento de contraseñas, utilizando salt y múltiples iteraciones para mitigar ataques de fuerza bruta.

## ✨ Características

### 🔐 Sistema de Autenticación
- **Registro de usuarios** con validación de datos
- **Inicio de sesión** con JWT tokens
- **Cambio de contraseñas** seguro
- **Autenticación persistente** con cookies
- **Logout** con limpieza de sesión

### 👥 Gestión de Usuarios
- **Perfil de usuario** editable
- **Última conexión** con formato localizado
- **Protección de rutas** basada en roles
- **Sistema de permisos** (admin/usuario)

### 🛠️ Panel de Administración
- **Listado completo** de usuarios registrados
- **Eliminación de usuarios** (excepto admins)
- **Reset de contraseñas** con contraseña temporal
- **Estadísticas** del sistema en tiempo real
- **Gestión de roles** y permisos

### 🎨 Interfaz de Usuario
- **Diseño responsive** para móviles y desktop
- **Componentes modernos** con shadcn/UI
- **Tema consistente** con Tailwind CSS
- **Navegación intuitiva** con menú hamburguesa
- **Feedback visual** para todas las acciones

## 🏗️ Arquitectura del Sistema

```
┌─────────────────┐    HTTP/JSON     ┌─────────────────┐
│                 │ ◄──────────────► │                 │
│   Frontend      │     Requests     │    Backend      │
│   (Next.js)     │                  │   (FastAPI)     │
│                 │                  │                 │
└─────────────────┘                  └─────────────────┘
         │                                     │
         ▼                                     ▼
┌─────────────────┐                  ┌─────────────────┐
│  Browser State  │                  │   SQLite DB     │
│  (Auth Context) │                  │  (User Data)    │
└─────────────────┘                  └─────────────────┘
```

### Flujo de Autenticación
1. **Usuario** → Envía credenciales al backend
2. **Backend** → Valida y genera JWT token
3. **Frontend** → Almacena token en cookies seguras
4. **Interceptores** → Añaden token automáticamente a requests
5. **Refresh automático** → Manejo de tokens expirados

## 🛠️ Tecnologías Utilizadas

### Backend (FastAPI)
- **FastAPI 0.104.1** - Framework web moderno y rápido
- **SQLAlchemy 2.0.23** - ORM para base de datos
- **SQLite** - Base de datos embebida
- **Python-JOSE** - Manejo de JWT tokens
- **Passlib** - Hash seguro de contraseñas (PBKDF2)
- **Uvicorn** - Servidor ASGI
- **Pydantic** - Validación de datos
- **CORS Middleware** - Configuración de dominios cruzados

### Frontend (Next.js)
- **Next.js 15** - Framework React con SSR
- **TypeScript** - Tipado estático
- **Tailwind CSS** - Framework de estilos utilitarios
- **shadcn/UI** - Componentes de UI modernos
- **React Hook Form** - Manejo de formularios
- **Zod** - Validación de esquemas
- **Axios** - Cliente HTTP con interceptores
- **js-cookie** - Manejo de cookies
- **Lucide React** - Iconografía moderna

## 🚀 Instalación y Configuración

### Prerrequisitos
- **Python 3.8+**
- **Node.js 18+**
- **npm o yarn**

### 1. Configuración del Backend

```bash
# Navegar al directorio raíz
cd login-backend-main

# Instalar dependencias de Python
pip install -r requirements.txt

# Iniciar el servidor backend
uvicorn app.main:app --reload
```

El backend estará disponible en `http://localhost:8000`

### 2. Configuración del Frontend

```bash
# Navegar al directorio frontend
cd frontend

# Instalar dependencias de Node.js
npm install

# Configurar variables de entorno
# Crear archivo .env.local con:
NEXT_PUBLIC_API_URL=http://localhost:8000

# Iniciar el servidor de desarrollo
npm run dev
```

El frontend estará disponible en `http://localhost:3000`

### 3. Configuración de Producción

```bash
# Backend
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Frontend
npm run build
npm start
```

## 📱 Uso de la Aplicación

### Primera Configuración
1. **Acceder** a `http://localhost:3000`
2. **Registrar** el primer usuario (será automáticamente admin)
3. **Iniciar sesión** con las credenciales creadas
4. **Explorar** el dashboard y panel de administración

### Funcionalidades por Rol

#### 👤 Usuario Regular
- ✅ Ver su perfil y última conexión
- ✅ Cambiar su contraseña
- ✅ Navegación por el dashboard
- ❌ Acceso al panel de administración

#### 👑 Administrador
- ✅ Todas las funciones de usuario regular
- ✅ Ver lista completa de usuarios
- ✅ Eliminar usuarios (excepto otros admins)
- ✅ Resetear contraseñas de usuarios
- ✅ Ver estadísticas del sistema

## 📚 Documentación de APIs

### Documentación Interactiva
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints Principales

#### 🔑 Autenticación
```http
POST /auth/login
Content-Type: application/json

{
  "username": "mi_usuario",
  "password": "mi_contraseña"
}
```

#### 👤 Gestión de Usuarios
```http
# Crear usuario
POST /api/users

# Información del usuario actual
GET /api/users/me

# Última conexión
GET /api/users/me/last-login

# Cambiar contraseña
PUT /api/users/me/password
```

#### 🛠️ Administración
```http
# Listar usuarios
GET /api/admin/users

# Eliminar usuario
DELETE /api/admin/users/{username}

# Reset contraseña
POST /api/admin/users/{username}/reset-password
```

## 📁 Estructura del Proyecto

```
login-backend-main/
├── 📄 README.md                    # Este archivo
├── 📄 requirements.txt             # Dependencias Python
├── 📄 login_platform.db           # Base de datos SQLite
├── 📁 app/                         # Código del backend
│   ├── 📄 main.py                 # Aplicación principal FastAPI
│   ├── 📄 models.py               # Modelos de base de datos
│   ├── 📄 schemas.py              # Esquemas Pydantic
│   ├── 📄 security.py             # Funciones de seguridad
│   └── 📄 database.py             # Configuración BD
└── 📁 frontend/                    # Aplicación Next.js
    ├── 📄 package.json            # Dependencias Node.js
    ├── 📄 tailwind.config.ts      # Configuración Tailwind
    ├── 📄 components.json         # Configuración shadcn/UI
    ├── 📁 src/
    │   ├── 📁 app/                # Rutas de la aplicación
    │   │   ├── 📄 layout.tsx      # Layout principal
    │   │   ├── 📄 page.tsx        # Página principal
    │   │   ├── 📁 login/          # Página de login
    │   │   ├── 📁 register/       # Página de registro
    │   │   ├── 📁 dashboard/      # Dashboard principal
    │   │   ├── 📁 profile/        # Perfil de usuario
    │   │   └── 📁 admin/          # Panel de administración
    │   ├── 📁 components/         # Componentes reutilizables
    │   │   ├── 📄 Navbar.tsx      # Barra de navegación
    │   │   ├── 📄 ProtectedRoute.tsx # Rutas protegidas
    │   │   └── 📁 ui/             # Componentes shadcn/UI
    │   ├── 📁 contexts/           # Context providers
    │   │   └── 📄 AuthContext.tsx # Contexto de autenticación
    │   ├── 📁 lib/                # Utilidades y servicios
    │   │   ├── 📄 api.ts          # Cliente HTTP configurado
    │   │   ├── 📄 services.ts     # Servicios de API
    │   │   └── 📄 utils.ts        # Utilidades generales
    │   └── 📁 types/              # Definiciones TypeScript
    │       └── 📄 index.ts        # Tipos principales
    └── 📁 public/                 # Archivos estáticos
```


## Implementación de Seguridad

### Hashing de Contraseñas con PBKDF2

La seguridad de las contraseñas es fundamental en cualquier sistema de autenticación. Implementamos **PBKDF2 (Password-Based Key Derivation Function 2)** que es un estándar recomendado por NIST para el almacenamiento seguro de contraseñas.

```python
from passlib.hash import pbkdf2_sha256

def hash_password(password: str, salt: str) -> str:
    return pbkdf2_sha256.hash(password + salt)

def verify_password(plain_password: str, salt: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(plain_password + salt, hashed_password)
```

**Ventajas del PBKDF2:**
- **Resistencia a ataques de fuerza bruta**: Utiliza un número configurable de iteraciones que hace computacionalmente costoso probar múltiples contraseñas
- **Protección contra rainbow tables**: Al usar salt único para cada contraseña, previene ataques con tablas precalculadas
- **Estándar probado**: Es un algoritmo aprobado por organismos de seguridad internacionales

###  Sistema de Salt Criptográfico

Cada contraseña utiliza un **salt único** generado criptográficamente:

```python
def create_salt() -> str:
    return secrets.token_hex(16)
```

El salt se genera usando el módulo `secrets` de Python, que proporciona números aleatorios criptográficamente seguros. Esto garantiza que:
- **Cada contraseña tiene un salt único**: Incluso si dos usuarios tienen la misma contraseña, sus hashes serán completamente diferentes
- **Prevención de ataques rainbow table**: Las tablas precalculadas de hashes no sirven contra contraseñas con salt
- **Aleatoriedad criptográfica**: El salt es impredecible y no puede ser reproducido

### Autenticación basada en JWT (JSON Web Tokens)

Para la gestión de sesiones, implementamos **JWT** que ofrece una autenticación stateless y segura:

```python
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

**Características de seguridad del JWT implementado:**
- **Expiración automática**: Los tokens tienen un tiempo de vida limitado (24 horas)
- **Clave secreta segura**: Generada aleatoriamente en cada ejecución del programa
- **Algoritmo HS256**: Utiliza HMAC con SHA-256 para la firma digital
- **Verificación de integridad**: Cualquier modificación del token lo invalida automáticamente

###  Control de Acceso y Autorización

El sistema implementa un control de acceso robusto con diferentes niveles de permisos:

```python
async def get_current_admin(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos suficientes",
        )
    return current_user
```

**Niveles de seguridad implementados:**
- **Autenticación**: Verificación de identidad mediante token JWT
- **Autorización**: Verificación de permisos según el tipo de usuario
- **Administrador único**: Solo el primer usuario registrado obtiene permisos de administrador
- **Protección de rutas**: Las operaciones administrativas requieren permisos especiales

### Seguridad en el Manejo de Tiempo

Para el registro de última conexión, implementamos manejo seguro de zonas horarias:

```python
# Guardar hora en UTC con tzinfo  
current_time = datetime.now(timezone.utc).replace(microsecond=0)
user.last_login = current_time
```

Esto previene problemas de seguridad relacionados con:
- **Manipulación de tiempo**: Almacenamiento en UTC previene confusiones de zona horaria
- **Consistencia**: Todos los registros de tiempo siguen el mismo estándar
- **Auditoría**: Facilita el seguimiento preciso de actividades de usuario

## Dificultades Encontradas

###  Manejo de Zonas Horarias
Una de las principales dificultades fue el manejo correcto de las zonas horarias para el registro de última conexión. Inicialmente, los timestamps se almacenaban como "naive datetime" sin información de zona horaria, lo que causaba inconsistencias.

**Solución implementada:**
- Almacenamiento en UTC en la base de datos
- Conversión a zona horaria local (Colombia) solo para visualización
- Verificación de `tzinfo` antes de realizar conversiones

###  Gestión de la Clave Secreta JWT
El manejo de la clave secreta para JWT presentó desafíos de seguridad. Usar una clave fija sería inseguro, pero generar una nueva en cada reinicio invalida todos los tokens existentes.

**Solución adoptada:**
- Generación de clave aleatoria en cada ejecución
- Los usuarios deben volver a autenticarse después de reiniciar el servidor
- Esto mejora la seguridad a costa de una menor persistencia de sesión

## Conclusiones

### Aspectos Positivos Logrados

 **Seguridad Robusta**: La implementación de PBKDF2 con salt único garantiza que las contraseñas estén protegidas contra los ataques más comunes (fuerza bruta, rainbow tables, etc.)

 **Arquitectura Modular**: La separación en módulos especializados (security, models, schemas) facilita el mantenimiento y permite futuras expansiones del sistema

 **Autenticación Moderna**: El uso de JWT proporciona una autenticación stateless que escala bien y es compatible con aplicaciones web modernas

 **Control de Acceso Granular**: La diferenciación entre usuarios comunes y administradores permite un control fino de permisos

### Lecciones Aprendidas

 **Importancia del Salt**: Sin salt, incluso PBKDF2 sería vulnerable a ataques de rainbow table. La combinación de ambos es esencial

 **Manejo de Tiempo**: Los sistemas de autenticación requieren un manejo cuidadoso del tiempo, especialmente cuando se involucran múltiples zonas horarias

 **Balance Seguridad-Usabilidad**: Decisiones como la duración de los tokens JWT requieren balancear seguridad (tiempo corto) con experiencia de usuario (tiempo largo)

### Recomendaciones para Mejoras Futuras

 **Refresh Tokens**: Implementar tokens de renovación para mejorar la experiencia de usuario sin comprometer la seguridad

 **Rate Limiting**: Agregar limitación de intentos de login para prevenir ataques de fuerza bruta

 **Logging de Seguridad**: Implementar un sistema de logs para auditoría de eventos de seguridad

 **Validación de Políticas de Contraseña**: Agregar requisitos mínimos para la complejidad de contraseñas

El proyecto demuestra que es posible implementar un sistema de autenticación seguro siguiendo las mejores prácticas de la industria, utilizando herramientas modernas y estándares probados de seguridad.

