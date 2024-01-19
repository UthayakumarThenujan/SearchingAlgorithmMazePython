from Pymaze import maze, COLOR, agent, textLabel
from queue import PriorityQueue


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1 - x2) + abs(y1 - y2)


def aStar(m):
    start = (m.rows, m.cols)

    g_score = {cell: float("inf") for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float("inf") for cell in m.grid}
    f_score[start] = h(start, (1, 1))

    open = PriorityQueue()
    open.put((h(start, (1, 1)), h(start, (1, 1)), start))
    aPath = {}
    spath = 0
    while not open.empty():
        currCell = open.get()[2]
        if currCell == (1, 1):
            break
        for d in "ESNW":
            if m.maze_map[currCell][d] == True:
                if d == "E":
                    childCell = (currCell[0], currCell[1] + 1)
                if d == "W":
                    childCell = (currCell[0], currCell[1] - 1)
                if d == "N":
                    childCell = (currCell[0] - 1, currCell[1])
                if d == "S":
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, (1, 1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, h(childCell, (1, 1)), childCell))
                    aPath[childCell] = currCell

                spath += 1
    fwdPath = {}
    cell = (1, 1)
    count = 0
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
        count += 1
    return fwdPath, count, spath


m = maze(20, 20)
m.CreateMaze()
path = aStar(m)

a = agent(m, footprints=True, filled=True, color=COLOR.blue)

textLabel(m, "A* paths:", path[1])
m.tracePath({a: path[0]}, showMarked=True, delay=100)


m.run()
