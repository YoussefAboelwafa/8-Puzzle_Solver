import queue
from utils import *


# Define a breadth-first search solver function
def bfs_solver(start_state, goal_state):
    # Initialize a queue for BFS, sets for tracking explored and frontier nodes,
    # a dictionary to store parent-child relationships, and other variables.
    frontier = queue.Queue()  # Queue for BFS
    explored = set()  # Set to track explored nodes
    frontier_explored = set()  # Set to track nodes in the frontier
    parent = dict()  # Dictionary to store parent-child relationships
    frontier.put(start_state)  # Initialize the queue with the start state
    parent[start_state] = start_state  # Set the start state as its own parent
    nodes_expanded = 0  # Counter for nodes expanded during search

    while not frontier.empty():
        # Increment the nodes expanded counter
        nodes_expanded += 1
        # Get the current state from the front of the queue
        curr = frontier.get()
        # Add the current state to the explored set
        explored.add(curr)
        # Add the current state to the frontier_explored set
        frontier_explored.add(curr)

        if curr == goal_state:
            # If the current state is the goal state, print the path to the goal and return the result
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded, res[0])

        # Get the neighbors of the current state using a function called getNeighbours
        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in frontier_explored:
                # Push the neighbor onto the queue
                frontier.put(neighbour)
                # Add the neighbor to the frontier_explored set
                frontier_explored.add(neighbour)
                # Set the current state as the parent of the neighbor
                parent[neighbour] = curr

    # If no solution is found, return a failure result
    return (False, "")
