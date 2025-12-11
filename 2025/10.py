import itertools
from collections import deque
import pulp 

BIG_NUMBER = 10000

def parse_input(lines: list[str]) -> tuple[list[str], list[list[list[int]]], list[list[int]]]:
  lights = []
  buttons = []
  joltages = []
  for line in lines:
    light, *button, joltage = line.split()
    lights.append([c == '#' for c in light.strip('[]')])
    buttons.append([list(map(int, b.strip('()').split(','))) for b in button])
    joltages.append(list(map(int, joltage.strip('{}').split(','))))
  return lights, buttons, joltages

def toggle_lights(target: list[bool], button_combos: tuple[list[int]]):
  lights = [False]*len(target)
  for bc in button_combos:
    for b in bc:
      lights[b] ^= True
  
  if target == lights:
    return len(button_combos)
  return BIG_NUMBER

# This does not work. It can find inefficient paths, save them in the state, and then it never gets recalculated.
def increase_joltage_dfs(target: list[int], joltage: list[int], button_list: list[list[int]], iter: int, memo: dict):
  state_tuple = tuple(joltage)
  if state_tuple in memo:
      return memo[state_tuple]

  if any(j > t for j,t in zip(joltage, target)) or iter >= BIG_NUMBER:
    return BIG_NUMBER
  if joltage == target:
    return iter
  
  presses = BIG_NUMBER
  for bl in button_list:
    new_joltage = joltage.copy()
    for b in bl:
      new_joltage[b] += 1
    count = increase_joltage_dfs(target, new_joltage, button_list, iter+1, memo)
    if count < presses:
      presses = count
  memo[state_tuple] = presses
  return presses

# This might work if given enough time and RAM. 
def increase_joltage_bfs(target: list[int], button_list: list[list[int]]) -> int:
  queue = deque([([0]*len(target), 0)])
  visited = set()

  while queue:
    current_joltage, presses = queue.popleft()
    if current_joltage == target:
      return presses
    
    state_tuple = tuple(current_joltage)
    if state_tuple in visited:
      continue
    visited.add(state_tuple)

    for bl in button_list:
      new_joltage = current_joltage.copy()
      for b in bl:
        new_joltage[b] += 1
      
      if all(j <= t for j, t in zip(new_joltage, target)):
        queue.append((new_joltage, presses + 1))

def increase_joltage_ilp(target: list[int], button_list: list[list[int]]) -> int:
  matrix = [[0]*len(button_list) for _ in range(len(target))]
  for j, buttons in enumerate(button_list):
    for i in buttons:
      matrix[i][j] = 1
  problem = pulp.LpProblem("Minimize Button Presses", pulp.LpMinimize)
  vars = [pulp.LpVariable(f'x_{i}', lowBound=0, cat='Integer') for i in range(len(button_list))]
  problem += pulp.lpSum(vars)
  for i in range(len(target)):
    problem += pulp.lpSum(matrix[i][j] * vars[j] for j in range(len(button_list))) == target[i]
  problem.solve()
  return int(sum(v.value() for v in vars))


def part_one(input: tuple[list[str], list[list[list[int]]], list[list[int]]]) -> int:
  target_lights, buttons, _ = input
  presses = 0
  for target, button_list in zip(target_lights, buttons):
    button_combos = []
    for r in range(0, len(button_list)):
      button_combos.extend(itertools.combinations(button_list, r+1))
    presses += min(toggle_lights(target, bc) for bc in button_combos)
  return presses

def part_two(input: tuple[list[str], list[list[list[int]]], list[list[int]]]) -> int:
  _, buttons, joltages = input
  presses = 0
  for i, (button_list, target) in enumerate(zip(buttons, joltages)):
    print(i, target)
    #presses += increase_joltage_dfs(target, [0]*len(target), button_list, 0, {})
    #presses += increase_joltage_bfs(target, button_list)
    presses += increase_joltage_ilp(target, button_list)
  return presses

def main() -> None:
  with open('10.in') as file:
    lines = [line.rstrip() for line in file]

  input = parse_input(lines)
  print('Part 1:', part_one(input))
  print('Part 2:', part_two(input))

if __name__ == '__main__':
  main()