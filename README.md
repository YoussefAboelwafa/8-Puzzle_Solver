# 8 Puzzle Solver

8 Puzzle Solver Using Classical Search Algorithms: DFS | BFS | A\*

## Deployment

- To Run Graphical Interface:

```bash
 python main.py
```

- To Run The Test File to Compare Different Algorithms:

## Data Structure Used

### DFS &rarr; Stack as frontier to store states

### BFS &rarr; Queue as frontier to store states

### A\* &rarr; Priority Queue as frontier to store states

## Algorithms Used

### BFS

```python
def bfs_solver(start_state, goal_state):
    frontier = queue.Queue()
    explored = set()
    frontier_explored = set()
    parent = dict()
    frontier.put(start_state)
    parent[start_state] = start_state
    nodes_expanded = 0

    while not frontier.empty():
        nodes_expanded += 1
        curr = frontier.get()
        explored.add(curr)
        frontier_explored.add(curr)
        if curr == goal_state:
            res = print_path(parent, goal_state)
            return (True, res, nodes_expanded, res[0])

        neighbours = getNeighbours(curr)
        for neighbour in neighbours:
            if neighbour not in frontier_explored:
                frontier.put(neighbour)
                frontier_explored.add(neighbour)
                parent[neighbour] = curr

    return (False, "")
```

### DFS

```python
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
```

### A\*

```python
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
```

#### Heuristic Functions

- The heuristic functions are used in A\* search to give a priority to each state to make the "probably" best state to be explored first.

##### Manhattan Distance

- It is the sum of absolute values of differences in the goal’s x and y coordinates and the current cell’s x and y coordinates respectively, the function value for each state is done through a simple function

```python
def manhatan(state, goal):
    cost = 0
    for i in range(9):
        if state[i] != "0":
            cost += abs(i % 3 - goal.index(state[i]) % 3) + abs(
                i // 3 - goal.index(state[i]) // 3
            )
    return cost
```

##### Euclidean Distance

- It is the distance between the current cell and the goal cell using the following formula
- The value of Euclidean Distance function for each state is done through this function

```python
def eucledian(state, goal):
    cost = 0
    for i in range(9):
        if state[i] != "0":
            cost += (
                (i % 3 - goal.index(state[i]) % 3) ** 2
                + (i // 3 - goal.index(state[i]) // 3) ** 2
            ) ** 0.5
    return cost
```

##### Which One is better?

- Both of the heuristic functions used are admissible, but we want to know which one of them is better and more effiecient
- According to the analysis done in [Analysis Section](#analysis-for-different-algorithms), Manhatten Distance is a better admissible function at it expands less number of states than Euclidean Distance. That will result in making the values of Manhatten Distance function values closer to the optimal function much more than the Euclidean Distance.

## Analysis for Different Algorithms.

- For the following random test case:
<table align="center">
  <tr>
    <td>7</td>
    <td>6</td>
    <td>2</td>
  </tr>
  <tr>
    <td>8</td>
    <td>5</td>
    <td>3</td>
  </tr>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>4</td>
  </tr>
</table>

- To reach the goal state:

<table align="center">
  <tr>
    <td>0</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4</td>
    <td>5</td>
  </tr>
  <tr>
    <td>6</td>
    <td>7</td>
    <td>8</td>
  </tr>
</table>
<table align="center">
  <tr>
    <th>Algorithm</th>
    <th>Cost of Path</th>
    <th>Nodes Expanded</th>
    <th>Search Depth</th>
    <th>Running time</th>
  </tr>
  <tr>
    <td>BFS</td>
    <td>22</td>
    <td>83130</td>
    <td>22</td>
    <td>377 ms</td>
  </tr>
  <tr>
    <td>DFS</td>
    <td>64674</td>
    <td>107462</td>
    <td>66488</td>
    <td>304 ms</td>
  </tr>
  <tr>
    <td>A* Manhattan</td>
    <td>22</td>
    <td>263</td>
    <td>22</td>
    <td>1 ms</td>
  </tr>
  <tr>
    <td>A* Euclidean</td>
    <td>22</td>
    <td>816</td>
    <td>22</td>
    <td>15 ms</td>
  </tr>
</table>

## Graphical Interface
