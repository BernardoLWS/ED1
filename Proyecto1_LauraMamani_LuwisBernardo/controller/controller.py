class AgendaController:
    """Controlador que conecta la Vista y el Modelo."""

    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

        # Conectar botones de la vista con métodos del controlador
        self.vista.boton_agregar.config(command=self.agregar_contacto)
        self.vista.boton_eliminar.config(command=self.eliminar_contacto)
        self.vista.boton_buscar.config(command=self.buscar_contacto)
        self.vista.boton_guardar.config(command=self.guardar_contactos)
        self.vista.boton_cargar.config(command=self.cargar_contactos)

    def agregar_contacto(self):
        """Obtiene datos de la vista y los agrega al modelo."""
        nombre = self.vista.caja_nombre.get().strip()
        telefono = self.vista.caja_telefono.get().strip()
        correo = self.vista.caja_correo.get().strip()
        abecedario = ("abcdefghijklmnñopqrstuvwxyz")
        numeros = ("0123456789")
    
        nombre_valido = len(nombre)>0 and all(c in abecedario or c==" " for c in nombre.lower())
        telefono_valido = len(telefono)>0 and all(c in numeros for c in telefono)
        correo_valido = "@" in correo and ".com" in correo

        if nombre_valido and telefono_valido and correo_valido:
            self.modelo.agregar_contacto(nombre, telefono, correo)
            self.vista.mostrar_mensaje("Contacto agregado correctamente.")
            self.actualizar_lista()
            """Limpiar despues e agregar contacto"""
            self.vista.caja_nombre.delete(0,"end")
            self.vista.caja_telefono.delete(0,"end")
            self.vista.caja_correo.delete(0,"end")
        else:
            self.vista.mostrar_mensaje("Por favor, completa todos los campos correctamente.")


    def eliminar_contacto(self):
        """Elimina el contacto seleccionado en la vista."""
        indice = self.vista.obtener_seleccionado()
        if indice is not None:
            contacto = self.modelo.obtener_todos()[indice]
            if self.modelo.eliminar_contacto(contacto.nombre):
                self.vista.mostrar_mensaje("Contacto eliminado correctamente.")
                self.actualizar_lista()
            else:
                self.vista.mostrar_mensaje("Error al eliminar el contacto.")
        else:
            self.vista.mostrar_mensaje("Selecciona un contacto para eliminar.")

    def buscar_contacto(self):
        """Busca contactos que coincidan con el texto ingresado."""
        texto_buscar = self.vista.caja_buscar.get().strip()
        if texto_buscar:
            resultados = self.modelo.buscar_contacto(texto_buscar)
            if resultados:
                self.vista.mostrar_resultados(resultados)
                self.vista.mostrar_mensaje(f"{len(resultados)} contacto(s) encontrado(s).")
            else:
                self.vista.mostrar_resultados([])
                self.vista.mostrar_mensaje("No se encontraron contactos.")
                self.actualizar_lista()
           
   

    def guardar_contactos(self):
        if not self.modelo.obtener_todos():
            self.vista.mostrar_mensaje("No hay contactos para guardar.")
        else:
            self.modelo.guardar("datos/contactos.json")
            self.vista.mostrar_mensaje("Contactos guardados en datos/contactos.json")

    def cargar_contactos(self):
        self.modelo.cargar("datos/contactos.json")
        self.actualizar_lista()
        self.vista.mostrar_mensaje("Contactos cargados desde datos/contactos.json")
    
    def actualizar_lista(self):
        """Muestra todos los contactos en la vista."""
        contactos = self.modelo.obtener_todos()
        if contactos:
            self.vista.mostrar_resultados(contactos)
        else:
            self.vista.mostrar_resultados([])
            self.vista.mostrar_mensaje("Lista vacía.")