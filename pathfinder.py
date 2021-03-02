from os import system
from random import randrange

def generate_grid(size, excluded):
    grid = []
    for y in range(0, size):
        line = []
        for x in range(0, size):
            node = [y, x]
            balance = randrange(0, 100)
            weight = 1
            if (balance >= randrange(50, 100) 
            and node not in excluded):
                weight = - 1
            line.append(weight)
        grid.append(line)
    return grid

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
            elif tuple(node) in path:
                emoji = "🟩"
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

def discover(start, end, grid):
    queue = [start]
    visited = []
    history = {}
    size = len(grid)
    while(len(queue) > 0):
        parent = queue.pop(0)
        visited.append(parent)
        show_map_tmp(start, end, grid, queue, visited)
        for node in get_neighbors(parent, size):
            if not is_block(grid[node[0]][node[1]]):
                weight = grid[node[0]][node[1]]
                if (parent[0], parent[1]) in history:
                    weight = history[(parent[0], parent[1])]["weight"] + weight
                trace =  {
                            (node[0], node[1]): {
                                "current": (parent[0], parent[1]),
                                "weight": weight
                            }
                        }
                if node == end:
                    history.update(trace)
                    queue = []
                    break
                elif (node not in queue 
                    and node not in visited
                ):
                    history.update(trace)
                    queue.append(node)
    return history

if __name__ == "__main__":
    start = [0, 0]
    end = [9, 9]

    grid = generate_grid(10, [start, end])

    history = discover(start, end, grid)

    if ((end[0], end[1]) in history): 
        path = backtrace(start, end, history)
        show_map(start, end, grid, path)
        print("Chemin : " + str(path))
        print("Poids : " + str(history[(end[0],end[1])]["weight"]))
    else:
        print("Point de destination inaccessible !")
