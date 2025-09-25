# =============================================================
# Banco de Guatemala
# Septiembre 2025
#
# Proyecto: caja registradora para café "El Economista"
#
#Integrantes:
# Chuvac González, Berni Alejandro
# Pérez Romero, Rita Guadalupe
# ===========================================================


import tkinter as tk

# Datos de prueba, luego se cambia a leer desde CSV
BEBIDAS = [
  {"id_bebida": "LATTE-12", "nombre": "Latte 12oz", "precio_base": 22.0, "categoría": "espresso", "activo": 1},
  {"id_bebida": "ESP-DBL", "nombre": "Espresso doble", "precio_base": 15.0, "categoría": "espresso", "activo": 1},
  {"id_bebida": "CAP-12", "nombre": "Cappuccino 12oz", "precio_base": 22.0, "categoría": "espresso", "activo": 1},
]

MODIFICADORES = [
  {"id_modificador": "LECHE-ENT", "nombre": "Leche entera", "tipo": "leche", "ajuste_precio": 0.0},
  {"id_modificador": "LECHE-COCO", "nombre": "Leche de coco", "tipo": "leche", "ajuste_precio": 3.0},
  {"id_modificador": "SHOT-DBL", "nombre": "Doble shot", "tipo": "shot", "ajuste_precio": 3.0},
  {"id_modificador": "JAR-CAR", "nombre": "Jarabe caramelo", "tipo": "jarabe", "ajuste_precio": 2.0},
]

BAKERY = [
  {"id_producto": "PROD-001", "nombre": "Pastelito 1", "categoría": "pastel azul", "existencias": 48, "precio_unitario": 6.0, "activo": 1},
  {"id_producto": "PROD-001", "nombre": "Pastelito 2", "categoría": "pastel rojo", "existencias": 12, "precio_unitario": 8.0, "activo": 1},
]

# Implementar la lógica para abrir la ventana de nuevo pedido
def abrir_ventana_pedido():
  """Implementa la lógica para abrir la venta de nuevo pedido"""
  ventana_pedido = tk.Toplevel(ventana)
  ventana_pedido.title("Café el economista")
  ventana_pedido.geometry("400x350")

  tk.Label(ventana_pedido, text="Nuevo Pedido", font=("Arial", 14)).pack(pady=20)

  # Botones del menú de pedido
  tk.Button(ventana_pedido, text="Bebidas", width=25, command=mostrar_bebidas).pack(pady=5)
  tk.Button(ventana_pedido, text="Bakery", width=25, command=mostrar_bakery).pack(pady=5)
  tk.Button(ventana_pedido, text="Ver pedido",width=25, command=ver_pedido).pack(pady=10)
  tk.Button(ventana_pedido, text="Pagar pedido", width=25, command=pagar_pedido).pack(pady=5)
  tk.Button(ventana_pedido, text="Cancelar pedido", width=25, command=cancelar_pedido).pack(pady=20)

def mostrar_bebidas():
    ventana_bebidas = tk.Toplevel()
    ventana_bebidas.title("Café el economista")
    #ventana_bebidas.geometry("1000x400")  # Ancho suficiente para 4 columnas

    # Título centrado
    tk.Label(ventana_bebidas, text="Bebidas disponibles", font=("Arial", 14)).grid(row=0, column=0, columnspan=4, pady=10)

    # Filtrar bebidas activas
    bebidas_activas = []
    for bebida in BEBIDAS:
        if bebida["activo"] == 1:
            bebidas_activas.append(bebida)

    # Si no hay bebidas activas
    if not bebidas_activas:
        tk.Label(ventana_bebidas, text="No hay bebidas disponibles").grid(row=1, column=0, columnspan=4, pady=10)
        return

    # Mostrar botones en 4 columnas
    fila = 1
    columna = 0

    for bebida in bebidas_activas:
        texto = f"{bebida['nombre']} - Q{round(bebida['precios_base'], 2)}"
        boton = tk.Button(
            ventana_bebidas,
            text=texto,
            width=18,
            command=lambda b=bebida: ventana_bebida_con_modificadores(b)
        )
        boton.grid(row=fila, column=columna, padx=5, pady=5)

        columna += 1
        if columna == 4:
            columna = 0
            fila += 1

def ventana_bebida_con_modificadores(bebida):
   pass
  

#def mostrar_bakery():
  #pass

def ver_pedido():
  pass
def pagar_pedido():
  pass
def cancelar_pedido():
  pass



def mostrar_reporte_dia():
  pass
def cerrar_venta():
  pass
def salir():
  ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Café el economista")  # Título de la ventana (barra superior)
ventana.geometry("400x300")  # Tamaño de la ventana

# Título centrado dentro de la ventana
titulo = tk.Label(ventana, text="Café el economista - Menú principal", font=("Arial", 16))
titulo.pack(pady=30)  # Espaciado vertical 30px

# Botones del menú
btn_nuevo = tk.Button(ventana, text="Nuevo pedido", width=20, command=abrir_ventana_pedido)
btn_nuevo.pack(pady=5) # Espaciado vertical 5px 

btn_cierre = tk.Button(ventana, text="Cerrar venta", width=20, command=cerrar_venta)
btn_cierre.pack(pady=5)

btn_reporte = tk.Button(ventana, text="Reporte del día", width=20, command=mostrar_reporte_dia)
btn_reporte.pack(pady=5)

btn_salir = tk.Button(ventana, text="Salir", width=20, command=salir)
btn_salir.pack(pady=20) # Espaciado vertical 20px


if __name__ == "__main__":
  ventana.mainloop()
