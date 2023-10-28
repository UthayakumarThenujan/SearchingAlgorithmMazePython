from Pymaze import maze, COLOR, agent, textLabel


def BFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    parent = [start]

    dfsPath = {}

    while len(parent) > 0:
        currCell = parent.pop(0)

        if currCell == m._goal:
            break
        poss = 0

        for d in "ESNW":
            if m.maze_map[currCell][d] == True:
                if d == "E":
                    child = (currCell[0], currCell[1] + 1)
                if d == "S":
                    child = (currCell[0] + 1, currCell[1])
                if d == "N":
                    child = (currCell[0] - 1, currCell[1])
                if d == "W":
                    child = (currCell[0], currCell[1] - 1)

                if child in explored:
                    continue
                poss += 1
                explored.append(child)
                parent.append(child)
                dfsPath[child] = currCell
        if poss > 1:
            m.markCells.append(currCell)

    fwdPath = {}
    cell = m._goal
    count = 0
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
        count += 1
    print("BFS: ", count)
    return fwdPath, count


m = maze(20, 20)
m.CreateMaze()
path = BFS(m)
a = agent(m, footprints=True, filled=True)
m.tracePath({a: path[0]}, showMarked=True, delay=100)
textLabel(m, "BFS paths:", path[1])
m.run()
