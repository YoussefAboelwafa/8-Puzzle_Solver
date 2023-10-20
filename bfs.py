import queue
import time
from utils import *


def bfs_solver(start_state, goal_state):
    fronteir = queue.Queue()
    explored = set()
    fronteir_explored = set()
    parent = dict()
    fronteir.put(start_state)
    parent[start_state] = start_state
    nodes_expanded = 0

    while not fronteir.empty():
        curr = fronteir.get()
        explored.add(curr)
        fronteir_explored.add(curr)
        nodes_expanded += 1
        if curr == goal_state:
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded)

        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in fronteir_explored:
                fronteir.put(neighbour)
                fronteir_explored.add(neighbour)
                parent[neighbour] = curr

    return (False, "")


start_time = time.time()          
_, res, nodes_expanded = bfs_solver("867254301", "012345678")
end_time = time.time()
cost = res[0]
path = res[1]
print("Cost:", cost)
print("Nodes expanded:", nodes_expanded)
print("Time taken:", (end_time - start_time)*1000, "ms")
