import queue
import time
from utils import *


def bfs_solver(start_state, goal_state):
    frontier = queue.Queue()
    explored = set()
    frontier_explored = set()
    parent = dict()
    frontier.put(start_state)
    parent[start_state] = start_state
    nodes_expanded = 0

    while not frontier.empty():
        nodes_expanded += 1
        curr = frontier.get()
        explored.add(curr)
        frontier_explored.add(curr)
        if curr == goal_state:
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded)

        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in frontier_explored:
                frontier.put(neighbour)
                frontier_explored.add(neighbour)
                parent[neighbour] = curr

    return (False, "")
