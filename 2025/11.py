def parse_input(lines: list[str]) -> dict[str, list[str]]:
  deviceIO = {}
  for line in lines:
    input, output = map(str.strip, line.split(':'))
    deviceIO[input] = output.split()
  return deviceIO

def count_paths(deviceIO: dict[str, list[str]], node: str, end: str, memo: set[str]) -> int:
  if node in memo:
    return memo[node]
  paths = 0
  for n in deviceIO[node]:
    if n == end:
      return 1
    paths += count_paths(deviceIO, n, end, memo)
  memo[node] = paths
  return paths

def part_one(deviceIO: dict[str, list[str]]) -> int:
  # fix for part 2 sample data
  if 'you' not in deviceIO:
    deviceIO['you'] = ['out']
  return count_paths(deviceIO, 'you', 'out', {})

def part_two(deviceIO: dict[str, list[str]]) -> int:
  deviceIO['out'] = []
  return (
          count_paths(deviceIO, 'svr', 'fft', {})
          * count_paths(deviceIO, 'fft', 'dac', {})
          * count_paths(deviceIO, 'dac', 'out', {})
  )

def main() -> None:
  with open('11.in') as file:
    lines = [line.rstrip() for line in file]

  input = parse_input(lines)
  print('Part 1:', part_one(input))
  print('Part 2:', part_two(input))

if __name__ == '__main__':
  main()