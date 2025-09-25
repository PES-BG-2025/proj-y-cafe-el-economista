# ====================================================================================
# Banco de Guatemala
# Septiembre 2025
#
# Proyecto: caja registradora para café "El Economista"
#
#Integrantes:
# Chuvac González, Berni Alejandro
# Pérez Romero, Rita Guadalupe
# ==================================================================================
# ================================================================================ --- IGNORE ---
#Esto nos permitirá importar y leer archivos CSV
import csv 
import datetime
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
    # Ruta completa al archivo CSV
    ruta = carpeta_catalogo / "modificadores.csv"
    # Abrimos y procesamos el archivo
    with open(ruta, newline="", encoding="utf-8-sig") as f:
        archivo = csv.DictReader(f, delimiter=",")
        modificadores = []
        for fila in archivo:
            # Igual que modificadores: limpiamos espacios y convertimos tipos
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
#Manejo de cierre de ventas
 # ================================================================================

# Genera el cierre diario de ventas
def generar_cierre_diario():
  # Fecha de hoy en formato "YYYY-MM-DD"
  hoy = datetime.date.today().isoformat()

  # Archivo del cierre del día (uno por fecha)
  ruta = Path("datos/cierres") / f"cierre_caja_{hoy}.csv"

  # Leer pedidos del día desde pedidos.csv
  pedidos_hoy = []
  pedidos_path = Path("datos/ventas_del_dia/pedidos.csv")
  if pedidos_path.exists():
    with open(pedidos_path, newline="", encoding="utf-8-sig") as f:
      archivo = csv.DictReader(f)
      for fila in archivo:
        # Solo pedidos cuya fecha empieza con "hoy"
        if fila["fecha_hora"].startswith(hoy):
          pedidos_hoy.append(fila)

  # Calcular total y número de pedidos
  total_dia = 0.0
  for p in pedidos_hoy:
    total_dia += float(p["total_pedido"])
  num_pedidos = len(pedidos_hoy)

  # Guardar cierre del día en su archivo propio
  with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
    campos = ["fecha", "num_pedidos", "total_dia"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerow({
      "fecha": hoy,
      "num_pedidos": num_pedidos,
      "total_dia": f"{total_dia:.2f}"
    })

  # Actualizar también el acumulado de cierres generales
  registrar_cierre_general(hoy, num_pedidos, total_dia)

  # Mensaje de confirmación en consola
  print(f"Cierre del {hoy} generado en {ruta}")


# ================================================================================
#Manejo de cierre de ventas
 # ================================================================================
 # Genera un reporte resumido de ventas del día
def generar_reporte_resumido_dia(bebidas, bakery):
    # Fecha de hoy en "YYYY-MM-DD"
    hoy = datetime.date.today().isoformat()

    # Archivo donde se registran las ventas
    ruta_ventas = Path("datos/ventas_del_dia/ventas.csv")

    # Diccionario con el resumen y total acumulado
    resumen = {}
    total_dia = 0.0

    # Si no existe el archivo, devolver vacío
    if not ruta_ventas.exists():
        return resumen, total_dia

    # Función interna para obtener nombre desde el id
    def obtener_nombre(id_item):
        # Buscar en bebidas
        for producto in bebidas:
            if producto.get("id_bebida") == id_item:
                return producto.get("nombre", id_item)
        # Buscar en bakery
        for producto in bakery:
            if producto.get("id_producto") == id_item:
                return producto.get("nombre", id_item)
        return id_item  # si no lo encuentra

    # Leer ventas y armar el resumen del día
    with open(ruta_ventas, newline="", encoding="utf-8-sig") as f:
        archivo = csv.DictReader(f)
        for fila in archivo:
            # Filtrar solo ventas de hoy
            if hoy in fila["fecha_hora"]:
                nombre = obtener_nombre(fila["id_item"])
                cantidad = int(fila["cantidad"])
                total_linea = float(fila["total_linea"])
                total_dia += total_linea

                # Si el producto no está en el resumen, inicializarlo
                if nombre not in resumen:
                    resumen[nombre] = {"cantidad": 0, "total": 0.0}

                # Acumular cantidad y total
                resumen[nombre]["cantidad"] += cantidad
                resumen[nombre]["total"] += total_linea

    # Retornar el resumen y el total del día
    return resumen, total_dia

