with open("01.in", "r") as file:
  dial = 50
  count = 0

  for line in file:
    rot = int(line[1:])

    previousDial = dial
    if line[0] == 'L':
      dial -= rot
    else:
      dial += rot

    dial %= 100

    count += rot // 100
    if dial == 0 and previousDial == 0:
      count += 0
    elif dial == 0:
      count += 1
    elif previousDial == 0:
      count += 0
    elif line[0] == 'L' and previousDial - (rot % 100) < 0:
      count += 1
    elif line[0] == 'R' and previousDial + (rot % 100) > 100:
      count += 1

  print(count)