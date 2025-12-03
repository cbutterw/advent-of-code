with open('20231206.in') as textfile:
  lines = [line.rstrip() for line in textfile]

times = [int(''.join(lines[0].split()[1:]))]
dists = [int(''.join(lines[1].split()[1:]))]

print (times, dists)

tot = 1

for time, dist in zip(times, dists):
  ms = 1
  wins = 0
  while ms < time:
    speed = ms
    # print(dist, speed, time - ms)
    total_dist = speed * (time - ms)
    if total_dist > dist:
      wins += 1
    if total_dist < dist and wins > 0:
      print(total_dist, dist)
      break
    ms += 1
  
  # print(wins)
  tot *= wins

print(tot)