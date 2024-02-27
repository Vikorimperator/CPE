import pandas as pd


def generar_intervalos_disparados(df):
    """
    Genera dos columnas booleanas 'sin_manifestar' y 'productor' en un DataFrame de disparos.

    Parameters:
    - df (DataFrame): DataFrame con información de disparos.

    Returns:
    - DataFrame: DataFrame actualizado con las columnas 'sin_manifestar' y 'productor'.
    """
    sin_manifestar = []
    productor = []

    cima = None

    for idx, row in df.iterrows():
        if row['Zone Name'] == 'SIN MANIFESTAR' or row['Zone Name'] == 'PRODUCTOR':
            if cima is not None:
                base = idx
                if df.loc[base, 'ZoneDescription'] == -9999:
                    sin_manifestar.append((cima, base))
                else:
                    productor.append((cima, base))
                cima = None
        elif row['ZoneDescription'] == -9999:
            cima = idx

    # Crear las columnas en el DataFrame
    df['sin_manifestar'] = False
    df['productor'] = False

    for cima, base in sin_manifestar:
        df.loc[cima:base, 'sin_manifestar'] = True

    for cima, base in productor:
        df.loc[cima:base, 'productor'] = True

    return df
