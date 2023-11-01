import pandas as pd


def print_unique_values(df, columna):
    """
    Imprime los valores únicos en una columna de un DataFrame como un string.

    Args:
    - df: DataFrame de pandas.
    - columna: Nombre de la columna del DataFrame cuyos valores únicos se imprimirán.

    Returns:
    - None (imprime los valores únicos como un string).
    """
    valores_unicos = df[columna].unique()
    valores_unicos_str = ', '.join(map(str, valores_unicos))
    print(f"Valores únicos en la columna '{columna}': {valores_unicos_str}")
