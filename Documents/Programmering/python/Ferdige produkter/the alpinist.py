import numpy as np
import math
import heapq

maze = "\n".join([
  "112",
  "010",
  "410",
])
def make_a_traversal_list(maze_length, maze_array):
  traversalList = [[math.inf for i in range (maze_length)] for i in range (maze_length)]
  traversalList[0][0] = 0
  return traversalList
            
def string_to_array(a):
  liste = []
  for element in a:
      if element == "\n":
          continue
      else:
          liste.append(int(element))
  length = int(math.sqrt(len(liste)))
  arrayen = np.array(liste)
  arrayen = np.reshape(arrayen,(length,length))
  return arrayen, length

maze_array, maze_length = string_to_array(maze)
values_of_nodes = make_a_traversal_list(maze_length, maze_array)
print(maze_length)

def bfs(maze_array, maze_length):
  start = (0,0)
  goalX = goalY = int(maze_length-1)
  queue = [(0,start,[(0,0)])]
  # print(queue)
  heapq.heapify(queue)
  # seen = set([start])
  while queue:
    # print("kø: ", queue)
    lowestPath = heapq.heappop(queue)
    # print(lowestPath)
    cost, node, path = lowestPath
    x,y = node
    if x == y == goalX == goalY:
      return values_of_nodes[maze_length-1][maze_length-1], path
    for x2,y2 in ((x+1,y), (x-1,y), (x,y+1),(x,y-1)):
        cost_for_neighbour = cost
        path_for_neighbour = path
        if 0 <= x2 < maze_length and 0 <= y2 < maze_length:
          cost_for_neighbour = cost_for_neighbour + abs(maze_array[x2][y2] - maze_array[x][y])
          print("cost-----", (x,y),(x2,y2), abs(maze_array[x2][y2] - maze_array[x][y]))
          if cost_for_neighbour < values_of_nodes[x2][y2]:
              path_for_neighbour = path_for_neighbour + [(x2,y2)]
              values_of_nodes[x2][y2] = cost_for_neighbour
              queue.append((cost_for_neighbour, (x2,y2), path_for_neighbour))
              print(values_of_nodes)
              print("path:",  path)
    print("---------------")

value_of_last_node, path = bfs(maze_array, maze_length)
print("Lowest cost from node 1 to last node: ", value_of_last_node, path)