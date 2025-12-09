import math

def get_distance(x1:int, y1:int, z1:int, x2:int, y2:int, z2:int) -> int:
  return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def get_ordered_connections(lines):# -> dict_keys:
  positions = [tuple(map(int, l.split(','))) for l in lines]
  distances = {}
  for i, p1 in enumerate(positions):
    for j, p2 in enumerate(positions[i+1:]):
      distances[(i,j+i+1)] = get_distance(*p1, *p2)
  return dict(sorted(distances.items(), key=lambda x: x[1])).keys()

def find_circuits(circuits: list[set], connections:list[set]) -> list[set]:
  for conn in connections:
    add_connection(circuits, conn)

  while connections != circuits:
    return find_circuits([], circuits)
  return circuits

def add_connection(circuits:list[set], connection:set) -> list[set]:
  circuit = next((c for c in circuits if not connection.isdisjoint(c)), None)
  if circuit:
    circuit.update(connection)
  else:
    circuits.append(connection)
  return circuits


def part_one(connections) -> int:
  # 10 for test data, 1000 otherwise
  sets = [set(key) for key in list(connections)[:1000]]
  circuits = find_circuits([], sets)
  circuits.sort(key=len, reverse=True)
  return math.prod([len(c) for c in circuits[:3]])

def part_two(connections, lines) -> int:
  sets = [set(key) for key in list(connections)]
  circuits = []
  for s in sets:
    find_circuits(circuits, [s])
    if len(circuits[0]) == len(lines):
      return int(lines[s.pop()].split(',')[0]) * int(lines[s.pop()].split(',')[0])
  return 0

def main() -> None:
  with open('08.in') as file:
    lines = [line.rstrip() for line in file]

  connections = get_ordered_connections(lines)
  print('Part 1:', part_one(connections))
  print('Part 2:', part_two(connections, lines))

if __name__ == '__main__':
  main()