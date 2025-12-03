f = open("20231201.in", "r")

tot = 0

for l in f:
  s = ""
  l = l.lower()
  l = l.replace("one", "o1e")
  l = l.replace("two", "t2o")
  l = l.replace("three", "thr3e")
  l = l.replace("four", "fo4r")
  l = l.replace("five", "f5ve")
  l = l.replace("six", "s6x")
  l = l.replace("seven", "se7en")
  l = l.replace("eight", "ei8ht")
  l = l.replace("nine", "n9ne")
  
  for c in l:
    if c in '123456789':
      s = s+c
  s = s[0] + s[len(s) - 1]
  tot += int(s)
  # print(s)

f.close()

print(tot)