import psycopg2
import os

# Configuración de conexión (puedes modificar o usar variables de entorno)
DB_NAME = os.getenv("PG_DB", "nombre_base")
DB_USER = os.getenv("PG_USER", "usuario")
DB_PASS = os.getenv("PG_PASSWORD", "contraseña")
DB_HOST = os.getenv("PG_HOST", "localhost")
DB_PORT = os.getenv("PG_PORT", "5432")

# SQL para crear tablas y restricciones exactamente como en tu pgAdmin
SQL = '''
CREATE TABLE IF NOT EXISTS public.usuarios
(
    id integer NOT NULL DEFAULT nextval('usuarios_id_seq'::regclass),
    nombre text NOT NULL,
    apellido text NOT NULL,
    correo text NOT NULL,
    fecha_nacimiento date NOT NULL,
    telefono text NOT NULL,
    "contraseña" text NOT NULL,
    rol text NOT NULL DEFAULT 'user',
    CONSTRAINT usuarios_pkey PRIMARY KEY (id),
    CONSTRAINT usuarios_correo_key UNIQUE (correo)
);

CREATE TABLE IF NOT EXISTS public.reservas
(
    id integer NOT NULL DEFAULT nextval('reservas_id_seq'::regclass),
    usuario_id integer NOT NULL,
    fecha date NOT NULL,
    hora time without time zone NOT NULL,
    cancha text NOT NULL,
    CONSTRAINT reservas_pkey PRIMARY KEY (id),
    CONSTRAINT reservas_fecha_hora_cancha_key UNIQUE (fecha, hora, cancha),
    CONSTRAINT reservas_usuario_id_fkey FOREIGN KEY (usuario_id)
        REFERENCES public.usuarios (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
'''

def main():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute(SQL)
        conn.commit()
        cur.close()
        conn.close()
        print("Base de datos y tablas creadas correctamente.")
    except Exception as e:
        print(f"Error al crear la base de datos/tablas: {e}")

if __name__ == "__main__":
    main()
