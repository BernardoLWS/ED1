import tkinter as tk

class ventana:
    def __init__(self, view):
        #--- Configuración de la ventana ---
        self.view = view
        self.view.title("POLINOMIO")
        self.view.geometry("900x400")

        self.frame = tk.Frame(view, bg="white", padx=5, pady=5)
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.frame_izq = tk.Frame(self.frame, bg="lightblue", padx=10, pady=10)
        self.frame_izq.pack(side="left", expand=True, fill="both")

        #self.frame_der = tk.Frame(self.frame, bg="lightgreen", padx=10, pady=10)
        #self.frame_der.pack(side="right", expand=True, fill="both")     
        #----------------------------------- POLINOMIO(X) ------------------------
        #--- Label Titulo ---
        self.Label_polX = tk.Label(
            self.frame_izq, 
            text="POLINOMIO : ",
            background="lightblue",
            font=("Arial", 18,"bold"),
            foreground="black"
        )
        self.Label_polX.pack(side="top", pady=5)

        # --------------------------------------  Exponente ------------------------------------------------
        fila_exp = tk.Frame(self.frame_izq, bg="lightblue")
        fila_exp.pack(anchor="w", padx=80, pady=5)

        #--- Label Exponente ---
        self.Label_exp = tk.Label(fila_exp,
            text="Exponente  -> ",
            background="lightblue",
            font=("Arial", 12),
            foreground="black"
        )
        self.Label_exp.pack(side="left", padx=5)

        #--- Edit Exponente ---
        self.entry_exp = tk.Entry(fila_exp,
            width=3,
            background="white",
            font=("Arial", 12),
            foreground="black"
        )
        self.entry_exp.pack(side="left", padx=5)

        #-------------------------------- Coeficiente --------------------------------------
        fila_coef = tk.Frame(self.frame_izq, bg="lightblue")
        fila_coef.pack(anchor="w")

        #--- Label Coeficiente ---
        self.Label_coef = tk.Label(fila_coef,
            text="Coeficiente  -> ",
            background="lightblue",
            font=("Arial", 12),
            foreground="black"
        )
        self.Label_coef.pack(side="left", padx=5)

        #--- Edit Coeficiente ---
        self.Entry_coef = tk.Entry(fila_coef,
            width=3,
            background="white",
            font=("Arial", 12),
            foreground="black"
        )
        self.Entry_coef.pack(side="left", padx=10)

        #---boton opciones (x,y,z)---
        opcion = tk.StringVar(value="x")
        menu = tk.OptionMenu(fila_coef, opcion, "x", "y", "z")
        menu.config(width=1, font=("Arial", 24,"bold"), background="white", foreground="black")
        menu.pack(side="left", pady=5)
                
        #--- Label mostrar polinomio ---
        self.Label_mostrarPoly = tk.Label(fila_exp,
            text="El polinomio es : ",
            background="lightblue",
            font=("Arial", 12),
            foreground="black"
        )
        self.Label_mostrarPoly.pack(anchor="w",padx=90, pady=5)

        #--- mostrar resultado ---
        self.Label_resultadoX = tk.Label(fila_coef,
            text="Resultado : ",
            background="lightblue",
            font=("Arial", 12),
            foreground="black"
        )
        self.Label_resultadoX.pack(anchor="e", padx=105, pady=5)
        #-------------------------------------------Botones-----------------------------------------------
        fila_boton = tk.Frame(self.frame_izq, bg="lightblue")
        fila_boton.pack(anchor="w", padx=5, pady=5)

        #-- Boton Agregar ---
        self.boton_agregar = tk.Button(fila_boton,
            text="Agregar",
            font=("Arial", 12),
            width=10
        )
        self.boton_agregar.pack(side="left", padx=30, pady=30)

        #--- Boton Calcular ---
        self.boton_evaluar = tk.Button(fila_boton,
            text="Calcular",
            font=("Arial", 12),
            width=10
        )
        self.boton_evaluar.pack(side="left", padx=30, pady=30)

        #--- Boton Limpiar ---
        self.boton_Limpiar = tk.Button(fila_boton,
            text = "Limpiar",
            font= ("Arial",12),
            width=10
        )
        self.boton_Limpiar.pack(side="left", padx=30, pady=30)

# Ejecutar ventana
root = tk.Tk()
app = ventana(root)
root.mainloop()


