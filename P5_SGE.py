import random
import statistics 
from prettytable import PrettyTable

# Pedir al usuario el nombre del archivo de texto a crear
nombreArchivo = input("Introduzca el nombre del archivo de texto que desea crear: ")

# Preguntar las características
lista = []
rangos = []
for i in range(5):
    caracteristica = input(f"Introduce la característica {i+1}: ")
    lista.append(caracteristica)
    rmax = int(input(f"Introduce el valor máximo para {caracteristica}: "))
    rmin = int(input(f"Introduce el valor mínimo para {caracteristica}: "))
    
    rangos.append((rmax, rmin))



try:
    f = open(nombreArchivo,"w") # Abrir fichero para escribir
except Exception:
    exit()

#escribimos caracteristicas primero
for i in range(len(lista)):
        f.write(lista[i])
        if i < len(lista) - 1:
            f.write(", ")
        else:
            f.write("\n")

 # Generar los valores aleatorios para cada característica y escribirlos en el archivo
for i in range(1000):
    # Creo una lista vacía para almacenar los valores aleatorios de cada característica
    valores = []
    # Para cada característica en la lista "rangos"
    for caracteristica in rangos:
        
        rmax, rmin = caracteristica # Paso a rmin y rmax los valores de caracteristica
        aleatorio = random.randint(rmin, rmax)
        # Agrego el valor aleatorio a la lista de valores
        valores.append(aleatorio)
    # Escribir los valores en el archivo separados por comas y con un salto de línea al final
    linea = ""
    for aleatorio in valores:
        linea += str(aleatorio) + ", "
    linea = linea[:-2] + "\n" # Eliminar la última coma y agregar un salto de línea
    f.write(linea)

f.close() # Cerrar








#PARTE 2

   # Preguntar por el nombre del archivo
nombreArchivo = input("Introduce el nombre del archivo: ")



try:
 f = open(nombreArchivo,"r") # Abrir fichero para leer
except Exception:
 exit()

 # Leer la primera línea para obtener las características
lista = f.readline().strip().split(", ")


 # Inicializamos
varianza = {}
media = {}
moda = {}
maximo = {}
minimo = {}

# Para leer valores de cada columna
valores_columna = []
for i in range(len(lista)):
    valores_columna.append([])  # Inicializo lista para cada columna
    
for linea in f:
    datos = linea.strip().split(", ")
    for i in range(len(lista)):
        if datos[i]: #si no esta vacio
            valores_columna[i].append(float(datos[i]))

# Calcular estadísticas para cada columna
valores_caracteristica = []
for i in range(len(lista)):
    caracteristica = lista[i]
    valores_caracteristica = valores_columna[i]
    media[caracteristica] = statistics.mean(valores_caracteristica)
    varianza[caracteristica] = statistics.variance(valores_caracteristica)
    moda[caracteristica] = statistics.mode(valores_caracteristica)
    maximo[caracteristica] = max(valores_caracteristica)
    minimo[caracteristica] = min(valores_caracteristica)




f.close() # Cerrar



    


    


# Crear tabla
table = PrettyTable()
table.field_names = ["Característica", "Media", "Moda", "Máximo", "Mínimo", "Varianza"]

# Agregar filas a la tabla
for caracteristica in lista:
    table.add_row([
        caracteristica,
        f"{media[caracteristica]:.2f}", #para mostrar con dos decimales
        f"{moda[caracteristica]}",
        f"{maximo[caracteristica]}",
        f"{minimo[caracteristica]}",
        f"{varianza[caracteristica]:.2f}" #para mostrar con dos decimales
    ])

# Imprimir tabla
print(table)