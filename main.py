from utils import *
from bfs import bfs_solver
from dfs import dfs_solver

start_state = "123456780"
goal_state = "012345678"

if is_solvable(start_state):
    bfs_solver(start_state, goal_state)
else:
    print("Unsolvable")

# dfs_solver(start_state, goal_state)