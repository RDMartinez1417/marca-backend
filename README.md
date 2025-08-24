# Proyecto CRUD de Marcas - Backend

Este es el backend del proyecto de prueba técnica para desarrollador FullStack.  
Está desarrollado con **FastAPI**, **SQLAlchemy** y soporta tanto **SQLite (local rápido)** como **PostgreSQL (producción)**.

---

## 🚀 Requisitos previos
- Python 3.11 (o superior)
- PostgreSQL 15+ (opcional si quieres usar DB en producción)
- Git

---

## ⚙️ Configuración inicial

### 1. Clonar el repositorio
``` bash
git clone https://github.com/RDMartinez1417/marca-backend.git
cd marca-backend
```

### 2. Crear ambiete virtual
``` bash
# En Windows (PowerShell)
py -m venv venv
.\venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
``` bash
pip install -r requirements.txt
```
Si no existe requirements.txt, genera uno:
``` bash
pip freeze > requirements.txt

```
### 4. Variables de entorno
Crea un archivo .env en la raíz del proyecto con la siguiente variable:
## Opción A: Usando SQLite (modo rápido)
``` python
DATABASE_URL=sqlite:///./database.db

```

## Opción B: Usando PostgreSQL (producción)
``` python
DATABASE_URL=postgresql://usuario:password@localhost:5432/marcas_db
```

### 5. Ejecutar la aplicación
``` python
uvicorn app.main:app --reload
```
- La API estará disponible en:
👉 http://localhost:8000
- Documentación interactiva:
👉 http://localhost:8000/docs

## 📌 Endpoints principales

### Listar marcas con filtros y paginación
- **GET** `/marcas/list`
  - Parámetros opcionales:
    - `skip` (int, default=0) → Paginación (omitir registros)
    - `limit` (int, default=100) → Límite de registros
    - `nombre` (str) → Filtrar por nombre
    - `estado` (str) → Filtrar por estado
    - `pais_origen` (str) → Filtrar por país
    - `clase_niza` (int) → Filtrar por clase Niza
    - `categoria` (str) → Filtrar por categoría

### Obtener una marca por ID
- **GET** `/marcas/list/{marca_id}`

### Crear una nueva marca
- **POST** `/marcas/create`
  - Body → `MarcaCreate`

### Actualizar una marca por ID
- **PUT** `/marcas/update/{marca_id}`
  - Body → `MarcaUpdate`

### Eliminar una marca por ID
- **DELETE** `/marcas/delete/{marca_id}`

### Resumen de marcas (conteo)
- **GET** `/marcas/summary`
  - Devuelve un diccionario con el conteo de marcas por estado/categoría.

### Listar categorías únicas
- **GET** `/marcas/categories`
  - Devuelve una lista de todas las categorías registradas.

### Listado de paises
- **GET** `https://restcountries.com/v3.1/all?fields=name`
  - Devuelve una lista de paises (**Api publica**).

## 📦 Librerías utilizadas

- **FastAPI** (`fastapi==0.116.1`) → Framework web para construir la API.  
- **SQLAlchemy** (`SQLAlchemy==2.0.43`) → ORM para manejo de la base de datos.  
- **psycopg2-binary** (`psycopg2-binary==2.9.10`) → Driver de PostgreSQL.  
- **Uvicorn** (`uvicorn==0.35.0`) → Servidor ASGI para correr la aplicación FastAPI.  
- **Pydantic** (`pydantic==2.11.7`) → Validación de datos y modelos.  
- **pydantic-core** (`pydantic_core==2.33.2`) → Núcleo de validación de Pydantic.  
- **python-dotenv** (`python-dotenv==1.1.1`) → Cargar variables de entorno desde `.env`.  
- **Starlette** (`starlette==0.47.2`) → Toolkit ASGI en el que se basa FastAPI.  
- **anyio** (`anyio==4.10.0`) → Soporte de concurrencia asíncrona.  
- **h11** (`h11==0.16.0`) → Implementación de HTTP para Uvicorn.  
- **idna** (`idna==3.10`) → Manejo de nombres de dominio internacionalizados.  
- **greenlet** (`greenlet==3.2.4`) → Soporte de corrutinas usado por SQLAlchemy.  
- **click** (`click==8.2.1`) → Utilidades de línea de comandos.  
- **colorama** (`colorama==0.4.6`) → Colores en consola (principalmente Windows).  
- **sniffio** (`sniffio==1.3.1`) → Detección del loop asíncrono en uso.  
- **typing-extensions** (`typing_extensions==4.14.1`) → Extensiones de tipado para versiones anteriores de Python.  
- **typing-inspection** (`typing-inspection==0.4.1`) → Herramienta para inspección de tipos.  
- **annotated-types** (`annotated-types==0.7.0`) → Extensiones de tipado para Pydantic y validaciones.  
