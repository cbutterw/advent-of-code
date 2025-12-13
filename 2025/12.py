def parse_input(lines: list[str]) -> tuple[dict[int, list[list[str]]], list[tuple[str, list[int]]]]:
  presents = {}
  regions = []
  shape = []

  for line in lines:
    if line.endswith(':'):
      shape = []
      presents[int(line[:-1])] = shape
    
    elif line and line[0] in '#.':
      shape.append(line)
    
    elif ':' in line:
      dimension, values = line.split(':')
      values = list(map(int, values.split()))
      regions.append((dimension, values))
  return presents, regions

def get_bounds(presents: dict[int, list[list[str]]], region: tuple[str, list[int]]):
  dimensions = tuple(map(int, region[0].split('x')))
  area = dimensions[0] * dimensions[1]
  quantities = region[1]

  size = 0
  nines = 0
  for i, q in enumerate(quantities):
    size += q * sum(p.count('#') for v in presents[i] for p in v)
    nines += q * 9
  return (nines <= area, size <= area)

def part_one(presents: dict[int, list[list[str]]], regions: list[tuple[str, list[int]]]) -> tuple[int, int]:
  bounds = tuple(map(sum, zip(*(get_bounds(presents, r) for r in regions))))
  return bounds

def part_two() -> str:
  return '*'

def main() -> None:
  with open('12.in') as file:
    lines = [line.rstrip() for line in file]

  input = parse_input(lines)
  print('Part 1:', part_one(*input))
  print('Part 2:', part_two())

if __name__ == '__main__':
  main()