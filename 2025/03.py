def part_one(lines):
  return max_joltage(lines, 2)

def part_two(lines):
  return max_joltage(lines, 12)

def max_joltage(lines, length):
  total = 0
  for line in lines:
    digits = [int(num) for num in line]
    index = 0

    for n in range(length):
      joltage = max(digits[index:len(digits)-(length-1-n)])
      # Use += since .index calculates from the beginning of the slice, not from the beginning of the list
      index += digits[index:].index(joltage) + 1
      total += joltage * 10**(length-1-n)

  return total


with open('03.in') as file:
  lines = [line.rstrip() for line in file]

print("Part 1:", part_one(lines))
print("Part 2:", part_two(lines))