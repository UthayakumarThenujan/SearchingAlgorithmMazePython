from Pymaze import maze, COLOR, agent, textLabel


def DFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]

    dfsPath = {}

    while len(frontier) > 0:
        currCell = frontier.pop()

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
                frontier.append(child)
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
    print("DFS: ", count)
    return fwdPath, count


m = maze()
m.CreateMaze()
path = DFS(m)
textLabel(m, "DFS paths:", path[1])
a = agent(m, footprints=True, filled=True)
m.tracePath({a: path[0]}, showMarked=True, delay=10)
m.run()
