import tkinter as tk 

class ventana:
    def __init__(self, controlador):
        #--- Configuracion de la ventana ---
        self.root = tk.Tk()
        self.control = controlador
        self.root.title("Lista Dinamica")
        self.root.geometry("900x600")

        self.ventana = tk.Frame(self.root, bg="lightblue", padx=5, pady=5)
        self.ventana.pack(fill="both", expand=True)

        #--- Posiciones ---
        self.pos1 = tk.Frame(self.ventana, bg="white")
        self.pos1.pack(pady=10)
        
        self.pos2 = tk.Frame(self.ventana, bg="white")
        self.pos2.pack(anchor="w",pady=10) 

        self.pos3 = tk.Frame(self.ventana, bg="white")
        self.pos3.pack(anchor="w", pady=10) 

        self.pos4 = tk.Frame(self.ventana, bg="white")
        self.pos4.pack(anchor="w", pady=10) 

        self.pos5 = tk.Frame(self.ventana, bg="white")
        self.pos5.pack(anchor="w", pady=10) 

        #--- Titulo --
        self.titulo = tk.Label(self.pos1, text=" LISTA DINAMICA ", font=("Arial", 18, "bold"), bg="white", fg="black")
        self.titulo.pack(pady=10)

        #-- Label --
        self.Label = tk.Label(self.pos2, text=" Ingrese : ", font=("Arial", 12), bg="white", fg="black")
        self.Label.pack(side="left", padx=40,pady=10)

        self.Label = tk.Label(self.pos5, text=" Tamaño : ", font=("Arial", 12), bg="white", fg="black")
        self.Label.pack(side="left",padx=40,pady=10)

        self.Contador = tk.Label(self.pos5, text=" 0 ", font=("Arial", 12), bg="white", fg="black")
        self.Contador.pack(side="left",pady=10)
        
        #--- Button ---
        self.Button = tk.Button(self.pos2, command=self.Limpiar,text="Limpiar",width=10)
        self.Button.pack(side="right",padx=100, pady=5)

        self.Button = tk.Button(self.pos3,command=self.InsertarFinal, text="Insertar", width=10)
        self.Button.pack(side="left",padx=40, pady=10)

        self.Button = tk.Button(self.pos3,command=self.InsertarInicio, text="Insertar Inicio", width=10)
        self.Button.pack(side="left",pady=10)

        self.Button = tk.Button(self.pos3,command=self.Buscar, text="Buscar", width=10)
        self.Button.pack(side="left",padx=40,pady=10)

        self.Button = tk.Button(self.pos3,command=self.Eliminar, text="Eliminar", width=10)
        self.Button.pack(side="left",pady=10)


        #--- Edit ---
        self.Entrada = tk.Entry(self.pos2,bg="white",fg="black",width=50)
        self.Entrada.pack(pady=10)

        #--- tabla resultado ---
        self.Resultado = tk.Listbox(self.pos4,bg="white",fg="black",width=100)
        self.Resultado.pack(padx=40, pady=10)

    def Limpiar(self):
        self.control.Limpiar()

    def InsertarFinal(self):
        self.control.InsertarFinal() 
        self.Entrada.delete(0,tk.END)
   
    def InsertarInicio(self):
        self.control.InsertarInicio()
        self.Entrada.delete(0, tk.END)

    def Buscar(self):
        self.control.Buscar()
        self.Entrada.delete(0,tk.END)

    def Eliminar(self):
        self.control.Eliminar()
        self.Entrada.delete(0, tk.END)

    def Iniciar(self):
        self.root.mainloop()

"""import tkinter as tk

class ventana:
    def __init__(self, controlador):
        #--- Configuración de la ventana ---
        self.root = tk.Tk()
        self.control = controlador
        self.root.title("LISTA DINÁMICA")
        self.root.geometry("900x600")

        self.ventana = tk.Frame(self.root, bg="#cce7ff", padx=5, pady=5)
        self.ventana.pack(fill="both", expand=True)

        #--- Secciones ---
        self.pos1 = tk.Frame(self.ventana, bg="white")
        self.pos1.pack(pady=10)

        self.pos2 = tk.Frame(self.ventana, bg="white")
        self.pos2.pack(anchor="w", pady=10)

        self.pos3 = tk.Frame(self.ventana, bg="white")
        self.pos3.pack(anchor="w", pady=10)

        self.pos4 = tk.Frame(self.ventana, bg="white")
        self.pos4.pack(anchor="w", pady=10)

        self.pos5 = tk.Frame(self.ventana, bg="white")
        self.pos5.pack(anchor="w", pady=10)

        #--- Título ---
        self.titulo = tk.Label(self.pos1, text="LISTA DINÁMICA", font=("Arial", 18, "bold"), bg="white", fg="black")
        self.titulo.pack(pady=10)

        #--- Entrada ---
        tk.Label(self.pos2, text="Ingrese:", font=("Arial", 12), bg="white", fg="black").pack(side="left", padx=40, pady=10)
        self.Entrada = tk.Entry(self.pos2, bg="white", fg="black", width=50)
        self.Entrada.pack(pady=10)

        #--- Botones ---
        botones = [
            ("Insertar", "#4CAF50", self.InsertarFinal),
            ("Insertar Inicio", "#2196F3", self.InsertarInicio),
            ("Buscar", "#FF9800", self.Buscar),
            ("Eliminar", "#F44336", self.Eliminar),
            ("Limpiar", "#FFC107", self.Limpiar)
        ]
        for texto, color, comando in botones:
            tk.Button(self.pos3, text=texto, bg=color, fg="white", width=12, command=comando).pack(side="left", padx=10, pady=10)

        #--- Tamaño ---
        tk.Label(self.pos5, text="Tamaño:", font=("Arial", 12), bg="white", fg="black").pack(side="left", padx=40, pady=10)
        self.Contador = tk.Label(self.pos5, text="0", font=("Arial", 12), bg="white", fg="black")
        self.Contador.pack(side="left", pady=10)

        #--- Canvas para nodos ---
        self.canvas = tk.Canvas(self.pos4, bg="white", width=800, height=250)
        self.canvas.pack(padx=40, pady=10)

    #--- Métodos de control ---
    def Limpiar(self):
        self.control.Limpiar()
        self.canvas.delete("all")
        self.Contador.config(text="0")

    def InsertarFinal(self):
        self.control.InsertarFinal()
        self.Entrada.delete(0, tk.END)

    def InsertarInicio(self):
        self.control.InsertarInicio()
        self.Entrada.delete(0, tk.END)

    def Buscar(self):
        self.control.Buscar()
        self.Entrada.delete(0, tk.END)

    def Eliminar(self):
        self.control.Eliminar()
        self.Entrada.delete(0, tk.END)

    def DibujarLista(self, lista):
       
        self.canvas.delete("all")
        x, y = 80, 120
        colores = ["#5DADE2", "#58D68D", "#F5B041", "#AF7AC5"]

        for i, elemento in enumerate(lista):
            color = colores[i % len(colores)]
            self.canvas.create_rectangle(x, y-25, x+70, y+25, fill=color, outline="black")
            self.canvas.create_text(x+35, y, text=str(elemento), font=("Arial", 12, "bold"))
            if i < len(lista) - 1:
                self.canvas.create_line(x+70, y, x+110, y, arrow=tk.LAST, width=2)
            x += 110

        # Nodo final NULL
        self.canvas.create_rectangle(x, y-25, x+70, y+25, fill="#D5D8DC", outline="black")
        self.canvas.create_text(x+35, y, text="NULL", font=("Arial", 12, "bold"))

    def Iniciar(self):
        self.root.mainloop()"""