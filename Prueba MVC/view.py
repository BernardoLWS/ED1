import tkinter as tk

class Vista:
    def __init__(self, controlador):
        #   configuracion de la ventana
        self.ventana = tk.Tk()
        self.ventana.geometry("600x400")
        self.ventana.title("MVC Demo")

        #   configuracion de entrada y boton
        self.entry = tk.Entry(self.ventana)
        self.entry.pack()

        #   configuracion de boton con comando para guardar usuario
        self.boton = tk.Button(self.ventana, text="Guardar", command=lambda: controlador.guardar_usuario(self.entry.get()))
        self.boton.pack()
        self.label = tk.Label(self.ventana, text="")
        self.label.pack()

        #   posicionamiento de los elementos en la ventana
        self.entry.place(x=200, y=50)
        self.boton.place(x=235, y=100)

    #   metodo para mostrar mensaje en la etiqueta
    def mostrar_mensaje(self, mensaje):
        self.label.config(text=mensaje)

    #   metodo para iniciar la ventana
    def iniciar(self):
        self.ventana.mainloop()