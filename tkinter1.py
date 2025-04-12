import tkinter

ventana =tkinter.Tk()
ventana.title("Ejemplo de tkinter1")


titulo = tkinter.Label(ventana, text="Poto con Caca",font=("Arial", 20, "bold"), padx=20, pady=40, bg="black", fg="green")
titulo.pack()

ventana.mainloop()