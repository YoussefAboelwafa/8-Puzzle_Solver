import queue
import time
from utils import *


def manhatan(state, goal):
    cost = 0
    for i in range(9):
        if state[i] != "0":
            cost += abs(i % 3 - goal.index(state[i]) % 3) + abs(
                i // 3 - goal.index(state[i]) // 3
            )
    return cost


def eucledian(state, goal):
    cost = 0
    for i in range(9):
        if state[i] != "0":
            cost += (
                (i % 3 - goal.index(state[i]) % 3) ** 2
                + (i // 3 - goal.index(state[i]) // 3) ** 2
            ) ** 0.5
    return cost


def astar(start_state, goal_state, heuristic):
    frontier = queue.PriorityQueue()
    parent = dict()
    frontier.put((0, start_state))
    parent[start_state] = start_state
    nodes_expanded = 0
    cost = dict()
    cost[start_state] = 0

    while not frontier.empty():
        nodes_expanded += 1
        curr = frontier.get()
        if curr[1] == goal_state:
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded, res[0])
        neighbours = getNeighbours(curr[1])

        for neighbour in neighbours:
            newcost = cost[curr[1]] + 1
            if neighbour not in cost or newcost < cost[neighbour]:
                if heuristic == "manhatan":
                    priority = manhatan(neighbour, goal_state) + newcost
                else:
                    priority = eucledian(neighbour, goal_state) + newcost

                frontier.put((priority, neighbour))
                cost[neighbour] = newcost
                parent[neighbour] = curr[1]

    return (False, "")
