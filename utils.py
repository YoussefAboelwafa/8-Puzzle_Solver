def is_solvable(state):
    flatten = list(state)
    puzzle = [flatten[0:3], flatten[3:6], flatten[6:9]]
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return inv_count % 2 == 0


def getInvCount(arr):
    inv_count = 0
    empty_value = "0"
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


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
    # arr=[]
    # for state in path:
    #     arr.append(state)
    #     if state == goal_state:
    #         flatten = list(state)
    #         mat = [flatten[0:3], flatten[3:6], flatten[6:9]]
    #         for row in mat:
    #             for col in row:
    #                 print(col, end="|")
    #             print()
    #         print("-------")
    #     else:
    #         flatten = list(state)
    #         mat = [flatten[0:3], flatten[3:6], flatten[6:9]]
    #         for row in mat:
    #             for col in row:
    #                 print(col, end="|")
    #             print()
    #         print("-------")

    return (cost, path)

   