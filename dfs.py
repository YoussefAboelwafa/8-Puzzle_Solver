from utils import *


def dfs_solver(start_state, goal_state):
    stack = []
    explored = set()
    frontier_explored = set()
    parent = dict()
    stack.append(start_state)
    parent[start_state] = start_state

    while stack:
        curr = stack.pop()
        explored.add(curr)
        frontier_explored.add(curr)

        if curr == goal_state:
            print_path(parent, goal_state)
            return True

        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in frontier_explored:
                stack.append(neighbour)
                frontier_explored.add(neighbour)
                parent[neighbour] = curr

    return False