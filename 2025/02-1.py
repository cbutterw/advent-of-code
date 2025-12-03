with open("20250102.in", "r") as file:
  ids = file.readline().split(',')
  total = 0

  for id in ids:
    ranges = id.split('-')
    start = int(ranges[0])
    end = int(ranges[1])

    for i in range(start, end + 1):
      s = str(i)
      if len(s) % 2 != 0:
        continue
      firstHalf = s[:len(s)//2]
      secondHalf = s[len(s)//2:]

      if firstHalf == secondHalf:
        total += i

  print(total)