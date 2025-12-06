def parse_input(lines):
  idx = lines.index('')
  fresh = lines[:idx]
  available = lines[idx+1:]

  return fresh, available

def part_one(lines):
  fresh, available = parse_input(lines)
  count = 0

  for a in available:
    n = int(a)
    for f in fresh:
      values = f.split('-')
      if int(values[0]) <= n <= int(values[1])+1:
        count += 1
        break
  return count
  

def part_two(lines):
  fresh = parse_input(lines)[0]
  pairs = [list(map(int, f.split('-'))) for f in fresh]
  pairs.sort()
  count = 0

  for p1, p2 in zip(pairs[:-1], pairs[1:]):
    if p1[1] >= p2[1]:
      p2[0] = -1 # flag to ignore this later
      p2[1] = p1[1] # use this to adjust the next pair
    elif p1[1] >= p2[0]:
      p2[0] = p1[1] + 1 # move the beginning
    
    if (p1[0] != -1):
      count += p1[1] - p1[0] + 1
  
  # add last pair, which isn't captured in the loop above
  if (-1 != pairs[-1][0] and pairs[-1][0] <= pairs[-1][1]):
    count += pairs[-1][1] - pairs[-1][0] + 1

  return count


with open('05.in') as file:
  lines = [line.rstrip() for line in file]

print('Part 1:', part_one(lines))
print('Part 2:', part_two(lines))