# Required if the grid is going to be modified
def input_to_grid(lines):
  grid = []
  for line in lines:
    grid.append(list(line))
  return grid

def is_in_grid(grid, x, y):
  if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x]):
    return True
  return False

def adjacency(grid, x, y, target):
  count = 0
  directions = []
  locations = []
  for m,n in [(x+i,y+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
    if is_in_grid(grid, m, n):
      if grid[m][n] == target:
        count += 1
        directions.append((m-x, n-y))
        locations.append((m, n))
  return count, directions, locations

def adjacent_in_direction(grid, x, y, target, direction):
  if is_in_grid(grid, x+direction[0], y+direction[1]):
    return target == grid[x+direction[0]][y+direction[1]]
  
def get_values(grid, x, y, positions):
  values = []
  for p in positions:
    if is_in_grid(grid, x+p[0], y+p[1]):
      values.append(grid[x+p[0]][y+p[1]])
  return values

def debug(grid, x, y):
  print(grid[x-1][y-1], grid[x-1][y], grid[x-1][y+1])
  print(grid[x][y-1], grid[x][y], grid[x][y])
  print(grid[x+1][y-1], grid[x+1][y], grid[x+1][y+1])
