import random
import statistics
from prettytable import PrettyTable

# Pedir al usuario el nombre del archivo de texto a crear
file_name = input("Introduzca el nombre del archivo de texto que desea crear: ")

# Preguntar las características
features = []
ranges = []
for i in range(5):
    feature = input(f"Introduce la característica {i+1}: ")
    features.append(feature)
    rmin = int(input(f"Introduce el valor mínimo para {feature}: "))
    rmax = int(input(f"Introduce el valor máximo para {feature}: "))
    ranges.append((rmin, rmax))

# Generar los 1000 registros
with open(file_name, "w") as f:
    # Escribir las características en la primera línea
    f.write(", ".join(features) + "\n")
    
    for i in range(1000):
        # Generar los valores aleatorios para cada característica
        values = [random.randint(rmin, rmax) for (rmin, rmax) in ranges]
        # Escribir los valores en el archivo
        f.write(", ".join(map(str, values)) + "\n")

   # Preguntar por el nombre del archivo
file_name = input("Introduce el nombre del archivo: ")

# Leer el archivo y calcular las estadísticas
with open(file_name, "r") as f:
    # Leer la primera línea para obtener las características
    features = f.readline().strip().split(", ")
    
    # Inicializar los diccionarios para guardar las estadísticas
    means = {feature: 0 for feature in features}
    modes = {feature: None for feature in features}
    maxs = {feature: float("-inf") for feature in features}
    mins = {feature: float("inf") for feature in features}
    variances = {feature: 0 for feature in features}

    # Leer los registros y actualizar las estadísticas
    data = []
    for line in f:
        record = line.strip().split(", ")
        data.append([int(x) for x in record])
        for i, value in enumerate(record):
            feature = features[i]
            value = int(value)
            means[feature] += value
            maxs[feature] = max(maxs[feature], value)
            mins[feature] = min(mins[feature], value)
            variances[feature] += value**2

    # Calcular las medias y varianzas
    n = len(data)
    for feature in features:
        means[feature] /= n
        variances[feature] = variances[feature]/n - means[feature]**2
        modes[feature] = max(set(data[i][features.index(feature)] for i in range(n)), key=lambda x: [data[i][features.index(feature)] for i in range(n)])






# Crear tabla
table = PrettyTable()
table.field_names = ["Característica", "Media", "Moda", "Máximo", "Mínimo", "Varianza"]

# Agregar filas a la tabla
for feature in features:
    table.add_row([
        feature,
        f"{means[feature]:.2f}",
        f"{modes[feature]}",
        f"{maxs[feature]}",
        f"{mins[feature]}",
        f"{variances[feature]:.2f}"
    ])

# Imprimir tabla
print(table)