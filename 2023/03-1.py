with open('20231203.in') as textfile:
  grid = [line.rstrip() for line in textfile]

digits = '0123456789'
nonsym = '0123456789.'

x=y=tot=0

while y < len(grid):
  while x < len(grid[0]):
    if grid[y][x] == '.':
      x += 1
      continue

    numlen = 0
    while x < len(grid[0]) and grid[y][x] in digits:
      # First digit in a number. How long is it?
      numlen += 1
      x += 1
    
    if numlen > 0:
      num = grid[y][x-numlen:x]
      print ("num: " , num)

      xstart = x-numlen-1
      if xstart < 0:
        xstart = 0
      xend = x+1
      if xend > len(grid[0]):
        xend = len(grid[0])
      ystart = y-1
      if ystart < 0:
        ystart = 0
      yend = y+2
      if yend > len(grid):
        yend = len(grid)
      # print(xstart, xend, ystart, yend)
      
      ispart = False
      
      for j in range(ystart, yend):
        for i in range(xstart, xend):
          #print(grid[j][i])
          if grid[j][i] not in nonsym:
            ispart = True
      
      if ispart:
        tot += int(num)
        #print(num, tot)
        #print(num, numlen, xstart, xend, ystart, yend, x, y)

    x += 1
  y += 1
  x = 0

print(tot)