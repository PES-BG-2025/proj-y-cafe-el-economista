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
# ================================================================================
# Leer catálogo de modificadores (tamaños y extras)
# ================================================================================
def leer_modificadores():
    ruta = carpeta_catalogo / "modificadores.csv"

    with open(ruta, newline="", encoding="utf-8-sig") as f:
        archivo = csv.DictReader(f, delimiter=",")
        modificadores = []
        for fila in archivo:
            modificadores.append({
                "id_modificador": fila["id_modificador"].strip(),
                "nombre": fila["nombre"].strip(),
                "tipo": fila["tipo"].strip(),  # "tamaño" o "extra"
                "precio_extra": float(fila["precio_extra"].strip()),
                "activo": int(fila["activo"].strip())
            })
    return modificadores
# ================================================================================ 
# Funciones de escritura
# ================================================================================ 
def actualizar_bakery(bakery: list[dict]):
  ruta =carpeta_catalogo/ "bakery_menu.csv"
  # El modo w es para borrar lo que ya tenía el archivo y escribir de nuevo
  with open(ruta, mode="w", newline="", encoding="utf-8-sig") as f:
    campos = ["id_producto", "nombre", "categoria", "existencias", "precio_unitario", "activo"]
    # Escribir es un objeto que permite escribir en el archivo csv
    escribir = csv.DictWriter(f, fieldnames=campos, delimiter=",")
    # Escribir la cabecera
    escribir.writeheader()
    # Escribir las filas
    for producto in bakery:
      escribir.writerow({
        "id_producto": producto["id_producto"],
        "nombre": producto["nombre"],
        "categoria": producto["categoria"],
        "existencias": producto["existencias"],
        "precio_unitario": f"{producto['precio_unitario']:.2f}",
        "activo": producto["activo"]
      })
# ================================================================================ 
#para que se haga la factura
def guardar_lineas(pedido, id_pedido):
  ruta = Path("datos/ventas_del_dia/ventas.csv")
  # No borra lo que ya tiene el archivo, sino que agrega al final por eso es mode="a"
  with open(ruta, mode="a", newline="", encoding="utf-8-sig") as f:
    campos = ["fecha_hora","id_ticket","id_linea","tipo_item","id_item","cantidad","precio_unitario","total_linea"]
    writer = csv.DictWriter(f, fieldnames=campos)
    # tell devuelve la posición actual del cursor en el archivo, si es 0 es que el archivo está vacío y hay que escribir la cabecera
    if f.tell() == 0:
      writer.writeheader()
    for linea in pedido["lineas"]:
      writer.writerow({
        "fecha_hora": pedido["fecha_hora"],
        "id_ticket": id_pedido,
        "id_linea": linea["id_linea"],
        "tipo_item": linea["tipo"],
        "id_item": linea["id_item"],
        "cantidad": linea["cantidad"],
        "precio_unitario": f"{linea['precio_unitario']:.2f}",
        "total_linea": f"{linea['total_linea']:.2f}"
      })
# ================================================================================ 
      
#definir 4 funciones 

# funcion para guardar los archivos en un csv

# ================================================================================ 
# Guarda un pedido en pedidos.csv
def guardar_pedido(pedido, pago_info, id_pedido):
  # Ruta del archivo donde se guardan los pedidos
  ruta = Path("datos/ventas_del_dia/pedidos.csv")

  # Abrir en modo "a" → agregar al final sin borrar
  with open(ruta, mode="a", newline="", encoding="utf-8-sig") as f:
    # Definir columnas del archivo
    campos = ["id_pedido","fecha_hora","total_pedido","metodo_pago","monto_pagado","cambio"]

    # Escritor que usa diccionarios
    writer = csv.DictWriter(f, fieldnames=campos)

    # Si el archivo está vacío → escribir cabecera
    if f.tell() == 0:  
      writer.writeheader()

    # Escribir una fila con la info del pedido
    writer.writerow({
      "id_pedido": id_pedido,
      "fecha_hora": pedido["fecha_hora"],
      "total_pedido": f"{pedido['total']:.2f}", 
      "metodo_pago": pago_info["metodo"],
      "monto_pagado": f"{pago_info['monto']:.2f}",
      "cambio": f"{pago_info['cambio']:.2f}"
    })

    # ================================================================================ 
# PARA GUARDAR LOS MODIFICADORES
    # ================================================================================ 
    # Guarda los modificadores de un pedido en ventas_modificadores.csv
def guardar_modificadores(pedido, id_pedido):
  # Ruta del archivo donde se guardan los modificadores
  ruta = Path("datos/ventas_del_dia/ventas_modificadores.csv")

  # Abrir en modo "a" → agregar al final sin borrar
  with open(ruta, mode="a", newline="", encoding="utf-8-sig") as f:
    # Definir columnas del archivo
    campos = ["id_ticket","id_linea","id_modificador","cantidad","ajuste_total"]
    writer = csv.DictWriter(f, fieldnames=campos)

    # Si el archivo está vacío → escribir cabecera
    if f.tell() == 0:
      writer.writeheader()

    # Recorrer cada línea del pedido y sus modificadores
    for linea in pedido["lineas"]:
      for mod in linea["modificadores"]:
        # Guardar fila con datos del modificador
        writer.writerow({
          "id_ticket": id_pedido,
          "id_linea": linea["id_linea"],
          "id_modificador": mod["id_modificador"],
          "cantidad": 1,  # cada modificador cuenta como uno
          "ajuste_total": f"{mod['ajuste_precio']:.2f}"
        })
 # ================================================================================
# PARA EL CIERRE GENERAL
  # ================================================================================

# Registra el cierre general de un día en cierres_generales.csv
def registrar_cierre_general(fecha, num_pedidos, total_dia):
  # Ruta del archivo donde se guardan los cierres
  ruta = Path("datos/cierres/cierres_generales.csv")

  # Abrir en modo "a" → agregar al final sin borrar
  with open(ruta, "a", newline="", encoding="utf-8-sig") as f:
    # Definir columnas del archivo
    campos = ["fecha", "num_pedidos", "total_dia"]
    writer = csv.DictWriter(f, fieldnames=campos)

    # Si el archivo está vacío → escribir cabecera
    if f.tell() == 0:
      writer.writeheader()

    # Guardar fila con los datos del cierre
    writer.writerow({
      "fecha": fecha,
      "num_pedidos": num_pedidos,
      "total_dia": f"{total_dia:.2f}"
    })

     # ================================================================================


