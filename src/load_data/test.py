# Cargamos los modulos a emplear
from dotenv import load_dotenv
from io import StringIO
from psycopg2 import sql
import psycopg2
import pandas as pd
import sys
import os
import time

# Cargamos variables de entorno
load_dotenv()

# Obtenemos los valores de las variables de entorno
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Conexion a la base de datos
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Creamos un cursor
cur = conn.cursor()

# Obtenemos el pozo_id del pozo de la tabla pozos
pozo = "Caparroso-71"
query = "SELECT pozo_id FROM pozos WHERE nombre_pozo = %s"
cur.execute(query, (pozo,))
result = cur.fetchone()

if result is not None:
    pozo_id = result[0]
    # Intentamos insertar el nuevo registro
    try:
        cur.execute("INSERT INTO cimas (nombre_cima, pozo_id, cima_md, fecha_creacion, actualizado) VALUES ('ejemplocima1', %s, 1000.0, now(), now())", (pozo_id,))
        print("Inserción exitosa.")
    except Exception as e:
        print(f"Error al insertar el registro: {e}")
else:
    print(f"No se encontró el pozo '{pozo}'.")

# Cerrar conexión
cur.close()
conn.close()