with open("20250101.in", "r") as file:
  dial = 50
  count = 0

  for line in file:
    if line[0] == 'L':
      dial -= int(line[1:])
    else:
      dial += int(line[1:])

    dial %= 100
    if dial == 0:
      count += 1

  print(count)