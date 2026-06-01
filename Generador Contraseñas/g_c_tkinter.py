import tkinter as tk
from tkinter import messagebox
import random
import string

def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        resultado.set(contraseña)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

def copiar_contraseña():
    ventana.clipboard_clear()
    ventana.clipboard_append(resultado.get())
    messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Generador de Contraseñas 🔐")
ventana.geometry("400x250")
ventana.configure(bg="#1e1e2f")

# Variables
resultado = tk.StringVar()

# Widgets
tk.Label(ventana, text="Longitud de la contraseña:", fg="white", bg="#1e1e2f").pack(pady=10)
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

tk.Button(ventana, text="Generar", command=generar_contraseña, bg="#007acc", fg="white").pack(pady=10)

tk.Entry(ventana, textvariable=resultado, width=30, justify="center").pack(pady=10)

tk.Button(ventana, text="Copiar", command=copiar_contraseña, bg="#00b894", fg="white").pack(pady=5)

# Ejecutar
ventana.mainloop()
