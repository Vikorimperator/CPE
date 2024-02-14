# Cargamos los modulos a emplear
import psycopg2
from psycopg2 import sql
import pandas as pd
from io import StringIO
import os
import sys
from dotenv import load_dotenv

# Definimos las rutas de los archivos a emplear
notebook_dir = os.getcwd()
scripts_dir = os.path.join(notebook_dir, "..", "src")
sys.path.append(scripts_dir)

# Cargamos variables de entorno
load_dotenv()

# Obtenemos los valores de las variables de entorno
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Conexión a la base de datos
conn = psycopg2.connet(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Creamos un cursor y abrimos un archivo temporal para copiar los datos
cur = conn.cursor()
temp_file = StringIO()
temp_file.write(csv_data)
temp_file.seek(0)

# Copiamos los datos desde el archivo temporal a la tabla cimas
cur.copy_from(temp_file, 'cimas', columns=df.columns, sep='\t')
conn.commit()

# Cerramos la conexión y el cursor
cur.close()
conn.close()
