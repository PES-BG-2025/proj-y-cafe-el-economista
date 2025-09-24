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

#Función inicial
def main():
    while True:
        print("MENU PRINCIPAL")
        print("1. Nuevo pedido")
        print("2. Reportes")
        print("3. Catálogo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("Ir a nuevo pedido")
        elif opcion == "2":
            print("Ir a reportes")
        elif opcion == "3":
            print("Ir a catálogo")
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción incorrecta. Por favor, intente de nuevo.")
            continue

if __name__ == "__main__":
  main()