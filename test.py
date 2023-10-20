import time
from bfs import *
from dfs import *
from astar import *

RED = "\033[91m"
RESET = "\033[0m"

start_time1 = time.time()
_, res, nodes_expanded = bfs_solver("867254301", "012345678")
end_time1 = time.time()
cost = res[0]
path = res[1]
print(RED + "BFS" + RESET)
print("Cost:", cost)
print("Nodes expanded:", nodes_expanded)
print("Time taken:", (end_time1 - start_time1) * 1000, "ms")
print("-------------------------------------------")

# ---------------------------------------------------------------------------

start_time2 = time.time()
_, res, nodes_expanded = dfs_solver("867254301", "012345678")
end_time2 = time.time()
cost = res[0]
path = res[1]
print(RED + "DFS" + RESET)
print("Cost:", cost)
print("Nodes expanded:", nodes_expanded)
print("Time taken:", (end_time2 - start_time2) * 1000, "ms")
print("-------------------------------------------")

# ---------------------------------------------------------------------------

start_time3 = time.time()
_, res, nodes_expanded = astar("182043765", "012345678", "manhatan")
end_time3 = time.time()
cost = res[0]
path = res[1]
print(RED + "A* (Manhatan)" + RESET)
print("Cost:", cost)
print("Nodes expanded:", nodes_expanded)
print("Time taken:", (end_time3 - start_time3) * 1000, "ms")
print("-------------------------------------------")

# ---------------------------------------------------------------------------

start_time4 = time.time()
_, res, nodes_expanded = astar("182043765", "012345678", "Eucledian")
end_time4 = time.time()
cost = res[0]
path = res[1]
print(RED + "A* (eucledian)" + RESET)
print("Cost:", cost)
print("Nodes expanded:", nodes_expanded)
print("Time taken:", (end_time4 - start_time4) * 1000, "ms")
