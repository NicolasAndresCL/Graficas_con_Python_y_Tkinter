import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login exitoso")
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")

# Crear ventana principal
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Etiquetas y campos de entrada
label_username = tk.Label(root, text="Usuario:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Contraseña:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Botón de login
button_login = tk.Button(root, text="Iniciar sesión", command=login)
button_login.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()

'''import tkinter as tkinter
from tkinter import messagebox # Importar el módulo messagebox para mostrar mensajes emergentes

ventana =tkinter.Tk()
# Funcion login
def login():
    nombre = nombre_var.get()
    password = password_var.get()

    if nombre == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login exitoso")
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")

# Variables
nombre_var = tkinter.StringVar()
password_var = tkinter.StringVar()

nombre_label = tkinter.Label(ventana, text="Nombre Usuario",font=("Arial", 20, "bold"), padx=20, pady=40).pack()
nombre_entry = tkinter.Entry(ventana, font=("Arial", 16, "bold"), textvariable=nombre_var).pack(padx=20, pady=20)
password_label = tkinter.Label(ventana, text="Password",font=("Arial", 20, "bold"), padx=20, pady=40).pack()
password_entry = tkinter.Entry(ventana, font=("Arial", 16, "bold"), textvariable=password_var).pack(padx=20, pady=20)
boton_ingresar = tkinter.Button(ventana, text="Ingresar", font=("Arial", 16, "bold"), command=login).pack(padx=20, pady=20)

ventana.mainloop()'''