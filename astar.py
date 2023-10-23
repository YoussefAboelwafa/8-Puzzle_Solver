import queue
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


# Define an A* search function
def astar(start_state, goal_state, heuristic):
    # Initialize a priority queue for A*, a dictionary to store parent-child relationships,
    # and other variables.
    frontier = queue.PriorityQueue()  # Priority Queue for A*
    parent = dict()  # Dictionary to store parent-child relationships
    frontier.put((0, start_state)) # Initialize the priority queue with a tuple (priority, start_state)
    parent[start_state] = start_state  # Set the start state as its own parent
    nodes_expanded = 0  # Counter for nodes expanded during search
    cost = dict() # Dictionary to store the cost to reach each state from the start state
    cost[start_state] = 0  # Set the cost to reach the start state as 0

    while not frontier.empty():
        # Increment the nodes expanded counter
        nodes_expanded += 1
        # Get the current state with the lowest priority from the priority queue
        curr = frontier.get()

        if curr[1] == goal_state:
            # If the current state is the goal state, print the path to the goal and return the result
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded, res[0])

        # Get the neighbors of the current state using a function called getNeighbours
        neighbours = getNeighbours(curr[1])

        for neighbour in neighbours:
            newcost = cost[curr[1]] + 1
            if neighbour not in cost or newcost < cost[neighbour]:
                # Calculate the priority based on the selected heuristic
                if heuristic == "manhattan":
                    priority = manhatan(neighbour, goal_state) + newcost
                else:
                    priority = eucledian(neighbour, goal_state) + newcost

                # Put the neighbor with its priority into the priority queue
                frontier.put((priority, neighbour))
                # Update the cost to reach the neighbor
                cost[neighbour] = newcost
                # Set the current state as the parent of the neighbor
                parent[neighbour] = curr[1]

    # If no solution is found, return a failure result
    return (False, "")
