import queue
from utils import *


def bfs_solver(start_state, goal_state):
    fronteir = queue.Queue()
    explored = set()
    fronteir_explored = set()
    parent = dict()
    fronteir.put(start_state)
    parent[start_state] = start_state

    while not fronteir.empty():
        curr = fronteir.get()
        explored.add(curr)
        fronteir_explored.add(curr)

        if curr == goal_state:
            print_path(parent, goal_state)
            return True

        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in fronteir_explored:
                fronteir.put(neighbour)
                fronteir_explored.add(neighbour)
                parent[neighbour] = curr

    return False
