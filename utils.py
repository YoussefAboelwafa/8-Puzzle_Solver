def getEmptyCell(state):
    for i in range(9):
        if state[i] == "0":
            return i


def swap(state, idx1, idx2):
    state_list = list(state)
    state_list[idx1], state_list[idx2] = state_list[idx2], state_list[idx1]
    return "".join(state_list)


def getNeighbours(state):
    neighbours = []
    # todo empty cell
    emptyCell = getEmptyCell(state)
    if emptyCell % 3 != 0:
        neighbours.append(swap(state, emptyCell, emptyCell - 1))
    if emptyCell % 3 != 2:
        neighbours.append(swap(state, emptyCell, emptyCell + 1))
    if emptyCell // 3 != 0:
        neighbours.append(swap(state, emptyCell, emptyCell - 3))
    if emptyCell // 3 != 2:
        neighbours.append(swap(state, emptyCell, emptyCell + 3))
    return neighbours


def print_path(parent, goal_state):
    curr = goal_state
    cost = 0
    path = []
    while parent[curr] != curr:
        path.append(curr)
        curr = parent[curr]
        cost += 1
    path.append(curr)
    path.reverse()
    for state in path:
        if state == goal_state:
            print(state)
        else:
            print(state, " -> ", end="")

    print("cost:", cost)
