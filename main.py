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

def abrir_ventana_pedido():
  pass  # Implementar la lógica para abrir la ventana de nuevo pedido
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
