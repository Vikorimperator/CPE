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

# Query para insertar el campo en la tabla campos
query = sql.SQL(
    "INSERT INTO campos (nombre_campo, fecha_creacion, actualizado) VALUES (%s, now(), now())")

# Ejecutar la consulta con el nombre del campo
cur.execute(query, [nombre_campo])

# Confirmar la inserción
conn.commit()

# Cerramos la conexión y el cursor
cur.close()
conn.close()
