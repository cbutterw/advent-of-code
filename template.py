def part_one(lines: list[str]) -> int:
  return 'not yet implemented'


def part_two(lines: list[str]) -> int:
  return 'not yet implemented'

def main() -> None:
  with open('00.in') as file:
    lines = [line.rstrip() for line in file]

  print('Part 1:', part_one(lines))
  print('Part 2:', part_two(lines))

if __name__ == '__main__':
  main()