import queue
import time
from utils import *
def manhtan(state, goal):
    cost = 0
    for i in range(9):
        if state[i] != "0":
            cost += abs(i % 3 - goal.index(state[i]) % 3) + abs(i // 3 - goal.index(state[i]) // 3)
    return cost

def eucledian(state, goal):
    cost = 0
    for i in range(9):
        if state[i] != "0":
            cost += ((i % 3 - goal.index(state[i]) % 3)**2 + (i // 3 - goal.index(state[i]) // 3)**2)**0.5
    return cost

def astar(start_state,goal_state,heuristic):
  frontier = queue.PriorityQueue()
  explored = set()
  frontier_explored = set()
  parent = dict()
  frontier.put((0,start_state))
  parent[start_state] = start_state
  nodes_expanded=0
  cost=0
  while not frontier.empty():
      curr=frontier.get()
      explored.add(curr[1])
      frontier_explored.add(curr[1])
      nodes_expanded+=1
      if curr[1]==goal_state:
          res=print_path(parent,goal_state)
          return (True,res,nodes_expanded)
      neighbours=getNeighbours(curr[1])
      for neighbour in neighbours:
            cost+=1
            if neighbour not in frontier_explored:
                if heuristic=="manhtan":
                    frontier.put((manhtan(neighbour,goal_state)+cost,neighbour))
                else:
                    frontier.put((eucledian(neighbour,goal_state)+cost,neighbour))
                frontier_explored.add(neighbour)
                parent[neighbour]=curr[1]    
  return (False,"")  

start_time = time.time()          
_, res, nodes_expanded = astar("182043765", "012345678","eculidean")
end_time = time.time()
cost = res[0]
path = res[1]
print("Cost:", cost)
print("Nodes expanded:", nodes_expanded)
print("Time taken:", (end_time - start_time)*1000, "ms")