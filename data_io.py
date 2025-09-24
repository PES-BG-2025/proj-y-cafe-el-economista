# Anotaciones Berni
# ================================================================================ --- IGNORE ---
#Esto nos permitirá importar y leer archivos CSV
import csv 
# Para poder manejar rutas de archivos de manera más sencilla
from pathlib import Path

carpeta_catalogo = Path("datos/catalogos")

#Definir la primera función para leer catálogo de bebidas
def leer_bebidas():

# Creamos la ruta completa al archivo CSV
    ruta = carpeta_catalogo / "bebidas_menu.csv"

# Abrimos el archivo y leemos su contenido y lo almacenamos en un diccionario en f 
    with open(ruta, newline="", encoding='utf-8-sig') as f:
        # leer el archivo CSV y indicar que el delimitador es una coma
        archivo = csv.DictReader(f, delimiter=',')
        print(archivo.fieldnames)  # Imprime los nombres de las columnas
        bebidas = []
        for fila in archivo:
            
            bebidas.append(fila)
    return bebidas
