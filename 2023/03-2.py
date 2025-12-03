def find_number(grid, x, y):
  digits = '0123456789'
  num = grid[y][x]
  
  if grid[y][x+1] in digits:
    num += grid[y][x+1]
    if grid[y][x+2] in digits:
      num += grid[y][x+2]
      if grid[y][x+3] in digits:
        num += grid[y][x+3]
  
  if grid[y][x-1] in digits:
    num = grid[y][x-1] + num
    if grid[y][x-2] in digits:
      num = grid[y][x-2] + num
      if grid[y][x-3] in digits:
        num = grid[y][x-3] + num
  return num


with open('20231203.in') as textfile:
  grid = ['.' + line.rstrip() + '.' for line in textfile]

dotstr = '.' * len(grid[0])
grid.insert(0, dotstr)
grid.append(dotstr)

# print (grid)

digits = '0123456789'
gear = '*'
count=0
x=y=tot=0

while y < len(grid):
  while x < len(grid[0]):
    # print (x, y)
    if grid[y][x] != '*':
      x += 1
      continue

    count += 1
    num_list = []
    
    if grid[y-1][x-1] in digits:
      num_list.append(find_number(grid, x-1, y-1))
    if grid[y-1][x] in digits:
      num_list.append(find_number(grid, x, y-1))
    if grid[y-1][x+1] in digits:
      num_list.append(find_number(grid, x+1, y-1))
      
    if grid[y][x-1] in digits:
      num_list.append(find_number(grid, x-1, y))
    if grid[y][x+1] in digits:
      num_list.append(find_number(grid, x+1, y))
    
    if grid[y+1][x-1] in digits:
      num_list.append(find_number(grid, x-1, y+1))
    if grid[y+1][x] in digits:
      num_list.append(find_number(grid, x, y+1))
    if grid[y+1][x+1] in digits:
      num_list.append(find_number(grid, x+1, y+1))
    
    # print(count, tot)
    # hack - hoping that the same number doesn't show up more than once... (540 does)
    nums = list(dict.fromkeys(num_list))
    if len(nums) == 2:
      tot += int(nums[0]) * int(nums[1])
    else:
      print(nums)
    
    x += 1
  y += 1
  x = 0

print(tot + 540*540)