from utils import *


# Define a depth-first search solver function
def dfs_solver(start_state, goal_state):
    # Initialize the stack for DFS, sets for tracking explored and frontier nodes,
    # a dictionary to store parent-child relationships, and other variables.
    stack = []  # Stack for DFS
    explored = set()  # Set to track explored nodes
    frontier_explored = set()  # Set to track nodes in the frontier
    parent = dict()  # Dictionary to store parent-child relationships
    stack.append(start_state)  # Initialize the stack with the start state
    parent[start_state] = start_state  # Set the start state as its own parent
    nodes_expanded = 0  # Counter for nodes expanded during search
    max_depth = 0  # Variable to keep track of the maximum depth reached
    cost_so_far = dict()  # Dictionary to store the cost to reach each state from the start state
    cost_so_far[start_state] = 0  # Set the cost to reach the start state as 0

    while stack:
        # Increment the nodes expanded counter
        nodes_expanded += 1
        # Pop the current state from the stack
        curr = stack.pop()
        # Add the current state to the explored set
        explored.add(curr)
        # Add the current state to the frontier_explored set
        frontier_explored.add(curr)

        if curr == goal_state:
            # If the current state is the goal state, print the path to the goal and return the result
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded, max_depth)

        # Get the neighbors of the current state using a function called getNeighbours
        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in frontier_explored:
                # Calculate the cost to reach the neighbor from the current state
                cost_so_far[neighbour] = cost_so_far[curr] + 1
                # Update the maximum depth if the current depth is greater
                if cost_so_far[neighbour] > max_depth:
                    max_depth = cost_so_far[neighbour]
                # Push the neighbor onto the stack
                stack.append(neighbour)
                # Add the neighbor to the frontier_explored set
                frontier_explored.add(neighbour)
                # Set the current state as the parent of the neighbor
                parent[neighbour] = curr

    # If no solution is found, return a failure result
    return (False, "")
