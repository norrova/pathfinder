start = [0,0]
end   = [2,2]

matrix = [
    [0, 1, 5],
    [1, 3, 1],
    [1, -1, 1]
]

queue   = [start]
visited = []
closed  = []
link    = []

for y in range(0, 3):
    link.append([])
    for x in range(0, 3):    
        link[y].append(
            {
                "weight": None,
                "current": None,
            }
        )

def backtrace(node):
    path = [node]
    current = link[node[0]][node[1]]["current"]
    while (current != None):
        path.append(current)
        current = link[current[0]][current[1]]["current"]
    return path

def getNeighbors(node, length):
    y = node[0]
    x = node[1]
    cells = [
        [y - 1, x],
        [y, x + 1],
        [y + 1, x],
        [y, x - 1]
    ]
    neighbors = []
    for vertex in cells:
        y = vertex[0]
        x = vertex[1]
        if (
            x >= 0 
            and x < length 
            and y >= 0
            and y < length
            and not isBlock(vertex)
        ):
            neighbors.append(vertex)
    return neighbors

def isBlock(node):
    y = node[0]
    x = node[1]
    return True if matrix[y][x] == -1 else False


def printStack():
    for y in range(0, 3):
        print(y)
        for x in range(0, 3):    
            print(link[y][x])

def printVisual(trace):
    for y in range(0, 3):
        for x in range(0, 3):    
            cell = [y, x]
            emoji = "🟥"
            if cell in trace:
                emoji = "🟩"
            print(emoji, end=' ')
        print()

link[start[0]][start[1]]["weight"] = 0
while queue:
    cell = queue.pop(0)
    closed.append(cell)

    # Si trouve la cellule
    if (cell == end):
        printStack()
        trace = backtrace(cell)
        print(trace)
        printVisual(trace)
        exit(0)

    # Propagation voisin
    for vertex in getNeighbors(cell, 3):
        # Vérifie si le sommet est encore disponible
        if (vertex in closed):
            continue
    
        # Récupération X et Y
        y = vertex[0]
        x = vertex[1]

        # Récupérer le poid du vertex
        if link[cell[0]][cell[1]]["weight"] != None:
            # Poid current + poid matrix
            weight = link[cell[0]][cell[1]]["weight"] + matrix[vertex[0]][vertex[1]]

            if (link[y][x]["weight"] == None or weight < link[y][x]["weight"]):
                link[vertex[0]][vertex[1]]["weight"] = weight
                link[vertex[0]][vertex[1]]["current"] = cell

        # Ajouter que si n'est pas dans la queue
        if vertex not in queue:
            queue.append(vertex)
        """
        Debug
        print("cell" + str(cell))
        print("vertex" + str(vertex))
        print("queue" + str(queue))
        print("closed" + str(closed))
        printStack()
        input()
        """
