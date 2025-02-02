from os import system
from random import randrange

def generate_grid(size, excluded):
    grid = []
    for y in range(0, size):
        line = []
        for x in range(0, size):
            node = [y, x]
            balance = randrange(0, 100)
            if node not in excluded:
                if balance >= randrange(60, 100):
                    weight = -1
                else:
                    weight = randrange(1, 5)
            else:
                weight = 0
            line.append(weight)
        grid.append(line)
    return grid

# Convertir un nombre en emoji
def number_to_emoji(number):
    if number > 8:
        raise IndexError
    emojis = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣']
    return emojis[number]

def show_map_tmp(start, end, grid, queue, visited):
    system('clear')
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):
            node = [y, x]
            emoji = "🟥"
            if node == start:
                emoji = "⚪"
            elif node == end:
                emoji = "🟣"
            elif is_block(grid[node[0]][node[1]]):
                emoji = "⬛"
            elif node in queue:
                emoji = "🟧"
            elif node in visited:
                emoji = "🟩"
            print(emoji, end=" ")
        print()

def show_map(start, end, grid, path):
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):
            node = [y, x]
            emoji = "🟥"
            if node == start:
                emoji = "⚪"
            elif node == end:
                emoji = "🟣"
            elif is_block(grid[node[0]][node[1]]):
                emoji = "⬛"
            elif tuple(node) in path:
                emoji = "🟩"
            else:
                emoji = number_to_emoji(grid[node[0]][node[1]])
            print(emoji, end=" ")
        print()

def is_block(weight):
    return True if weight < 0 else False

def get_neighbors(parent, max):
    nodes = [
        [parent[0] - 1, parent[1]],
        [parent[0], parent[1] + 1],
        [parent[0] + 1, parent[1]],
        [parent[0], parent[1] - 1],
    ]
    tmp = []
    for node in nodes:
        if (node[0] >= 0 and node[0] < max and node[1] >= 0 and node[1] < max):
            tmp.append(node)
    return tmp

def backtrace(start, end, history):
    trace = history[(end[0], end[1])]["current"]
    path = [tuple(end), tuple(trace)]
    try:
        while(history[tuple(trace)]):
            trace = history[tuple(trace)]["current"]
            path.append(trace)
    except KeyError:
        return path[::-1]

def exists(grid, node, history):
    return (node[0], node[1]) in history

def getCurrentNode(node, history):
    return history[(node[0], node[1])]["current"]

def getWeight(node, history):
    return history[(node[0], node[1])]["weight"]

def discover_cells(start, end, grid):
    queue = [start]
    visited = []
    history = {}
    size = len(grid)
    add_cell_to_queue = True
    while(len(queue) > 0):
        parent = queue.pop(0)
        visited.append(parent)
        show_map_tmp(start, end, grid, queue, visited)
        for node in get_neighbors(parent, size):
            if not is_block(grid[node[0]][node[1]]):
                update_cell = False
                add_cell_to_history = True
                weight = grid[node[0]][node[1]]
                trace_current = None
                trace_weight  = None
                if exists(grid, parent, history):
                    weight = getWeight(parent, history) + weight
                    if exists(grid, node, history):
                        if (weight < getWeight(node, history) 
                        and getCurrentNode(node, history) != (parent[0],parent[1])):
                            trace_current = (parent[0], parent[1])
                            trace_weight  = weight
                            update_cell = True
                        else:
                            add_cell_to_history = False
                    else:
                        trace_current = (parent[0], parent[1])
                        trace_weight  = weight
                else:
                    trace_current = (parent[0], parent[1])
                    trace_weight  = weight

                trace = {
                    (node[0],  node[1]): {
                        "current": trace_current,
                        "weight": trace_weight
                    }
                }

                if update_cell:
                    history.update(trace)

                if node == end:
                    if True == add_cell_to_history:
                        history.update(trace)
                    add_cell_to_queue = False
                    break
                elif (node not in queue and node not in visited):
                    if True == add_cell_to_history:
                        history.update(trace)
                    if add_cell_to_queue:
                        queue.append(node)
    return history

if __name__ == "__main__":
    start = [0, 0]
    end = [4, 4]

    grid = generate_grid(5, [start, end])

    history = discover_cells(start, end, grid)

    if ((end[0], end[1]) in history): 
        path = backtrace(start, end, history)
        system('clear')
        show_map(start, end, grid, path)
        print("Chemin : " + str(path))
        print("Poids : " + str(history[(end[0],end[1])]["weight"]))
        show_map(start,end, grid, [])
    else:
        print("Point de destination inaccessible !")
