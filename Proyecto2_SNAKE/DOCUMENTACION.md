# 📋 Documentación del Proyecto Snake

## Índice
1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Patrón de Arquitectura (MVC)](#patrón-de-arquitectura-mvc)
3. [Modelo de Datos](#modelo-de-datos)
4. [Sistema de Vistas](#sistema-de-vistas)
5. [Movimiento de la Serpiente](#movimiento-de-la-serpiente)
6. [Colisiones y Game Over](#colisiones-y-game-over)
7. [Interacción con la Manzana](#interacción-con-la-manzana)
8. [Diseño de la Interfaz](#diseño-de-la-interfaz)
9. [Flujo del Programa](#flujo-del-programa)
10. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 1. Estructura del Proyecto

El proyecto utiliza una **arquitectura de tres capas** (MVC - Model-View-Controller):

```
Proyecto2_SNAKE/
├── main.py                 # Punto de entrada del programa
├── model/
│   └── model.py           # Lógica del juego (datos y cálculos)
├── view/
│   └── view.py            # Renderizado visual (interfaz gráfica)
├── controller/
│   └── controller.py      # Coordinador de entrada y lógica
└── __pycache__/           # Archivos compilados de Python
```

### ¿Por qué esta estructura?
- **Separación de responsabilidades**: Cada componente tiene una función clara
- **Mantenibilidad**: Cambios en la visual no afectan la lógica del juego
- **Reutilización**: El modelo puede usarse con diferentes vistas
- **Facilidad de pruebas**: Cada módulo puede testearse independientemente

---

## 2. Patrón de Arquitectura (MVC)

El proyecto implementa el patrón **Model-View-Controller**:

### 📊 Diagrama de flujo

```
┌─────────────────────────────────────────────────────────┐
│                   MAIN.PY (Entrada)                     │
│         Inicializa Model, View y Controller              │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   ┌────────┐  ┌────────┐  ┌────────────┐
   │ MODEL  │  │ VIEW   │  │ CONTROLLER │
   │ (Datos)│  │(Visual)│  │(Entrada)   │
   └────────┘  └────────┘  └────────────┘
        ▲              ▲              │
        │              │              │
        └──────────────┼──────────────┘
                       │
              ┌────────▼────────┐
              │  BUCLE PRINCIPAL │
              └──────────────────┘
```

### Responsabilidades:

| Componente | Responsabilidad |
|-----------|-----------------|
| **Model** | Gestiona el estado del juego (posición de serpiente, manzana, puntuación) |
| **View** | Dibuja en pantalla todo lo visual |
| **Controller** | Captura entrada del usuario y coordina las acciones |

---

## 3. Modelo de Datos (SnakeModel)

El modelo almacena **todos los datos del juego** usando estructuras simples:

### Atributos principales:

```python
class SnakeModel:
    # Dimensiones de la pantalla
    width = 800          # ancho en píxeles
    height = 600         # alto en píxeles
    cell_size = 20       # tamaño de cada celda de la cuadrícula
    
    # Estado del juego
    snake = [(100, 100), (80, 100), (60, 100)]  # Lista de (x, y) del cuerpo
    direction = (20, 0)   # Dirección actual: (dx, dy) en píxeles
    apple = (400, 300)    # Posición de la manzana: (x, y)
    score = 0             # Puntuación actual
```

### ¿Cómo se estructura la serpiente?

La serpiente es una **lista de tuplas** donde cada tupla representa las coordenadas de un segmento:

```
snake = [(100, 100), (80, 100), (60, 100)]
         └─ Cabeza  │           │
                    Cuerpo      Cola
```

- **Índice 0**: Siempre es la **cabeza** (parte frontal que se mueve)
- **Índices 1 al final**: Son el **cuerpo** (sigue a la cabeza)

### Sistema de coordenadas

Las posiciones se almacenan en **píxeles**:
- Origen (0, 0) está en la **esquina superior izquierda**
- X aumenta hacia la **derecha**
- Y aumenta hacia **abajo**

```
(0,0) ─────────────────────► X
  │
  │      serpiente (100, 100)
  │            ●
  ▼
  Y
```

---

## 4. Sistema de Vistas (SnakeView)

La vista es responsable de **dibujar todo en pantalla** usando la librería `pygame`.

### Inicialización de colores:

```python
self.BACKGROUND = (15, 15, 60)       # Azul oscuro (fondo)
self.GRID_COLOR = (30, 30, 80)       # Azul más claro (cuadrícula)
self.SNAKE_COLOR = (102, 255, 102)   # Verde brillante
self.SNAKE_BORDER = (0, 120, 0)      # Verde oscuro (borde)
self.APPLE_COLOR = (255, 80, 80)     # Rojo
self.INFO_BG = (10, 10, 30)          # Panel de información
self.INFO_TEXT = (240, 240, 180)     # Texto de información
self.BORDER_COLOR = (70, 130, 180)   # Borde del tablero
```

### Método principal: `draw()`

Este método se llama cada fotograma:

```python
def draw(self, snake, apple, score):
    self.draw_background()      # 1. Llena el fondo
    self.draw_border()          # 2. Dibuja borde del tablero
    self.draw_snake(snake)      # 3. Dibuja la serpiente
    self.draw_apple(apple)      # 4. Dibuja la manzana
    self.show_info(score)       # 5. Muestra puntuación y tiempo
    pygame.display.flip()       # 6. Actualiza la pantalla
```

### Proceso de renderizado:

1. **draw_background()**: Llena toda la pantalla con color de fondo y dibuja una cuadrícula sutil
2. **draw_border()**: Dibuja un rectángulo de borde alrededor del área de juego
3. **draw_snake()**: Itera por cada segmento y dibuja un cuadrado
4. **draw_apple()**: Dibuja la manzana con bordes redondeados
5. **show_info()**: Muestra el panel superior con puntuación y tiempo
6. **pygame.display.flip()**: Refresca la pantalla

---

## 5. Movimiento de la Serpiente

El movimiento es uno de los **núcleos del juego**.

### ¿Cómo se mueve?

1. **Se calcula la nueva cabeza** basada en la dirección actual
2. **Se añade la nueva cabeza** al frente de la lista
3. **Se elimina la cola** (a menos que haya comido)

```python
def move(self):
    # 1. Calcular nueva posición de la cabeza
    head_x, head_y = self.snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    
    # 2. Insertar nueva cabeza al frente
    self.snake.insert(0, new_head)
    
    # 3. Eliminar cola (a menos que coma)
    self.snake.pop()  # El cuerpo "sigue" a la cabeza
```

### Visualización del movimiento paso a paso:

```
Turno 0:           Turno 1:           Turno 2:
(100,100)          (120,100)          (140,100)
  ●                  ●                  ●
(80,100) ●        (100,100) ●        (120,100) ●
  ●                  ●                  ●
(60,100) ●        (80,100) ●        (100,100) ●

Dirección: →        Dirección: →       Dirección: →
```

### Sistema de dirección:

La dirección se representa como un vector `(dx, dy)` en píxeles:

| Tecla | Dirección | Vector |
|------|-----------|--------|
| ↑ UP | Arriba | (0, -20) |
| ↓ DOWN | Abajo | (0, 20) |
| ← LEFT | Izquierda | (-20, 0) |
| → RIGHT | Derecha | (20, 0) |

---

## 6. Colisiones y Game Over

El juego termina cuando ocurre una **colisión**. Hay dos tipos:

### Tipos de colisión:

#### 1. **Colisión con paredes**
```python
def collision(self):
    x, y = new_head
    
    # Detectar si salió del tablero
    if x < 0 or x >= self.width or y < 0 or y >= self.height:
        return True  # ¡Colisión!
```

#### 2. **Colisión con el propio cuerpo**
```python
def collision(self):
    # La nueva cabeza no puede estar en el cuerpo (excepto la cabeza actual)
    if self.new_head in self.snake[1:]:  # [1:] = todo excepto la cabeza
        return True  # ¡Colisión!
```

### Pantalla de Game Over:

```python
def game_over(self):
    # Crear un overlay oscuro (80% transparente)
    overlay.fill((0, 0, 0, 180))
    
    # Mostrar "GAME OVER" en rojo
    text = "GAME OVER"
    
    # Mostrar mensaje
    subtext = "Gracias por jugar. Cierra la ventana para salir."
    
    # Esperar 2 segundos
    pygame.time.wait(2000)
    pygame.quit()
```

---

## 7. Interacción con la Manzana

### ¿Qué ocurre cuando la serpiente come?

Cuando la **nueva cabeza** ocupa la misma posición que la **manzana**:

```python
def move(self):
    # Si la cabeza está en la manzana
    if self.new_head == self.apple:
        self.spawn_apple()      # Generar nueva manzana
        self.score += 1         # Sumar puntuación
        # NO hacer pop() - la serpiente CRECE
    else:
        self.snake.pop()        # Movimiento normal - eliminar cola
```

### Comparación: Comer vs No comer

#### SIN comer (movimiento normal):
```
Antes:           Después:
●●●●            ●●●●
   ●              ●●●

La serpiente mantiene la misma longitud
```

#### COMIENDO:
```
Cabeza en:
●●●●✓ (manzana)

Después:
●●●●●

La serpiente CRECE en una unidad
```

### Generación de la manzana:

```python
def spawn_apple(self):
    while True:
        # Generar posición aleatoria (en unidades de cell_size)
        apple_x = random.randint(0, (width // cell_size) - 1) * cell_size
        apple_y = random.randint(0, (height // cell_size) - 1) * cell_size
        new_apple = (apple_x, apple_y)
        
        # Asegurar que no aparezca donde está la serpiente
        if new_apple not in self.snake:
            self.apple = new_apple
            break  # ¡Posición válida encontrada!
```

---

## 8. Diseño de la Interfaz

### Disposición de la interfaz:

```
┌──────────────────────────────────────────────┐
│ SNAKE                                        │  ◄─ Panel de info
│ Score: 005   Time: 042                       │
├──────────────────────────────────────────────┤  ◄─ Borde del tablero
│  . . . . . . . . . . . . . . . . . . . . .   │
│  .                                        .   │
│  .        ●                               .   │
│  .        ●                               .   │
│  .        ●                               .   │
│  .                                        .   │
│  .                    ✓                   .   │
│  .                                        .   │
│  . . . . . . . . . . . . . . . . . . . . .   │
└──────────────────────────────────────────────┘
```

### Elementos visuales:

| Elemento | Color | Función |
|----------|-------|---------|
| Fondo | Azul oscuro (15,15,60) | Area de juego |
| Cuadrícula | Azul claro (30,30,80) | Referencia visual |
| Borde | Azul medio (70,130,180) | Límite del tablero |
| Serpiente | Verde (102,255,102) | Jugador |
| Manzana | Rojo (255,80,80) | Objetivo |
| Panel info | Azul muy oscuro (10,10,30) | Puntuación/tiempo |
| Texto | Beige (240,240,180) | Legibilidad |

### Velocidad de renderizado:

```python
def tick(self, fps=10):
    self.clock.tick(fps)  # 10 fotogramas por segundo
```

- **10 FPS**: El juego se actualiza 10 veces por segundo
- **Cada frame**: ~100ms entre actualizaciones

---

## 9. Flujo del Programa

### Secuencia de inicio:

```
1. main.py se ejecuta
2. Crear SnakeView()
3. Crear SnakeModel()
4. Crear SnakeController()
5. controller.run()  ◄── BUCLE PRINCIPAL
```

### Bucle principal (`controller.run()`):

```
while running:
    ├─ handle_events()      # Captura entrada del usuario
    ├─ model.move()         # Actualiza posición
    ├─ view.draw()          # Renderiza pantalla
    ├─ view.tick()          # Controla FPS
    └─ Si colisión: GAME OVER
```

---

## 10. Preguntas Frecuentes

### ¿Cómo se guarda el estado en el modelo?

El modelo mantiene todos los datos del juego:
- **snake**: Lista de tuplas con coordenadas de cada segmento
- **apple**: Tupla con coordenadas de la manzana
- **direction**: Vector de movimiento
- **score**: Puntuación actual

### ¿Cómo se muestra en la vista?

La vista recibe los datos del modelo y los dibuja:
1. Itera sobre la lista de serpiente y dibuja cada segmento
2. Dibuja la manzana en su posición
3. Muestra la puntuación en el panel superior
4. Actualiza la pantalla

### ¿Por qué la serpiente crece al comer?

Porque cuando come, **NO se elimina la cola**:
```python
if self.new_head == self.apple:
    # Cuando come, NO hace pop()
    # La serpiente mantiene todos sus segmentos + la nueva cabeza
else:
    self.snake.pop()  # Sin comer, elimina la cola
```

### ¿Qué pasa en una colisión?

- `model.move()` retorna `False`
- El controller detiene el bucle principal
- Se muestra la pantalla de "GAME OVER"
- El programa se cierra

---

**Documentación creada**: 2026-06-30
