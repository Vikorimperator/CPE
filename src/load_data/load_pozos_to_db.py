# cargamos los modulos a emplear
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
logs_file_name = 'registros_cpe.csv'
path_well_logs = os.path.join(file_dir, 'data', 'raw', logs_file_name)

# Cargamos la información de los pozos desde el archivo csv
well_logs_df = load_csv(path_well_logs)

# verificamos que no existan valores negativos en la columna md
well_logs_df = well_logs_df[well_logs_df['md'] >= 0]

# Obtenemos los valores unicos de la columna "wellname"
pozos_unicos = well_logs_df["wellname"].unique()

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

# Creamos un cursor y abrimos un archivo temporal para copiar los datos
cur = conn.cursor()

# Obtenemos el campo_id del campo de la tabla campos
campo = "Caparroso-Pijije-Escuintle"
query = "SELECT campo_id FROM campos WHERE nombre_campo = %s"
cur.execute(query, (campo,))
campo_id = cur.fetchone()[0]

# Insertar registros en la tabla pozos utilizando el campo_id obtenido
def insert_well_logs(row):
    query = "INSERT INTO pozos (nombre_pozo, campo_id, fecha_creacion, actualizado) VALUES (%s, %s, now(), now())"
    cur.execute(query, (row["wellname"], campo_id))

# Aplicar la función insert_well_logs a cada fila del DataFrame well_logs_df
well_logs_df.apply(insert_well_logs, axis=1)

# Confirmar la inserción
conn.commit()

# Cerrar el cursor y la conexión
cur.close()
conn.close()

# Calculamos el tiempo de ejecución
tiempo_fin = time.time()
tiemepo_ejecución = tiempo_fin - tiempo_inicio

# Imprimimos el tiempo de ejecución y un mensaje
print(f'Tiempo de ejecución: {tiemepo_ejecución} segundos.')
print("Script ejecutado.")