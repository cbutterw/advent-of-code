from grid import input_to_grid, adjacency

def part_one(lines):
  grid = input_to_grid(lines)
  adjacent = 0
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y] == '@' and adjacency(grid, x, y, '@')[0] < 4:
        adjacent += 1
  return adjacent

def part_two(lines):
  grid = input_to_grid(lines)
  count = 0
  prevCount = -1

  while prevCount != count:
    prevCount = count
    for x in range(len(grid)):
      for y in range(len(grid[x])):
        if grid[x][y] == '@' and adjacency(grid, x, y, '@')[0] < 4:
          grid[x][y] = 'x'
    count = sum(s.count('x') for s in grid)
  return count


with open('04.in') as file:
  lines = [line.rstrip() for line in file]

print("Part 1:", part_one(lines))
print("Part 2:", part_two(lines))