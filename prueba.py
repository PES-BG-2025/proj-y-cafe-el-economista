import tkinter as tk
from tkinter import messagebox

#Creación de ventana del menú principal
# Crear ventana principal
ventana = tk.Tk()
ventana.title("Café el economista") # Título de la ventana (barra superior)
ventana.geometry("400x300") # Tamaño de la ventana

# Título centrado dentro de la ventana
titulo = tk.Label(ventana, text="Café el economista - Menú principal", font=("Arial", 16))
titulo.pack(pady=30) # Espaciado vertical


# Ejecutar la ventana
ventana.mainloop()
messagebox.showinfo("Nuevo pedido", "Aquí irá la lógica para iniciar un nuevo pedido.")