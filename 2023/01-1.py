f = open("20231201.in", "r")

tot = 0

for l in f:
  s = ""
  for c in l:
    if c in '0123456789':
      s = s+c
  s = s[0] + s[len(s) - 1]
  tot += int(s)
  print(s)

f.close()

print(tot)