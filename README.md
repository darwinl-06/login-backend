# 🚀 Plataforma de Autenticación Completa

Una aplicación web moderna de autenticación construida con **FastAPI** (backend) y **Next.js** (frontend), implementando un sistema completo de gestión de usuarios con autenticación JWT, panel de administración y diseño responsivo.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Uso de la Aplicación](#-uso-de-la-aplicación)
- [Documentación de APIs](#-documentación-de-apis)
- [Estructura del Proyecto](#-estructura-del-proyecto)

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


Este proyecto está abierto a contribuciones. Para contribuir:

1. **Fork** el repositorio
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**Desarrollado con ❤️ usando FastAPI y Next.js**