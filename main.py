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


import tkinter as tk
from tkinter import messagebox
import datetime
import data_io #para traer las funciones que están en data_io

# ======== Datos de prueba, luego se cambia a leer desde CSV
# BEBIDAS = [
#   {"id_bebida": "LATTE-12", "nombre": "Latte 12oz", "precios_base": 22.0, "categoría": "espresso", "activo": 1},
#   {"id_bebida": "ESP-DBL", "nombre": "Espresso doble", "precios_base": 15.0, "categoría": "espresso", "activo": 1},
#   {"id_bebida": "CAP-12", "nombre": "Cappuccino 12oz", "precios_base": 22.0, "categoría": "espresso", "activo": 1},
# ]

# MODIFICADORES = [
#   {"id_modificador": "LECHE-ENT", "nombre": "Leche entera", "tipo": "leche", "ajuste_precio": 0.0,"activo": 1},
#   {"id_modificador": "LECHE-COCO", "nombre": "Leche de coco", "tipo": "leche", "ajuste_precio": 3.0, "activo": 1},
#   {"id_modificador": "SHOT-DBL", "nombre": "Doble shot", "tipo": "shot", "ajuste_precio": 3.0, "activo": 1},
#   {"id_modificador": "JAR-CAR", "nombre": "Jarabe caramelo", "tipo": "jarabe", "ajuste_precio": 2.0,"activo": 1},
# ]

# BAKERY = [
#   {"id_producto": "PROD-001", "nombre": "Pastelito 1", "categoría": "pastel azul", "existencias": 48, "precio_unitario": 6.0, "activo": 1},
#   {"id_producto": "PROD-001", "nombre": "Pastelito 2", "categoría": "pastel rojo", "existencias": 12, "precio_unitario": 8.0, "activo": 1},
# ]
# ======== Fin de datos de prueba

pedido_actual = {
    "fecha_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "lineas": [],
    "total": 0.0}
id_linea_actual = 0

BEBIDAS = data_io.leer_bebidas()
BAKERY = data_io.leer_bakery()
MODIFICADORES = data_io.leer_modificadores()

