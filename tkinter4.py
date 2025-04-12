import tkinter

ventana =tkinter.Tk()
ventana.title("Ejemplo de tkinter4")
ventana.geometry("200x300")
def a_binario():
    text = texto.get( 1.0, tkinter.END) # Obtener el texto del widget de texto
    binario = ''
    for letra in text:
        binario += bin(ord(letra))[2:]  
        
    texto.delete(1.0, tkinter.END) 
    texto.insert(tkinter.END, binario) 

     
label_texto = tkinter.Label(ventana, text="Texto").pack()
texto = tkinter.Text(ventana, height=10, width=30)
texto.pack(padx=20, pady=20)
boton_cambio = tkinter.Button(ventana, text="A Binario", font=("Arial", 16, "bold"), command=a_binario).pack(padx=20, pady=20)

ventana.mainloop()