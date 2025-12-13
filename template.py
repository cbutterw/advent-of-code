def parse_input(lines: list[str]):
  return 0


def part_one(lines: list[str]) -> int:
  return 'not yet implemented'

def part_two(lines: list[str]) -> int:
  return 'not yet implemented'

def main() -> None:
  with open('00.in') as file:
    lines = [line.rstrip() for line in file]

  input = parse_input(lines)
  print('Part 1:', part_one(input))
  print('Part 2:', part_two(input))

if __name__ == '__main__':
  main()