start = [0,0]
end   = [2,2]

matrix = [
    [1, 1, 1],
    [2, 123321, 65],
    [1, 42, 1]
]

queue   = [start]
visited = []
link    = []

for y in range(0, 3):
    link.append([])
    for x in range(0, 3):    
        link[y].append(
            {
                "weight": None,
                "current": None
            }
        )

while queue:
    cell = queue.pop(0)
    visited.append(cell)

    cells = [
        [cell[0] - 1, cell[1]],
        [cell[0], cell[1] + 1],
        [cell[0] + 1, cell[1]],
        [cell[0], cell[1] - 1]
    ]

    for vertex in cells:
        if (vertex[0] >= 0 and vertex[0] < 3 and vertex[1] >= 0 and vertex[1] < 3):
            if vertex not in queue and vertex not in visited:
                queue.append(vertex)
            weight = matrix[cell[0]][cell[1]] + matrix[vertex[0]][vertex[1]]
            if None == link[vertex[0]][vertex[1]]["weight"] or weight < link[vertex[0]][vertex[1]]["weight"]:
                link[vertex[0]][vertex[1]]["weight"]  = weight
                link[vertex[0]][vertex[1]]["current"] = cell

for y in range(0, 3):
    print(y)
    for x in range(0, 3):    
        print(link[y][x])
