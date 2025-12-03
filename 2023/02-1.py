f = open("20231202.in", "r")

rmax = 12
gmax = 13
bmax = 14

gametot = 0

for l in f:
  x = l.split(': ')
  game = int(x[0].split(' ')[1])
  draws = x[1].split('; ')
  isgood = True
  
  for draw in draws:
    cubes = draw.split('\n')[0].split(', ')
    rcount = 0
    gcount = 0
    bcount = 0
    print ("CUBES")
    print(cubes)
    for cube in cubes:
      t = cube.split(' ')
      if t[1] == 'red':
        rcount += int(t[0])
      elif t[1] == 'green':
        gcount += int(t[0])
      elif t[1] == 'blue':
        bcount += int(t[0])
    
    if rcount > rmax or gcount > gmax or bcount > bmax:
      isgood = False
    
    print("Game")
    print (game)
    print(rcount)
    print(gcount)
    print(bcount)
  
  if isgood:
    gametot += game
    
f.close()

print(gametot)