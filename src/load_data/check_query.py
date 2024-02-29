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

# Crear un cursor para ejecutar consultas
cur = conn.cursor()

# Consulta para contar el número de registros en la tabla campos
query = "SELECT COUNT(*) FROM campos;"

# Ejecutar la consulta
cur.execute(query)

# Obtener el resultado de la consulta
num_registros = cur.fetchone()[0]

print(f"El número de registros en la tabla campos es: {num_registros}")

# Cerrar cursor y conexión
cur.close()
conn.close()
