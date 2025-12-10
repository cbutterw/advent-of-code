from shapely.geometry import Polygon, box
import matplotlib.pyplot as plt

def parse_input(lines: list[str]) -> list[tuple[int,int]]:
  return [tuple(map(int, l.split(','))) for l in lines]

def area(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
  x1,y1 = tile1
  x2,y2 = tile2
  return (abs(x1-x2)+1)*(abs(y1-y2)+1)

def green_area(floor: Polygon, tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
  x1,y1 = tile1
  x2,y2 = tile2
  rectangle = box(
    min(x1, x2), min(y1, y2),
    max(x1, x2), max(y1, y2)
  )
  if floor.contains(rectangle):
    x,y = rectangle.exterior.xy
    plt.plot(x,y)
    return area(tile1, tile2)
  return 0


def part_one(tiles: list[tuple[int,int]]) -> int:
  return max(area(a, b) for i, a in enumerate(tiles) for b in tiles[i+1:])

def part_two(tiles: list[tuple[int,int]]) -> int:
  floor = Polygon(tiles)
  area = max(green_area(floor, a, b) for i, a in enumerate(tiles) for b in tiles[i+1:])

  x,y = floor.exterior.xy
  plt.plot(x,y)
  plt.show()
  return area

def main() -> None:
  with open('09.in') as file:
    lines = [line.rstrip() for line in file]

  input = parse_input(lines)
  print('Part 1:', part_one(input))
  print('Part 2:', part_two(input))

if __name__ == '__main__':
  main()