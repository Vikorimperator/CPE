import os


def save_data_csv(df, pozos_interes, nombre_archivo):
    """
    Guarda información específica de un DataFrame en un archivo CSV.

    Args:
    - df: DataFrame de pandas.
    - pozos_interes: Lista de nombres de pozos que se guardarán en el archivo CSV.
    - nombre_archivo: Nombre del archivo CSV donde se guardarán los datos.

    Returns:
    - None (guarda los datos en un archivo CSV).
    """
    # Filtra el DataFrame para incluir solo los pozos de interés y las columnas que terminan con '_norm', 'md' y 'wellname'
    columnas_interes = [col for col in df.columns if col.endswith(
        '_norm') or col == 'md' or col == 'wellname']
    datos_a_guardar = df[df['wellname'].isin(pozos_interes)][columnas_interes]

    # Obtiene el directorio del script actual
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta del directorio 'processed' dentro de la estructura del proyecto
    ruta_guardado = os.path.join(
        script_directory, '..', '..', 'data', 'processed')

    # Si la ruta no existe, crea los directorios necesarios
    if not os.path.exists(ruta_guardado):
        os.makedirs(ruta_guardado)

    # Guarda los datos en un archivo CSV
    ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
    datos_a_guardar.to_csv(ruta_completa, index=False)
