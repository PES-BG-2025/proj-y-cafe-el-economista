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
        bebidas = []
        for fila in archivo:
# Agregamos cada fila del archivo CSV a la lista bebidas
            bebidas.append({"id_bebida": fila["id_bebida"].strip(),"nombre": fila["nombre"].strip(), "precios_base": float(fila["precios_base"].strip()),"categoria": fila["categoria"].strip(),"activo": int(fila["activo"].strip())})
    return bebidas
# Probamos la función
if __name__ == "__main__":
    print(leer_bebidas)


    # ================================================================================ 
# Leer catálogo de productos de panadería (bakery)
# ================================================================================
def leer_bakery():
    # Ruta completa al archivo CSV
    ruta = carpeta_catalogo / "bakery_menu.csv"

    # Abrimos y procesamos el archivo
    with open(ruta, newline="", encoding='utf-8-sig') as f:
        archivo = csv.DictReader(f, delimiter=',')
        productos = []
        for fila in archivo:
            # Igual que bebidas: limpiamos espacios y convertimos tipos
            productos.append({"id_producto": fila["id_producto"].strip(),"nombre": fila["nombre"].strip(),"precio": float(fila["precio"].strip()), "stock": int(fila["stock"].strip()),"activo": int(fila["activo"].strip())})
    return productos

