import tkinter as tk

class AgendaView:
    """Construye la ventana principal de la agenda."""
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("900x600")
        self.ventana.title("--- AGENDA DE CONTACTOS ---")
        self.ventana.configure(bg="#ABB7C2")

        # Botones
        self.boton_agregar = tk.Button(self.ventana, text="Agregar", bg="#207dd3", fg="#ffffff")
        self.boton_eliminar = tk.Button(self.ventana, text="Eliminar", bg="#207dd3", fg="#ffffff")
        self.boton_buscar = tk.Button(self.ventana, text="Buscar", bg="#207dd3", fg="#ffffff")
        self.boton_guardar = tk.Button(
        self.ventana, text="Guardar", bg="#207dd3", fg="#ffffff")
        
        self.boton_cargar = tk.Button(
        self.ventana, text="Cargar", bg="#207dd3", fg="#ffffff")


        # Posicionamiento
      
        # Cajas de texto
        self.caja_buscar = tk.Entry(self.ventana, font=("Arial", 12), fg="#000000", bg="#F8FBFD")
        self.caja_nombre = tk.Entry(self.ventana, font=("Arial", 12), fg="#000000", bg="#F8FBFD")
        self.caja_telefono = tk.Entry(self.ventana, font=("Arial", 12), fg="#000000", bg="#F8FBFD")
        self.caja_gmail = tk.Entry(self.ventana, font=("Arial", 12), fg="#000000", bg="#F8FBFD")

        # Listbox para contactos
        self.caja_resultado = tk.Listbox(
            self.ventana, font=("Arial", 12),
            fg="#000000", bg="white",
            selectmode=tk.SINGLE
        )

        # Textos descriptivos
        self.caja_mensajes = tk.Label(self.ventana, text="", font=("Arial", 12), fg="#B10000",bg="#ABB7C2")
        self.texto_nombre = tk.Label(self.ventana, text="Nombre :", font=("Arial", 12), fg="black", bg="#ABB7C2")
        self.texto_telefono = tk.Label(self.ventana, text="Teléfono :", font=("Arial", 12), fg="black", bg="#ABB7C2")
        self.texto_gmail = tk.Label(self.ventana, text="Correo :", font=("Arial", 12), fg="black", bg="#ABB7C2")
        self.texto_tbuscar = tk.Label(self.ventana, text="Buscar Contacto :", font=("Arial", 12), fg="black", bg="#ABB7C2")
        self.texto_tagregar = tk.Label(self.ventana, text="Agregar Contacto :", font=("Arial", 12), fg="black", bg="#ABB7C2")
        self.texto_lista = tk.Label(self.ventana, text="Lista de Contactos :", font=("Arial", 12), fg="black", bg="#ABB7C2")

        # Posicionamiento
        self.caja_mensajes.place(relx=0.05, rely=0.95)
        self.caja_resultado.place(relx=0.05, rely=0.10, relwidth=0.40, relheight=0.65)
        self.texto_tbuscar.place(relx=0.50, rely=0.05)
        self.caja_buscar.place(relx=0.50, rely=0.10, relwidth=0.30, relheight=0.07)
        self.boton_buscar.place(relx=0.85, rely=0.10, relwidth=0.08, relheight=0.07)
        self.texto_tagregar.place(relx=0.50, rely=0.22)
        self.texto_nombre.place(relx=0.50, rely=0.32)
        self.caja_nombre.place(relx=0.60, rely=0.30, relwidth=0.33, relheight=0.07)
        self.texto_telefono.place(relx=0.50, rely=0.42)
        self.caja_telefono.place(relx=0.60, rely=0.40, relwidth=0.33, relheight=0.07)
        self.texto_gmail.place(relx=0.50, rely=0.52)
        self.caja_gmail.place(relx=0.60, rely=0.50, relwidth=0.33, relheight=0.07)
        self.boton_agregar.place(relx=0.70, rely=0.62, relwidth=0.10, relheight=0.07)
        self.boton_eliminar.place(relx=0.20, rely=0.80, relwidth=0.09, relheight=0.07)
        self.boton_guardar.place(relx=0.10, rely=0.80, relwidth=0.09, relheight=0.07)
        self.boton_cargar.place(relx=0.30, rely=0.80, relwidth=0.09, relheight=0.07)

    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje en el Label de mensajes."""
        self.caja_mensajes.config(text=mensaje)

    def mostrar_resultados(self, contactos):
        """Muestra resultados o lista de contactos en el Listbox."""
        self.caja_resultado.delete(0, tk.END)
        for contacto in contactos:
            self.caja_resultado.insert(tk.END, str(contacto))

    def obtener_seleccionado(self):
        """Devuelve el índice del contacto seleccionado en el Listbox."""
        seleccion = self.caja_resultado.curselection()
        if seleccion:
            return seleccion[0]
        return None

    def iniciar(self):
        """Inicializa la ventana principal."""
        self.ventana.mainloop()