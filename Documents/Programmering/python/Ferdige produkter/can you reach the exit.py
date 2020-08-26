import numpy as np
import math

maze = "\n".join([
  "...",
  ".W.",
  "..."
])
def string_to_array(a):
  liste = []
  for element in a:
      if element == "\n":
          continue
      else:
          liste.append(element)
  length = int(math.sqrt(len(liste)))
  arrayen = np.array(liste)
  arrayen = np.reshape(arrayen,(length,length))
  return arrayen, length

maze_array, maze_length = string_to_array(maze)
directions = [[0,1],[1,0],[0,-1],[-1,0]]
print(maze_length)

def bfs(maze_array, maze_length):
  start = (0,0)
  goalX = goalY = int(maze_length-1)
  queue = ([[start]])
  seen = set([start])
  while queue:
    print("kø: ", queue)
    path = queue.pop(0)
    x,y = path[-1]
    if x == y == goalX == goalY:
      return path
    for x2,y2 in ((x+1,y), (x-1,y), (x,y+1),(x,y-1)):
      print(x2,y2)
      if 0 <= x2 < maze_length and 0 <= y2 < maze_length and maze_array[x][y] != "W" and (x2,y2) not in seen:
        queue.append(path + [(x2,y2)])
        seen.add((x2,y2))
    print("---------------")
print(bfs(maze_array, maze_length))







