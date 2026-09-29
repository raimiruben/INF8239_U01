def pareto_flags(df, score="f1_macro", cost="fit_median_s"):
    """Retorna una lista de booleanos indicando si cada fila es un punto de Pareto."""
    
    # 1. Buscamos qué filas están dominadas por alguna otra del DataFrame
    es_dominado = (
        (df[score].values[:, None] > df[score].values) & (df[cost].values[:, None] <= df[cost].values)
    ) | (
        (df[score].values[:, None] == df[score].values) & (df[cost].values[:, None] < df[cost].values)
    )
    
    # 2. Si alguna fila (columna en la matriz) domina a la fila actual, esta es dominada
    dominados = es_dominado.any(axis=0)
    
    # 3. Los puntos de Pareto son aquellos que NO son dominados
    return (~dominados).tolist()