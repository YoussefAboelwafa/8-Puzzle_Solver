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
    max_depth = 0
    cost_so_far = dict()
    cost_so_far[start_state] = 0

    while stack:
        nodes_expanded += 1
        curr = stack.pop()
        explored.add(curr)
        frontier_explored.add(curr)

        if curr == goal_state:
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded, max_depth)

        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in frontier_explored:
                cost_so_far[neighbour] = cost_so_far[curr] + 1
                if cost_so_far[neighbour] > max_depth:
                    max_depth = cost_so_far[neighbour]
                stack.append(neighbour)
                frontier_explored.add(neighbour)
                parent[neighbour] = curr

    return (False, "")