# Implementar la lógica para abrir la ventana de nuevo pedido
def abrir_ventana_pedido():
    """Implementa la lógica para abrir la venta de nuevo pedido"""
    ventana_pedido = tk.Toplevel(ventana)
    ventana_pedido.title("Café el economista")
    ventana_pedido.geometry("400x350")

    tk.Label(ventana_pedido, text="Nuevo Pedido", font=("Arial", 14)).pack(pady=20)
    def cancelar_pedido():
        confirmar = messagebox.askyesno("Cancelar pedido", "¿Realmente desea cancelar el pedido?")
        if confirmar:
            pedido_actual["lineas"].clear()
            pedido_actual["total"] = 0.0
            pedido_actual["fecha_hora"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            global id_linea_actual
            id_linea_actual = 0
            messagebox.showinfo("Pedido cancelado", "El pedido fue cancelado correctamente.")
            ventana_pedido.destroy()

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
    ventana_mods = tk.Toplevel()
    ventana_mods.title("Café el economista")

    precio_base = round(bebida["precios_base"], 2)
    subtotal_var = tk.DoubleVar(value=precio_base)

    tk.Label(ventana_mods, text=bebida["nombre"], font=("Arial", 14)).pack(pady=10)
    tk.Label(ventana_mods, text=f"Precio base: Q{precio_base:.2f}", font=("Arial", 12)).pack()

    tk.Label(ventana_mods, text="Modificadores disponibles:", font=("Arial", 12)).pack(pady=10)

    modificadores_activados = []
    modificadores_vars = []

    for mod in MODIFICADORES:
        if mod["activo"] == 1:
            var = tk.IntVar()
            chk = tk.Checkbutton(
                ventana_mods,
                text=f"{mod['nombre']} (+Q{mod['ajuste_precio']:.2f})",
                variable=var,
                command=lambda: actualizar_subtotal()
            )
            chk.pack(anchor="w", padx=20)
            modificadores_activados.append(mod)
            modificadores_vars.append(var)

    subtotal_label = tk.Label(ventana_mods, text=f"Subtotal: Q{subtotal_var.get():.2f}", font=("Arial", 12))
    subtotal_label.pack(pady=10)

    def actualizar_subtotal():
        total = precio_base
        for i in range(len(modificadores_activados)):
            if modificadores_vars[i].get() == 1:
                total += modificadores_activados[i]["ajuste_precio"]
        subtotal_var.set(round(total, 2))
        subtotal_label.config(text=f"Subtotal: Q{subtotal_var.get():.2f}")

    def agregar_bebida():
        seleccionados = []
        for i in range(len(modificadores_activados)):
            if modificadores_vars[i].get() == 1:
                seleccionados.append(modificadores_activados[i])

        global id_linea_actual
        id_linea_actual += 1

        total_modificadores = sum(mod["ajuste_precio"] for mod in seleccionados)
        total_linea = precio_base + round(total_modificadores, 2)

        nueva_linea = {
            "id_linea": id_linea_actual,
            "tipo": "bebida",
            "id_item": bebida["id_bebida"],
            "nombre": bebida["nombre"],
            "cantidad": 1,
            "precio_unitario": precio_base,
            "modificadores": seleccionados,
            "total_linea": total_linea
        }

        pedido_actual["lineas"].append(nueva_linea)
        pedido_actual["total"] += total_linea

        messagebox.showinfo("Pedido agregado", f"{bebida['nombre']} fue agregada correctamente.\nTotal: Q{total_linea:.2f}")
        ventana_mods.destroy()

    tk.Button(ventana_mods, text="Agregar bebida", command=agregar_bebida).pack(pady=10)
  
  

#def mostrar_bakery():
  #pass

def ver_pedido():
    ventana_pedido = tk.Toplevel()
    ventana_pedido.title("Resumen del pedido")

    tk.Label(ventana_pedido, text="Pedido actual", font=("Arial", 14)).pack(pady=10)

    if not pedido_actual["lineas"]:
        tk.Label(ventana_pedido, text="No hay productos en el pedido.", font=("Arial", 12)).pack(pady=10)
        return

    for linea in pedido_actual["lineas"]:
        texto = f"{linea['nombre']} - Q{linea['precio_unitario']:.2f}"
        if linea["modificadores"]:
            for mod in linea["modificadores"]:
                texto += f"\n    + {mod['nombre']} (+Q{mod['ajuste_precio']:.2f})"
        texto += f"\n  Subtotal: Q{linea['total_linea']:.2f}\n"
        tk.Label(ventana_pedido, text=texto, justify="left", anchor="w", font=("Arial", 11)).pack(padx=20, pady=5, fill="x")

    tk.Label(ventana_pedido, text=f"Total del pedido: Q{pedido_actual['total']:.2f}", font=("Arial", 12, "bold")).pack(pady=10)


def pagar_pedido():
    if not pedido_actual["lineas"]:
        messagebox.showwarning("Sin productos", "No hay productos en el pedido.")
        return

    ventana_pago = tk.Toplevel()
    ventana_pago.title("Pagar pedido")

    tk.Label(ventana_pago, text="Resumen del pedido", font=("Arial", 14)).pack(pady=10)

    # Mostrar cada línea del pedido
    for linea in pedido_actual["lineas"]:
        texto = f"{linea['nombre']} - Q{linea['precio_unitario']:.2f}"
        if linea["modificadores"]:
            for mod in linea["modificadores"]:
                texto += f"\n    + {mod['nombre']} (+Q{mod['ajuste_precio']:.2f})"
        texto += f"\n  Subtotal: Q{linea['total_linea']:.2f}\n"
        tk.Label(ventana_pago, text=texto, justify="left", anchor="w", font=("Arial", 11)).pack(padx=20, pady=5, fill="x")

    # Total general
    tk.Label(ventana_pago, text=f"Total a pagar: Q{pedido_actual['total']:.2f}", font=("Arial", 12, "bold")).pack(pady=10)

		# Función que genera la información del pago y la almacena con funciones que vienen de data_io
    def confirmar_pago():
        id_pedido = f"PV-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"

        pago_info = {
            "metodo": "tarjeta",
            "monto": pedido_actual["total"],
            "cambio": 0.0
        }
        
        data_io.guardar_pedido(pedido_actual, pago_info, id_pedido)
        data_io.guardar_lineas(pedido_actual, id_pedido)
        data_io.guardar_modificadores(pedido_actual, id_pedido)

        # Actualizar existencias de bakery
        for linea in pedido_actual["lineas"]:
            if linea["tipo"] == "bakery":
                for producto in BAKERY:
                    if producto["id_producto"] == linea["id_item"]:
                        producto["existencias"] -= 1
                        break

        data_io.actualizar_bakery(BAKERY)

        messagebox.showinfo("Pago exitoso", f"Pedido pagado correctamente.\nMétodo: Tarjeta")

        pedido_actual["lineas"].clear()
        pedido_actual["total"] = 0.0
        pedido_actual["fecha_hora"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ventana_pago.destroy()

    def cancelar_pago():
        messagebox.showinfo("Pedido en curso", "Continúa agregando a tu pedido.")
        ventana_pago.destroy()

    tk.Button(ventana_pago, text="Confirmar pago", command=confirmar_pago).pack(pady=10)
    tk.Button(ventana_pago, text="Cancelar", command=cancelar_pago).pack(pady=5)

def mostrar_reporte_dia():
    # Asigna a resumen y total, los dos valores que devuelve la función en main, indicando que recibe bebidas y bakery
    resumen, total_dia = data_io.generar_reporte_resumido_dia(BEBIDAS, BAKERY)

    ventana_reporte = tk.Toplevel()
    ventana_reporte.title("Resumen de ventas del día")

    tk.Label(ventana_reporte, text="Resumen por producto", font=("Arial", 14)).pack(pady=10)

    # nombre y datos como indice en el diccionario resumen para optener cantidad y total
    for nombre, datos in resumen.items():
        texto = f"{nombre} - {datos['cantidad']} vendidos - Q{datos['total']:.2f}"
        tk.Label(ventana_reporte, text=texto, justify="left", font=("Arial", 11)).pack(padx=20)

    tk.Label(ventana_reporte, text=f"\nTotal del día: Q{total_dia:.2f}", font=("Arial", 12, "bold")).pack(pady=10)


def cerrar_venta():
    confirmar = messagebox.askyesno("Confirmar", "¿Desea cerrar la venta del día?")
    if confirmar:
        data_io.generar_cierre_diario()
        messagebox.showinfo("Cierre", "Cierre del día generado correctamente.")


def salir():
  ventana.quit()


def mostrar_bakery():
    ventana_bakery = tk.Toplevel()
    ventana_bakery.title("Café el economista")

    tk.Label(ventana_bakery, text="Productos de Bakery", font=("Arial", 14)).grid(row=0, column=0, columnspan=4, pady=10)

    productos_activos = [p for p in BAKERY if p["activo"] == 1]

    if not productos_activos:
        tk.Label(ventana_bakery, text="No hay productos disponibles").grid(row=1, column=0, columnspan=4, pady=10)
        return

    def agregar_producto_bakery(producto, ventana_bakery):
        global id_linea_actual
        id_linea_actual += 1

        nueva_linea = {
            "id_linea": id_linea_actual,
            "tipo": "bakery",
            "id_item": producto["id_producto"],
            "nombre": producto["nombre"],
            "cantidad": 1,
            "precio_unitario": producto["precio_unitario"],
            "modificadores": [],
            "total_linea": producto["precio_unitario"]
        }

        pedido_actual["lineas"].append(nueva_linea)
        pedido_actual["total"] += producto["precio_unitario"]

        messagebox.showinfo("Producto agregado", f"{producto['nombre']} fue agregado correctamente.\nTotal: Q{producto['precio_unitario']:.2f}")
        ventana_bakery.destroy()
    
    fila = 1
    columna = 0

    for producto in productos_activos:
        texto = f"{producto['nombre']} - Q{round(producto['precio_unitario'], 2)}"
        boton = tk.Button(
            ventana_bakery,
            text=texto,
            width=18,
            command=lambda p=producto: agregar_producto_bakery(p, ventana_bakery)
        )
        boton.grid(row=fila, column=columna, padx=5, pady=5)

        columna += 1
        if columna == 4:
            columna = 0
            fila += 1

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
