def part_one(lines):
  tachyons = [x == 'S' for x in lines[0]]
  splits = 0
  for line in lines[1:]:
    for idx, (l, t) in enumerate(zip(line, tachyons)):
      if t and l == '^':
        tachyons[idx-1] = True
        tachyons[idx] = False
        tachyons[idx+1] = True
        splits += 1

  return splits


def part_two(lines):
  timelines = [int(x == 'S') for x in lines[0]]
  for line in lines[1:]:
    for idx, l in enumerate(line):
      if l == '^':
        timelines[idx-1] += timelines[idx]
        timelines[idx+1] += timelines[idx]
        timelines[idx] = 0

  return sum(timelines)


with open('07.in') as file:
  lines = [line.rstrip() for line in file]

print('Part 1:', part_one(lines))
print('Part 2:', part_two(lines))