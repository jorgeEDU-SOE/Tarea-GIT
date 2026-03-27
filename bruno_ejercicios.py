def calcular_estadisticas(datos):
    if not datos:
        return None

    # Ordenar los datos es clave para mediana y moda
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)

    # 1. Calcular Media (Promedio)
    media = sum(datos_ordenados) / n

    # 2. Calcular Mediana (El valor central)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]

    # 3. Calcular Moda (El valor que más se repite)
    frecuencias = {}
    for x in datos_ordenados:
        frecuencias[x] = frecuencias.get(x, 0) + 1
    
    max_frecuencia = max(frecuencias.values())
    moda = [k for k, v in frecuencias.items() if v == max_frecuencia]

    return media, mediana, moda

# Lista de prueba (ejemplo de edades o notas)
mis_datos = [15, 18, 20, 20, 22, 25, 30, 20, 18]

media, mediana, moda = calcular_estadisticas(mis_datos)

print("--- Resultados de Estadística Básica ---")
print(f"Datos: {mis_datos}")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")