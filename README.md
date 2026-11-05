# Práctica 1: Algoritmos de Búsqueda — Ramificación y Acotación (B&B) y A*

Este proyecto contiene la implementación y comparación de estrategias de búsqueda no informadas ($B\&B$) e informadas ($A^*$) sobre el problema del grafo de ciudades de Rumanía, desarrollado para la asignatura **Fundamentos de los Sistemas Inteligentes** de la **Universidad de Las Palmas de Gran Canaria (ULPGC)**.

---

## Estructura y Modificaciones del Código Base

El proyecto extiende la estructura base de AIMA en Python mediante las siguientes modificaciones:

### 1. `utils.py`
* **`PriorityQueue`**: Implementada como subclase de `Queue`.
  * Recibe una función evaluadora `f` en su constructor para extraer el menor coste.
  * Los elementos se insertan/ordenan con `reverse=True` usando `.sort(key=self.f, reverse=True)`. Esto permite que el elemento con menor valor $f(n)$ quede al final y se extraiga de forma directa mediante `.pop()`.
  * Soporte de `extend(items)` que inserta múltiples nodos y reordena la cola.
* **Importación de `math`**: Inclusión explícita de `import math` para permitir el cálculo de la distancia euclídea de la heurística.

### 2. `search.py`
* **`graph_search(problem, manager)`**:
  * Utiliza `manager` como nombre para la lista abierta.
  * **Test de objetivo diferido**: Se evalúa `problem.goal_test(node.state)` al **extraer el nodo** de la lista abierta, requisito obligatorio para garantizar optimidad en $B\&B$ y $A^*$.
  * Contabiliza los nodos expandidos (llamadas a `node.expand(problem)`) y actualiza el camino si se encuentra una ruta hacia un estado con menor `path_cost` $g(n)$.
* **`branch_and_bound_graph_search(problem)`**:
  * Implementa la Ramificación y Acotación pura (Coste Uniforme).
  * Función de evaluación: $f(n) = g(n) = \text{node.path\_cost}$.
* **`astar_graph_search(problem)`**:
  * Implementa Ramificación y Acotación con Subestimación ($A^*$).
  * Función de evaluación: $f(n) = g(n) + h(n) = \text{node.path\_cost} + \text{problem.h(node)}$.
  * Utiliza como heurística consistente la distancia en línea recta al nodo objetivo.

### 3. `run.py`
Archivo de ejecución principal que resuelve el problema `GPSProblem('A', 'B', search.romania)` e imprime la comparativa de los algoritmos de búsqueda.

---

## Resultados Obtenidos

Ejecución desde **Arad (A)** hasta **Bucharest (B)**:

| Algoritmo | Camino Resultante | Coste Total ($g$) | Observaciones |
| :--- | :--- | :--- | :--- |
| **BFS** | `['A', 'S', 'F', 'B']` | 450 | Selecciona la ruta con menos saltos (3 pasos), pero de mayor coste. |
| **DFS** | `['A', 'T', 'L', 'M', 'D', 'C', 'P', 'B']` | 733 | Explora profundamente la primera rama encontrada. |
| **B&B** | `['A', 'S', 'R', 'P', 'B']` | **418** | **Óptimo**. Explora strictly guiado por coste acumulado $g(n)$. |
| **A\*** | `['A', 'S', 'R', 'P', 'B']` | **418** | **Óptimo**. Obtiene la misma solución que $B\&B$ expandiendo **menos nodos** gracias a la heurística $h(n)$. |

---

## Ejecución

Para ejecutar el programa, utiliza el siguiente comando en la terminal:

```bash
python run.py
```

### Salida esperada:

```text
BFS: ['A', 'S', 'F', 'B']  :  450
DFS: ['A', 'T', 'L', 'M', 'D', 'C', 'P', 'B']  :  733
B&B: ['A', 'S', 'R', 'P', 'B']  :  418
A*: ['A', 'S', 'R', 'P', 'B']  :  418
```