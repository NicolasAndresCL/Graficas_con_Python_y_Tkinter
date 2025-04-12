import tkinter

ventana =tkinter.Tk()
ventana.title("Ejemplo de tkinter5")
ventana.geometry("200x400")


tarea1 = tkinter.Checkbutton(ventana, text="Estudiar Python", font=("Arial", 14))
tarea1.pack(padx=20, pady=10)
tarea2 = tkinter.Checkbutton(ventana, text="Estudiar Tkinter", font=("Arial", 14))
tarea2.pack(padx=20, pady=10)
tarea3 = tkinter.Checkbutton(ventana, text="Estudiar Pandas", font=("Arial", 14))
tarea3.pack(padx=20, pady=10)
tarea4 = tkinter.Checkbutton(ventana, text="Estudiar SumPy", font=("Arial", 14))
tarea4.pack(padx=20, pady=10)
tarea5 = tkinter.Checkbutton(ventana, text="Estudiar Figma", font=("Arial", 14))
tarea5.pack(padx=20, pady=10)
tarea6 = tkinter.Checkbutton(ventana, text="Estudiar Power BI", font=("Arial", 14))
tarea6.pack(padx=20, pady=10)
tarea7 = tkinter.Checkbutton(ventana, text="Estudiar Unity", font=("Arial", 14))
tarea7.pack(padx=20, pady=10)

ventana.mainloop()