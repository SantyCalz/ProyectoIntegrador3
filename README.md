# Sistema de Reservas - Grupo CodeX5

Este proyecto es un sistema de reservas de canchas deportivas con interfaz gráfica en Python y base de datos PostgreSQL.

## Requisitos
- Python 3.10 o superior
- PostgreSQL instalado y corriendo
- Acceso a un usuario de PostgreSQL con permisos para crear tablas

## Instalación de dependencias

1. Crea y activa un entorno virtual (opcional pero recomendado):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```

# También puedes instalar todo con este comando:
```powershell
pip install customtkinter psycopg2 tkcalendar
```

## Configuración de la base de datos

### 1. Crear la base de datos (solo la primera vez)
Debes crear la base de datos en PostgreSQL antes de ejecutar el sistema. Puedes hacerlo desde pgAdmin, DBeaver o con el siguiente comando en consola:

```sql
CREATE DATABASE nombre_base;
```

O desde PowerShell:
```powershell
psql -U usuario -h localhost -c "CREATE DATABASE nombre_base;"
```

### 2. Configurar los datos de conexión
Puedes configurar los datos de conexión a PostgreSQL usando variables de entorno. Ejemplo (en PowerShell):

```powershell
$env:PG_DB = "nombre_base"
$env:PG_USER = "usuario"
$env:PG_PASSWORD = "contraseña"
$env:PG_HOST = "localhost"
$env:PG_PORT = "5432"
```

O edita directamente los valores por defecto en `init_db.py` y `conexion.py`.

### 3. Crear las tablas automáticamente
Ejecuta el script para crear las tablas y restricciones necesarias:

```powershell
python init_db.py
```

Verás el mensaje `Base de datos y tablas creadas correctamente.` si todo salió bien.

## Ejecución del sistema

1. Asegúrate de que el servidor de PostgreSQL esté corriendo y que la base de datos y tablas existan.
2. Ejecuta la interfaz gráfica:
   ```powershell
   python interfaz.py
   ```

## Estructura del proyecto
```
ProyectoIntegrador/
├── interfaz.py         # Interfaz gráfica (CustomTkinter)
├── usuarios.py         # Lógica de usuarios (registro, login)
├── reservas.py         # Lógica de reservas (crear, ver, eliminar)
├── conexion.py         # Conexión a PostgreSQL
├── init_db.py          # Script para crear tablas automáticamente
├── requirements.txt    # Dependencias
├── data/               # Carpeta para archivos temporales (no se usa con PostgreSQL)
```

## Créditos y roles
- Santiago: Base de datos y conexión
- Santino: Módulo de usuarios
- Leo: Módulo de reservas
- Ana: Interfaz gráfica y documentación

## Notas
- Si tienes problemas de conexión, revisa los datos de usuario, contraseña y nombre de base de datos.
- Si cambias la estructura de las tablas, actualiza el script `init_db.py`.
- No subas tus contraseñas ni datos sensibles al repositorio.

---

