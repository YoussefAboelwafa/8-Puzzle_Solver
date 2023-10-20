from utils import *
import time

def dfs_solver(start_state, goal_state):
    stack = []
    explored = set()
    frontier_explored = set()
    parent = dict()
    stack.append(start_state)
    parent[start_state] = start_state
    nodes_expanded = 0

    while stack:
        curr = stack.pop()
        explored.add(curr)
        nodes_expanded += 1
        frontier_explored.add(curr)

        if curr == goal_state:
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded)

        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in frontier_explored:
                stack.append(neighbour)
                frontier_explored.add(neighbour)
                parent[neighbour] = curr

    return (False, "")


start_time = time.time()          
_, res, nodes_expanded = dfs_solver("867254301", "012345678")
end_time = time.time()
cost = res[0]
path = res[1]
print("Cost:", cost)
print("Nodes expanded:", nodes_expanded)
print("Time taken:", (end_time - start_time)*1000, "ms")
