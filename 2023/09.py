def lower_poly (seq):
  new_poly = []
  i = 1
  
  while i < len(seq):
    new_poly.append(seq[i] - seq[i-1])
    i += 1
  
  return new_poly

def part_one(lines):
  total = 0

  for line in lines:
    seqs = [list(map(int, line.split()))]
    
    while set(seqs[-1]) != {0}:
      seqs.append(lower_poly(seqs[-1]))
    
    # print (seqs)
    
    for seq in seqs:
      total += seq[-1]
    
  return total

def part_two(lines):
  total = 0

  for line in lines:
    seqs = [list(map(int, line.split()))]
    
    while set(seqs[-1]) != {0}:
      seqs.append(lower_poly(seqs[-1]))
    
    # print (seqs)
    
    for n, seq in enumerate(seqs):
      if n % 2 == 0:
        total += seq[0]
      elif n % 2 == 1:
        total -= seq[0]
  
  return total

with open('09.in') as textfile:
  lines = [line.rstrip() for line in textfile]

print("Part 1:", part_one(lines))

print("Part 2:", part_two(lines))
