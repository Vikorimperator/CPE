import pandas as pd


def map_cimas_create_columns(cimas_df: pd.DataFrame, well_df: pd.DataFrame, periodo: False) -> pd.DataFrame:
    """
    Función para mapear las cimas a sus respectivas profundidades y crear columnas booleanas por periodo en el DataFrame de registros de pozo.

    Args:
    - cimas_df: Un DataFrame con el nombre de las cimas en una columna y las profundidades en otra
    - well_df: Un DataFrame con la información de los registros de pozo
    - periodo: Un valor booleano que indica si se deben crear columnas booleanas por periodo (Cretácico, Jurásico, Terciario). 
               Por defecto, es False.

    Returns:
    - Regresa un DataFrame con la información de las cimas mapeadas, los registros de pozo y columnas booleanas por periodo.
    """

    # Creamos un diccionario para mapear las cimas por pozo
    cimas_mapping = {}

    # Agrupamos las cimas por el nombre del pozo
    for _, row in cimas_df.iterrows():
        well_name = row['wellname']
        cima_name = row['surface']
        cima_depth = row['md']

        # Verificamos si el pozo ya está en el diccionario
        if well_name not in cimas_mapping:
            cimas_mapping[well_name] = []

        # Agregamos la cima al pozo correspondiente
        cimas_mapping[well_name].append((cima_name, cima_depth))

    # Iteramos a través de los pozos y asignamos las cimas en función de las profundidades
    for well_name, well_data in well_df.groupby('wellname'):
        if well_name in cimas_mapping:
            cimas_mapping[well_name].sort(key=lambda x: x[1])
            for i in range(len(cimas_mapping[well_name])):
                current_top, current_depth = cimas_mapping[well_name][i]
                next_depth = cimas_mapping[well_name][i + 1][1] if i < len(
                    cimas_mapping[well_name]) - 1 else float('inf')
                well_df.loc[(well_df['wellname'] == well_name) & (well_df['md'] >= current_depth) & (
                    well_df['md'] < next_depth), 'cima'] = current_top

    # Cambiamos a minúsculas los nombres de las cimas
    well_df['cima'] = well_df['cima'].str.lower()

    if periodo:
        # Creamos las columnas booleanas por periodo
        cretacico = ["mndz", "snfl", "agnv", "crtcm", "crti"]
        jurasico = ["ttnno", "kmmgi", "sal_mes"]

        well_df['cretacico'] = well_df['cima'].apply(lambda x: x in cretacico)
        well_df['jurasico'] = well_df['cima'].apply(lambda x: x in jurasico)
        well_df['terciario'] = well_df['cima'].apply(
            lambda x: not (x in cretacico or x in jurasico))

    else:
        # Obtén las columnas booleanas para cada etiqueta y establece el nombre de la columna como el valor de la etiqueta
        df_etiquetas = pd.get_dummies(well_df["cima"])

        # Concatena las nuevas columnas booleanas con el DataFrame original
        well_df = pd.concat([well_df, df_etiquetas], axis=1)

        # Elimina la columna original de cimas si lo deseas
        well_df = well_df.drop(columns=['cima'])

    return well_df
