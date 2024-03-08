# Cargamos los modulos a emplear
from dotenv import load_dotenv
from io import StringIO
from psycopg2 import sql
import psycopg2
import pandas as pd
import sys
import os
import time

# Guardamos el tiempo de inicio
tiempo_inicio = time.time()

# Obtener el directorio actual del script
file_dir = os.getcwd()

# Agregamos el directorio 'src' al path
src_dir = os.path.join(file_dir, 'src')
sys.path.append(src_dir)

# Agregamos el directorio 'data_transform' al path
data_transform_dir = os.path.join(src_dir, 'data_transform')
sys.path.append(data_transform_dir)

# Importamos la funcion load_csv
from data_transform.load_csv import load_csv

# Definimos la ruta del archivo csv
cimas_file_name = 'cimas_cpe.csv'
cimas = os.path.join(file_dir, 'data', 'raw', cimas_file_name)

# Cargamos la información de los pozos desde al archivo csv
cimas_df = load_csv(cimas)

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

# Obtener todos los pozos de la base de datos
pozos_df = pd.read_sql_query("SELECT nombre_pozo, pozo_id FROM pozos", conn)

# Fusionar cimas_df con pozos_df para obtener pozo_id
cimas_df = cimas_df.merge(pozos_df, left_on='wellname', right_on='nombre_pozo', how='left')

# Eliminar columnas innecesarias
cimas_df.drop(columns=['wellname', 'nombre_pozo', 'zonedescription'], inplace=True)

# Insertar valores en la tabla cimas
for index, row in cimas_df.iterrows():
    # Verificar si la cima ya existe
    cur.execute("SELECT cima_id FROM cimas WHERE nombre_cima = %s AND pozo_id = %s", (row['surface'], row['pozo_id']))
    existing_cima = cur.fetchone()
    if existing_cima:
        print(f"La cima {row['surface']} para el pozo {row['pozo_id']} ya existe.")
    else:
        query = sql.SQL("INSERT INTO cimas (nombre_cima, pozo_id, cima_md, fecha_creacion, actualizado) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)")
        values = (row['surface'], row['pozo_id'], row['md'])
        print(f"Intentando insertar: {values}")
        try:
            cur.execute(query, values)
            print("Inserción exitosa.")
        except Exception as e:
            print(f"Error al insertar: {e}")

# Cerrar conexión
cur.close()
conn.close()

# Calculamos el tiempo de ejecución
tiempo_fin = time.time()
tiemepo_ejecución = tiempo_fin - tiempo_inicio

# Imprimimos el tiempo de ejecución y un mensaje
print(f'Tiempo de ejecución: {tiemepo_ejecución} segundos.')
print("Script ejecutado.")