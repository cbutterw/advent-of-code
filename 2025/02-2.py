with open("02.in", "r") as file:
  ids = file.readline().split(',')
  total = 0
  invalidIds = []

  def hasPattern(s, chunkSize, numChunks):
    return s.count(s[:chunkSize]) == numChunks

  for id in ids:
    ranges = id.split('-')
    start = int(ranges[0])
    end = int(ranges[1])

    for i in range(start, end + 1):
      s = str(i)

      for n in range(2, len(s)+1):
        if len(s) % n == 0:
          if hasPattern(s, int(len(s)/n), n):
            total += i
            invalidIds.append(i)
            break

  print(total)
  #print(invalidIds)