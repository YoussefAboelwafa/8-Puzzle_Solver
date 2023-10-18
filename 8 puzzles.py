import queue
def getEmptyCell(state):
    for i in range(9):
        if state[i] == '0':
            return i
def swap(state, idx1, idx2):
   state_list = list(state)
   state_list[idx1], state_list[idx2] = state_list[idx2], state_list[idx1]
   return ''.join(state_list)

def getNeighbours(state):
    neighbours = []
    #todo empty cell
    emptyCell = getEmptyCell(state)
    if emptyCell % 3 != 0:
        neighbours.append(swap(state, emptyCell, emptyCell - 1))
    if emptyCell % 3 != 2:
        neighbours.append(swap(state, emptyCell, emptyCell + 1))
    if emptyCell // 3 != 0:
        neighbours.append(swap(state, emptyCell, emptyCell - 3))
    if emptyCell // 3 != 2:
        neighbours.append(swap(state, emptyCell, emptyCell + 3))
    return neighbours

def print_path(parent,goal_state):
  curr=goal_state
  cost=0
  path=[]
  while parent[curr]!=curr:
      path.append(curr)
      curr=parent[curr]
      cost+=1
  path.append(curr)
  path.reverse()
  for state in path:
        if state==goal_state:
            print(state)
        else:
         print(state," -> ",end='')
  
  print("cost:",cost)  

def bfs_solver(start_state,goal_state):
    fronteir=queue.Queue()
    explored=set()
    fronteir_explored=set()
    parent=dict()
    fronteir.put(start_state)
    parent[start_state]=start_state
    while not fronteir.empty():
        curr=fronteir.get()
        explored.add(curr)
        fronteir_explored.add(curr)
        if curr==goal_state:
            print_path(parent,goal_state)
            return True
        neighbours=getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in fronteir_explored:
                fronteir.put(neighbour)
                fronteir_explored.add(neighbour)
                parent[neighbour]=curr
    return False    

print(bfs_solver('647850321','012345678'))

        
    
   