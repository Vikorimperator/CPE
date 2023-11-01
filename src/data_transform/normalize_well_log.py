def normalize_well_log(curve, ref_low, ref_high, well_low, well_high):
    """
    Normaliza una curva de pozo utilizando el método de normalización propuesto por Shier en 2004.

    Args:
    - curve (pandas.Series): Serie de pandas que representa la curva de pozo que se va a normalizar.
    - ref_low (float): Valor mínimo de referencia para la normalización.
    - ref_high (float): Valor máximo de referencia para la normalización.
    - well_low (float): Valor mínimo en la curva del pozo que se va a normalizar.
    - well_high (float): Valor máximo en la curva del pozo que se va a normalizar.

    Returns:
    - pandas.Series: Serie de pandas que representa la curva normalizada.

    Esta función toma una serie de datos (representando una curva de pozo), junto con los valores mínimos y máximos
    de referencia (ref_low y ref_high) y los valores mínimos y máximos de la curva de pozo (well_low y well_high).
    Normaliza la curva de pozo utilizando el método de normalización propuesto por Shier en 2004 y devuelve la curva normalizada.
    """
    normalized_curve = ref_low + \
        ((ref_high - ref_low) * ((curve - well_low) / (well_high - well_low)))
    return normalized_curve
