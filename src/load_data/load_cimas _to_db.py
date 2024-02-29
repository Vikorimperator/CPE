# Cargamos los modulos a emplear
import psycopg2
from psycopg2 import sql
from io import StringIO
import os
import sys
from dotenv import load_dotenv

# Cargamos variables de entorno
load_dotenv()

# Obtenemos los valores de las variables de entorno
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Creamos un cursor y abrimos un archivo temporal para copiar los datos
cur = conn.cursor()

# Nombre del campo a insertar
nombre_campo = "Caparroso-Pijije-Escuintle"

# Query para verificar si el campo ya existe en la tabla campos
query_check = sql.SQL(
    "SELECT campo_id FROM campos WHERE nombre_campo = %s")
cur.execute(query_check, [nombre_campo])
existing_campo = cur.fetchone()

if existing_campo:
    print(f"El campo '{nombre_campo}' ya existe en la base de datos.")
else:
    # Query para insertar el campo en la tabla campos
    query_insert = sql.SQL(
        "INSERT INTO public.campos (nombre_campo, fecha_creacion, actualizado) VALUES (%s, now(), now())")
    cur.execute(query_insert, [nombre_campo])
    print(f"Se ha insertado el campo '{nombre_campo}' en la base de datos.")

# Confirmar la inserción o la verificación
conn.commit()

# Cerramos la conexión y el cursor
cur.close()
conn.close()
