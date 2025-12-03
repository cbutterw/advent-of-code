def part_one(lines):
  pattern = lines[0]
  
  tree = {}
  
  # Load tree
  for line in lines[2::]:
    node = line.split(' = ')[0]
    coords = line.split(' = ')[1].strip('()')
    left = coords.split(', ')[0]
    right = coords.split(', ')[1]
    tree[node] = (left, right)
    
  # Traverse tree
  index = 0
  node = "AAA"
  while index < 100000:
    step = pattern[index % len(pattern)]
    
    if step == 'L':
      node = tree[node][0]
    elif step == 'R':
      node = tree[node][1]
    
    index += 1
    if node == "ZZZ":
      return index
    
  return "Nope"

def part_two(lines):
  pattern = lines[0]
  
  tree = {}
  nodes = []
  
  # Load tree
  for line in lines[2::]:
    node = line.split(' = ')[0]
    coords = line.split(' = ')[1].strip('()')
    left = coords.split(', ')[0]
    right = coords.split(', ')[1]
    tree[node] = (left, right)
    if node.endswith('A'):
      nodes.append(node)
    
  # Traverse tree
  index = 0
  loops = [(False, False, 0, '')] * len(nodes)
  while index < 100000:
    step = pattern[index % len(pattern)]
    
    for i, n in enumerate(nodes):
      #print(index, nodes[i])
      if step == 'L':
        nodes[i] = tree[n][0]
      elif step == 'R':
        nodes[i] = tree[n][1]
      
      if n.endswith('Z') and not loops[i][0] and not loops[i][1]:
        loops[i] = (True, False, 0, n)
        
      if loops[i][0] and not loops[i][1]:
        if loops[i][2] > 0 and n == loops[i][3]:
          loops[i] = (True, True, loops[i][2], loops[i][3])
        else:
          loops[i] = (True, False, loops[i][2] + 1, loops[i][3])
    
    index += 1
    
    values = []
    included = 0
    for l in loops:
      if l[1]:
        values.append(l[2])
        included += 1
    
    if included == len(loops):
      print (loops)
      return lcm(values)
    
  print (loops)
  return "Nope"

def lcm(values):
  x = values[1]
  if len(values) > 2:
    x = lcm(values[1::])
  y = values[0]
  print (x, y)
  
  return (x*y)//gcd(x,y)
  
def gcd(x, y):
  while(y):
    x, y = y, x % y
  return x

with open('08.in') as textfile:
  lines = [line.rstrip() for line in textfile]

print("Part 1:", part_one(lines))

print("Part 2:", part_two(lines))

# 591389029402879128960 (off by 1 error...)
#        14616363770447