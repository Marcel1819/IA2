from collections import deque
import copy

# Representación del estado inicial y objetivo
initial_state = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Función para verificar si dos estados son iguales
def states_equal(state1, state2):
    # Compara cada elemento de los dos estados
    return all(state1[i][j] == state2[i][j] for i in range(3) for j in range(3))

# Función para obtener los movimientos posibles desde un estado dado
def get_possible_moves(state):
    zero_pos = None
    # Encuentra la posición de la ficha vacía (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_pos = (i, j)
                break
    moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for d in directions:
        new_i, new_j = zero_pos[0] + d[0], zero_pos[1] + d[1]
        # Verifica si el movimiento es válido dentro del tablero
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            # Realiza el movimiento intercambiando la ficha vacía con otra
            new_state[zero_pos[0]][zero_pos[1]] = state[new_i][new_j]
            new_state[new_i][new_j] = 0
            moves.append(new_state)

    return moves

# Función para resolver el rompecabezas utilizando BFS
def solve_puzzle(initial_state, goal_state):
    queue = deque([(initial_state, [])])  # Inicializa la cola con el estado inicial
    visited = set()  # Conjunto para mantener los estados visitados

    while queue:
        current_state, path = queue.popleft()  # Obtiene el estado actual y el camino hasta aquí

        if states_equal(current_state, goal_state):
            return path  # Si el estado actual es igual al objetivo, se ha encontrado la solución

        visited.add(tuple(map(tuple, current_state)))  # Agrega el estado actual a los visitados

        for next_state in get_possible_moves(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                # Si el siguiente estado no ha sido visitado, lo encola y actualiza el camino
                queue.append((next_state, path + [next_state]))

# Resuelve el rompecabezas e imprime la solución
solution_path = solve_puzzle(initial_state, goal_state)
for i, state in enumerate(solution_path):
    print(f"Paso {i + 1}:\n")
    for row in state:
        print(row)
    print()