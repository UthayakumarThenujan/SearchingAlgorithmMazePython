def dijkstra(graph, start, goal):
    unvisited = {n: float("inf") for n in graph.keys()}
    unvisited[start] = 0
    visited = {}
    revPath = {}
    print(".......................")
    print(f"{unvisited=}")
    print(f"{visited=}")
    print(".......................")
    while unvisited:
        minNode = min(unvisited, key=unvisited.get)
        visited[minNode] = unvisited[minNode]

        # if minNode == goal:
        #     break
        print("...........IN FOR...........")
        for neigbor in graph.get(minNode):
            if neigbor in visited:
                continue
            tempDist = unvisited[minNode] + graph[minNode][neigbor]
            if tempDist < unvisited[neigbor]:
                unvisited[neigbor] = tempDist
                revPath[neigbor] = minNode
            print(f"{unvisited=}")
            print(f"{visited=}")

        unvisited.pop(minNode)
        print(".......................")
        print(f"{unvisited=}")
        print(f"{visited=}")
    # node = goal
    # revPathString = node
    # while node != start:
    #     revPathString += revPath[node]
    #     node = revPath[node]
    # fwdPath = revPathString[::-1]
    # return visited[goal]


myGraph = {
    "A": {"B": 2, "C": 9, "F": 4},
    "B": {"C": 6, "E": 3, "F": 2},
    "C": {"D": 1},
    "D": {"C": 2},
    "E": {"D": 5, "C": 2},
    "F": {"E": 3},
}

dijkstra(myGraph, "A", "D")
