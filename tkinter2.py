import tkinter

ventana =tkinter.Tk()
ventana.title("Ejemplo de tkinter2")

hola_nombre = tkinter.Label(ventana, text="Hola Nombre",font=("Arial", 20, "bold"), padx=20, pady=40)
hola_nombre.pack()

nombre = tkinter.Entry(ventana, font=("Arial", 16, "bold"))
nombre.pack(padx=20, pady=20)

boton_cambio = tkinter.Button(ventana, text="Cambiar", font=("Arial", 16, "bold"), command=lambda: hola_nombre.config(text=f"Hola {nombre.get()}"))
boton_cambio.pack(padx=20, pady=20)

ventana.mainloop()