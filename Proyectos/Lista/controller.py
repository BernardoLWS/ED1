import tkinter as tk
from tkinter import messagebox

class controlador:
    def __init__(self, view, model):
        self.vista = view
        self.modelo = model

    def Actualizar(self, lista):
        self.vista.Resultado.delete(0, tk.END)
        for dato in lista:
            self.vista.Resultado.insert(tk.END, dato)
        tamaño = len(lista)    
        self.vista.Contador.config(text=(tamaño))

    def Verificacion(self, dato):
        permitidos = (  "abcdefghijkmnlñopqrstuvwxyz"
                        "ABCDEFGHIJKMNLÑOPQRSTUVWXYZ"
                        "áéíóúÁÉÍÓÚ"
                        "àèìòùÀÈÌÒÙ"
                        "äëïöüÄËÏÖÜ"
                        "âêîôûÂÊÎÔÛ"
                        "0123456789"
                        " "
                     )
        for caracter in dato:
            if caracter not in permitidos:
                return False
        return True


    def InsertarFinal(self):
        dato = self.vista.Entrada.get()
        if self.Verificacion(dato):
            if dato:
                self.modelo.Insertar_Final(dato)
                lista = self.modelo.mostrar()
                self.Actualizar(lista)

    def InsertarInicio(self):
        dato = self.vista.Entrada.get()
        if dato:
            self.modelo.Insertar_Inicio(dato)
            lista = self.modelo.mostrar()
            self.Actualizar(lista)
        
    def Buscar(self):
        dato = self.vista.Entrada.get()
        pos = self.modelo.Buscar(dato)
        if pos != -1:
            messagebox.showinfo("Éxito", f" Encontrado en la posición: {pos}")
        else:
            messagebox.showerror("Error",f" No encontrado")   

    def Eliminar(self):
        dato = self.vista.Entrada.get()
        self.modelo.Eliminar(dato)
        lista = self.modelo.mostrar()
        self.Actualizar(lista)

    def Limpiar(self):
        self.vista.Entrada.delete(0, tk.END)
        self.vista.Resultado.delete(0, tk.END)
        self.vista.Contador.config(text="0")
        self.modelo.vaciar()
   

 