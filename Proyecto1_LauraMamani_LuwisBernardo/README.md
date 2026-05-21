# 📒 Agenda de Contactos

Proyecto desarrollado por **Laura Mamani** y **Luwis Bernardo** como parte del Proyecto 1.

---

## Descripción

Aplicación de escritorio para gestionar una agenda de contactos personales. Permite agregar, buscar, eliminar, guardar y cargar contactos mediante una interfaz gráfica construida con **Tkinter**. Los contactos se almacenan internamente en una **lista enlazada** ordenada alfabéticamente y se persisten en un archivo **JSON**.

---

## Estructura del Proyecto

```
Proyecto1_LauraMamani_LuwisBernardo/
│
├── main.py                   # Punto de entrada de la aplicación
│
├── model/
│   └── model.py              # Lógica de datos: lista enlazada de contactos
│
├── view/
│   └── view.py               # Interfaz gráfica con Tkinter
│
├── controller/
│   └── controller.py         # Controlador: conecta la vista con el modelo
│
└── datos/
    └── contactos.json        # Archivo de persistencia de contactos
```

El proyecto sigue el patrón de diseño **MVC (Modelo - Vista - Controlador)**.

---

## Funcionalidades

- **Agregar contacto** — Ingresa nombre, teléfono y correo. El contacto se inserta automáticamente en orden alfabético.
- **Eliminar contacto** — Selecciona un contacto de la lista y elimínalo con un clic.
- **Buscar contacto** — Búsqueda parcial o total por nombre.
- **Guardar** — Exporta todos los contactos al archivo `datos/contactos.json`.
- **Cargar** — Importa los contactos guardados desde el archivo JSON al iniciar o en cualquier momento.

---

## Validaciones

Al agregar un contacto, el sistema valida que:

- El **nombre** no esté vacío y contenga solo letras y espacios.
- El **teléfono** no esté vacío y contenga solo dígitos.
- El **correo** contenga `@` y `.com`.

---

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)

No se requieren librerías externas.

---

## Cómo ejecutar

1. Clona o descomprime el proyecto.
2. Desde la raíz del proyecto, ejecuta:

```bash
python main.py
```

---

## Estructura de datos

Los contactos se gestionan mediante una **lista enlazada simple** (`NodoContacto`), donde cada nodo almacena:

| Campo     | Descripción              |
|-----------|--------------------------|
| `nombre`  | Nombre completo          |
| `telefono`| Número de teléfono       |
| `correo`  | Dirección de correo      |

La lista se mantiene ordenada alfabéticamente en cada inserción.

El archivo de persistencia `contactos.json` sigue este formato:

```json
[
    {
        "nombre": "Ana López",
        "telefono": "71234567",
        "correo": "ana@ejemplo.com"
    }
]
```

---

## Autores

| Nombre          | Rol         |
|-----------------|-------------|
| Laura Mamani    | Desarrolladora |
| Luwis Bernardo  | Desarrollador  |
