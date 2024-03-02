# Cargamos los modulos a emplear
import psycopg2
import csv
import time
from dotenv import load_dotenv
import os
import sys

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

# Cargamos variables de entorno
load_dotenv()

# Obtenemos los valores de las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Conexion a la base de datos
conn = psycopg2.connect(
    dbname="bronce",
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Creamos un cursor y abrimos un archivo temporal para copiar los datos
cur = conn.cursor()

# Definimos la ruta del archivo csv
logs_file_name = 'registros_cpe.csv'
csv_file = os.path.join(file_dir, 'data', 'raw', logs_file_name)

# Abrir el archivo CSV
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la primera fila (encabezado)
    next(reader)  # Saltar la segunda fila (unidades)
    for row in reader:
        # Insertar la fila en la base de datos
        cur.execute(
            "INSERT INTO registros (pozo, md, bound_water, calcite, cgr, dolomite, dtco, gr, illite, nphi, phit, phie, rhob, rp, sw, uoil, uwater, vsh) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

# Confirmar la transacción
conn.commit()

# Cerrar la conexión
cur.close()
conn.close()

# Calculamos el tiempo de ejecución
tiempo_fin = time.time()
tiemepo_ejecución = tiempo_fin - tiempo_inicio

# Imprimimos el tiempo de ejecución y un mensaje
print(f'Tiempo de ejecución: {tiemepo_ejecución} segundos.')
print("Script ejecutado.")