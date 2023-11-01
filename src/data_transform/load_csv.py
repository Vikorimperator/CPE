import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """
    Función para cargar información cruda de formato CSV de Techlog. Cambia el nombre de la columna 'DEPTH' o 'DEPT' a 'MD' si está presente.

    Args:
    - path: La ruta donde se encuentra el archivo CSV a cargar en formato string.

    Returns:
    - Regresa un DataFrame generado de un archivo CSV sin la columna datasetName, con los nombres de las columnas en minúscula y con las columnas adecuadas como float.
    La columna datasetName se genera de manera automática en el CSV, pero no es de interés.
    """

    df = pd.read_csv(path, header=0, skiprows=[1], na_values=[-9999])
    df.drop("datasetName", axis=1, inplace=True)
    df.columns = df.columns.str.lower()

    # Cambia el nombre de la columna depth o dept a MD si está presente
    if 'depth' in df.columns:
        df.rename(columns={'depth': 'md'}, inplace=True)
    elif 'dept' in df.columns:
        df.rename(columns={'dept': 'md'}, inplace=True)
    elif 'top' in df.columns:
        df.rename(columns={'top': 'md'}, inplace=True)

    # Cambia el nombre de la columna zone name a surface si esta presente
    if 'zone name' in df.columns:
        df.rename(columns={'zone name': 'surface'}, inplace=True)
    elif 'zone_name' in df.columns:
        df.rename(columns={'zone_name': 'surface'}, inplace=True)

    return df
