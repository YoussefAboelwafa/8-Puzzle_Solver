import time
from bfs import *
from dfs import *
from astar import *
from utils import *

RED = "\033[91m"
RESET = "\033[0m"

start_state = "806547231"
goal_state = "012345678"

if is_solvable(start_state):
    start_time1 = time.time()
    _, res, nodes_expanded, search_depth = bfs_solver(start_state, goal_state)
    end_time1 = time.time()
    cost = res[0]
    path = res[1]
    print(RED + "BFS" + RESET)
    print("Cost:", cost)
    print("Nodes expanded:", nodes_expanded)
    print("Search depth:", search_depth)
    print("Time taken:", (end_time1 - start_time1) * 1000, "ms")
    print("-------------------------------------------")

    # ---------------------------------------------------------------------------

    start_time2 = time.time()
    _, res, nodes_expanded, search_depth = dfs_solver(start_state, goal_state)
    end_time2 = time.time()
    cost = res[0]
    path = res[1]
    print(RED + "DFS" + RESET)
    print("Cost:", cost)
    print("Nodes expanded:", nodes_expanded)
    print("Search depth:", search_depth)
    print("Time taken:", (end_time2 - start_time2) * 1000, "ms")
    print("-------------------------------------------")

    # ---------------------------------------------------------------------------

    start_time3 = time.time()
    _, res, nodes_expanded, search_depth = astar(start_state, goal_state, "manhatan")
    end_time3 = time.time()
    cost = res[0]
    path = res[1]
    print(RED + "A* (Manhatan)" + RESET)
    print("Cost:", cost)
    print("Nodes expanded:", nodes_expanded)
    print("Search depth:", search_depth)
    print("Time taken:", (end_time3 - start_time3) * 1000, "ms")
    print("-------------------------------------------")

    # ---------------------------------------------------------------------------

    start_time4 = time.time()
    _, res, nodes_expanded, search_depth = astar(start_state, goal_state, "eucledian")
    end_time4 = time.time()
    cost = res[0]
    path = res[1]
    print(RED + "A* (Eucledian)" + RESET)
    print("Cost:", cost)
    print("Nodes expanded:", nodes_expanded)
    print("Search depth:", search_depth)
    print("Time taken:", (end_time4 - start_time4) * 1000, "ms")
    print("-------------------------------------------")

else:
    print(RED + "Not solvable" + RESET)
