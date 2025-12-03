f = open("20231202.in", "r")

tot = 0

for l in f:
  x = l.split(': ')
  game = int(x[0].split(' ')[1])
  draws = x[1].split('; ')
  
  rmax = 0
  gmax = 0
  bmax = 0
  
  for draw in draws:
    cubes = draw.split('\n')[0].split(', ')
    rcount = 0
    gcount = 0
    bcount = 0
    
    for cube in cubes:
      t = cube.split(' ')
      if t[1] == 'red':
        rcount += int(t[0])
      elif t[1] == 'green':
        gcount += int(t[0])
      elif t[1] == 'blue':
        bcount += int(t[0])
    
    if rcount > rmax:
      rmax = rcount
    if gcount > gmax:
      gmax = gcount
    if bcount > bmax:
      bmax = bcount
    
  tot += rmax * gmax * bmax
    
f.close()

print(tot)