# Cargamos los modulos a emplear
import psycopg2
from dotenv import load_dotenv
import os
import sys

# Cargamos variables de entorno
load_dotenv()

# Obtenemos los valores de las variables de entorno
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

try:
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

    # Ejecutar una consulta simple para verificar la conexión
    cur.execute('SELECT 1')

    # Obtener el resultado de la consulta
    result = cur.fetchone()

    print('Conexión exitosa. Resultado de la consulta:', result)

except psycopg2.Error as e:
    print('Error al conectar a la base de datos:', e)

finally:
    # Cerrar el cursor y la conexión
    if cur:
        cur.close()
    if conn:
        conn.close()
