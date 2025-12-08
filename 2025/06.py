import numpy

def operate(params, operation):
  match operation:
    case '*':
      return numpy.prod(params, dtype='uint64')
    case '+':
      return sum(params)

def part_one(lines):
  inputs = [[int(num) for num in l.split()] for l in lines[:-1]]
  operations = lines[-1].split()
  problems = numpy.rot90(inputs, k=3)
  return int(sum(operate(p, o) for p, o in zip(problems, operations)))
  

def part_two(lines):
  inputs = [list(l) for l in lines[:-1]]
  grid = numpy.rot90(inputs, k=1)
  numbers = [''.join(num).strip() for num in grid]
  problem = []
  problems = []
  for n in numbers:
    if (n == ''):
      problems.append(problem)
      problem = []
    else:
      problem.append(int(n))
  problems.append(problem)
  operations = lines[-1].split()[::-1]
  
  return int(sum(operate(p, o) for p, o in zip(problems, operations)))


with open('06.in') as file:
  lines = [line.rstrip('\n') for line in file]

print('Part 1:', part_one(lines))
print('Part 2:', part_two(lines))