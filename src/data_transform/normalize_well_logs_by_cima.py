from data_transform.normalize_well_log import normalize_well_log
import pandas as pd


def normalize_well_logs_by_cima(df, cimas_interes, key_well, curve_names, quanti_low=0.05, quanti_high=0.95):
    """
    Normaliza las curvas de pozo para cada cima especificada y agrega las columnas de curvas normalizadas al DataFrame de cada arena.

    Args:
    - df: DataFrame principal que contiene los datos de los pozos.
    - cimas_interes: Lista de nombres de cimas que se utilizarán para la normalización.
    - key_well: Nombre del pozo clave utilizado como referencia para la normalización.
    - curve_names: Lista de nombres de las curvas que se normalizarán.
    - quanti_low: Cuantil inferior para la normalización (por defecto 0.05).
    - quanti_high: Cuantil superior para la normalización (por defecto 0.95).

    Returns:
    - Lista de DataFrames, cada uno conteniendo las curvas normalizadas para una arena específica.

    """

    # Lista para almacenar los DataFrames de curvas normalizadas
    normalized_curves_data = []

    for cima in cimas_interes:
        # Obtener el DataFrame de la arena correspondiente
        arena_df = df[df["cima"] == cima].copy()

        # Eliminar valores nulos de las curvas que se van a normalizar
        arena_df.dropna(subset=curve_names, inplace=True)

        # Obtener los cuantiles para la normalización del pozo clave para cada curva
        key_well_data = arena_df[arena_df["wellname"] == key_well]
        quanti_low_values = key_well_data[curve_names].quantile(quanti_low)
        quanti_high_values = key_well_data[curve_names].quantile(quanti_high)

        # Calcular percentiles bajos y altos para cada pozo para cada curva
        low_percentile = arena_df.groupby(
            "wellname")[curve_names].quantile(quanti_low)
        high_percentile = arena_df.groupby(
            "wellname")[curve_names].quantile(quanti_high)

        # Normalizar cada curva de pozo para la arena y agregar la columna de curva normalizada
        for curve_name in curve_names:
            arena_df[curve_name + "_norm"] = arena_df.apply(
                lambda x: normalize_well_log(x[curve_name], quanti_low_values[curve_name],
                                             quanti_high_values[curve_name], low_percentile[curve_name][x["wellname"]],
                                             high_percentile[curve_name][x["wellname"]]),
                axis=1
            )

        # Agregar el DataFrame de la arena normalizada a la lista de datos de arena
        normalized_curves_data.append(arena_df)

    return normalized_curves_data
