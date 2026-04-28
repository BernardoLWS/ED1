#from datos import contactos
import json
"""Nodo que representa un contacto en la lista enlazada."""
class NodoContacto():
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.siguiente = None

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.correo}"

class AgendaModel():
    def __init__(self):
        self.cabeza = None

    def agregar_contacto(self, nombre, telefono, correo):
        """Agrega un contacto en orden alfabético por nombre."""
        nuevo = NodoContacto(nombre, telefono, correo)

        # Si la lista está vacía o el nuevo va antes de la cabeza
        if self.cabeza is None or nuevo.nombre.lower() < self.cabeza.nombre.lower():
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        # Buscar la posición correcta
        actual = self.cabeza
        while (actual.siguiente is not None and
               actual.siguiente.nombre.lower() < nuevo.nombre.lower()):
            actual = actual.siguiente

        # Insertar en la posición encontrada
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def eliminar_contacto(self, nombre):
        """Elimina un contacto por nombre."""
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.nombre.lower() == nombre.lower():
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar_contacto(self, nombre):
        """Busca contactos que coincidan parcial o totalmente."""
        resultados = []
        actual = self.cabeza
        while actual is not None:
            if nombre.lower() in actual.nombre.lower():
                resultados.append(actual)
            actual = actual.siguiente
        return resultados

    def obtener_todos(self):
        """Devuelve todos los contactos en orden alfabético."""
        contactos = []
        actual = self.cabeza
        while actual is not None:
            contactos.append(actual)
            actual = actual.siguiente
        return contactos
    # Guardar en archivo JSON
    def guardar(self, archivo="datos/contactos.json"):
        """Guarda todos los contactos en un archivo JSON."""
        contactos = []
        actual = self.cabeza
        while actual:
            contactos.append({
                "nombre": actual.nombre,
                "telefono": actual.telefono,
                "correo": actual.correo
            })
            actual = actual.siguiente
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(contactos, f, indent=4, ensure_ascii=False)

    def cargar(self, archivo="datos/contactos.json"):
        """Carga contactos desde un archivo JSON."""
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                contactos = json.load(f)
            self.cabeza = None
            for c in contactos:
                self.agregar_contacto(c["nombre"], c["telefono"], c["correo"])
        except FileNotFoundError:
            print("⚠️ No existe el archivo, se inicia agenda vacía.")