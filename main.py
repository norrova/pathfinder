def findDestination(matrix, start, end): 
    queue = [start]
    flagged = queue.copy()
    while len(queue) > 0:
        cell = queue.pop()
        print(queue)
        for cellAdjacent in get_surrounding_cells(cell):
            if cellAdjacent not in flagged:
                queue.append(cellAdjacent)
                flagged.append(cellAdjacent)
                
def get_surrounding_cells(cell):
    tmp_y = cell[0]
    tmp_x = cell[1]
    cells_around = []
    for x in [ tmp_x-1, tmp_x, tmp_x+1]:
        for y in  [ tmp_y-1, tmp_y, tmp_y+1]:
            if(x >= 0 and x < 5 and y >= 0 and y < 5):
                cells_around.append([x, y])
    return cells_around

if __name__ == "__main__":
    matrix = [
        [0,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]
    ] 
    findDestination(matrix, [1,1], [3,4])
