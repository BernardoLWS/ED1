import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.configurar_ventana()
        self.crear_interfaz()
        
    def configurar_ventana(self):
        self.page.title = "Programa de proyectos - MVC"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.bgcolor = "grey50"
        self.page.padding = 20
        self.page.spacing = 20

    def crear_interfaz(self):
        # Título principal
        titulo = ft.Text("Gestor y Visualizador de Proyectos", size=22, weight="bold", color="blue900")
        
        # Panel de entrada de datos y botones de control
        panel_controles = ft.Column([
            ft.Row([
                ft.FilledButton("Agregar Inicio", bgcolor="lightblue",width=140),
                ft.FilledButton("Agregar Final", bgcolor="lightblue",width=140),
                ft.Text("Entrada :", size=22, weight="bold", color="black"),
                ft.TextField(label="Ingrese datos aqui."),
                ft.FilledButton("Ejecutar accion",bgcolor="lightblue",width=140),
                ft.FilledButton("Desacer",bgcolor="lightblue",width=140),
                ft.FilledButton("Rehacer",bgcolor="lightblue",width=140),
            ]),
            ft.Row([
                ft.FilledButton("Buscar",bgcolor="lightblue",width=140),
                ft.FilledButton("Eliminar",bgcolor="lightblue",width=140),
                ft.FilledButton("Encolar",bgcolor="lightblue",width=140),
                ft.FilledButton("Desencolar",bgcolor="lightblue",width=140),
            ]),

        
        ],alignment=ft.MainAxisAlignment.CENTER, spacing=10)

        # =========================================================================
        # 1. PARTE IZQUIERDA: LISTA DOBLEMENTE ENLAZADA
        # =========================================================================
        # titulo :
        lbl_lista = ft.Text("Lista Doblemente Enlazada", weight="bold", size=14, color="purple900")
        elementos_lista = ["Proyecto Alpha", "Proyecto Beta", "Proyecto Gamma"]
        
        nodos_lista_items = [ft.Container(content=ft.Text("None", italic=True, size=11), padding=6, bgcolor="grey300", border_radius=4)]
        for elem in elementos_lista:
            nodos_lista_items.append(ft.Text(" ⇄ ", weight="bold", size=14, color="purple700"))
            nodos_lista_items.append(
                ft.Container(
                    content=ft.Text(elem, weight="bold", size=11),
                    padding=8,
                    bgcolor="purple100",
                    border_radius=6,
                    border=ft.Border.all(1, "purple400")
                )
            )
        nodos_lista_items.append(ft.Text(" ⇄ ", weight="bold", size=14, color="purple700"))
        nodos_lista_items.append(ft.Container(content=ft.Text("None", italic=True, size=11), padding=6, bgcolor="grey300", border_radius=4))
        
        seccion_lista = ft.Container(
            content=ft.Column([
                lbl_lista,
                ft.Row(nodos_lista_items, scroll=ft.ScrollMode.AUTO, spacing=4, alignment=ft.MainAxisAlignment.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            bgcolor="white",
            border_radius=10,
            border=ft.Border.all(3, "purple200"),
            expand=True
        )

        # =========================================================================
        # 2. PARTE DERECHA: PILA
        # =========================================================================
        lbl_pila = ft.Text("Pila (Historial / Acciones)", weight="bold", size=14, color="blue900")
        elementos_pila = ["Proyecto C (Cima)", "Proyecto B", "Proyecto A (Base)"]
        contenedores_pila = []
        
        for i, elem in enumerate(elementos_pila):
            bg_color = "blue200" if i == 0 else "blue100"
            border_color = "blue400" if i == 0 else "blue300"
            contenedores_pila.append(
                ft.Container(
                    content=ft.Text(elem, weight="bold" if i == 0 else "normal", size=12, color="black87"),
                    padding=8,
                    bgcolor=bg_color,
                    border_radius=6,
                    width=180,
                    border=ft.Border.all(1.2, border_color)
                )
            )
        
        seccion_pila = ft.Container(
            content=ft.Column([
                lbl_pila,
                ft.Column(contenedores_pila, spacing=4, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            bgcolor="white",
            border_radius=10,
            border=ft.Border.all(1, "blue200"),
            width=220
        )

        # Fila superior que une la IZQUIERDA (Lista) y la DERECHA (Pila)
        seccion_superior = ft.Row([
            seccion_lista,
            seccion_pila
        ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START, spacing=15)

        # =========================================================================
        # 3. PARTE ABAJO: COLA DE PRIORIDAD
        # =========================================================================
        lbl_cola = ft.Text("Cola de Prioridad (Tareas)", weight="bold", size=14, color="green900")
        tareas_prio = [
            {"nombre": "Base de Datos", "prio": "Alta (1)", "color": "red200", "borde": "red400"},
            {"nombre": "Diseño Login", "prio": "Media (2)", "color": "orange200", "borde": "orange400"},
            {"nombre": "Documentación", "prio": "Baja (3)", "color": "green200", "borde": "green400"},
        ]
        
        tarjetas_fila = []
        for t in tareas_prio:
            tarjetas_fila.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"Prioridad: {t['prio']}", size=10, weight="bold", color="black54"),
                        ft.Text(t['nombre'], size=12, weight="bold", color="black"),
                    ], spacing=2),
                    padding=10,
                    bgcolor=t['color'],
                    border_radius=8,
                    width=150,
                    height=60,
                    border=ft.Border.all(1.2, t['borde'])
                )
            )
        
        seccion_abajo = ft.Container(
            content=ft.Column([
                lbl_cola,
                ft.Row(tarjetas_fila, scroll=ft.ScrollMode.AUTO, spacing=10, alignment=ft.MainAxisAlignment.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            bgcolor="white",
            border_radius=10,
            border=ft.Border.all(1, "green200")
        )

        # Agregamos todo estructurado a la página principal
        self.page.add(
            titulo,
            panel_controles,
            ft.Divider(),
            seccion_superior,
            seccion_abajo
        )
        self.page.update()

def main(page: ft.Page):
    View(page)

if __name__ == "__main__":
    ft.run(main)