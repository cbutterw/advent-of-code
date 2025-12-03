with open('20231204.in') as textfile:
  lines = [line.rstrip() for line in textfile]

tot = index = 0
copies = [1] * len(lines)

for l in lines:
  line = l.split(": ")
  nums = line[1].split(" | ")
  wins = [x for x in nums[0].split(" ") if x.strip()]
  picks = [x for x in nums[1].split(" ") if x.strip()]
  correct = 0
  
  numcards = copies[index]
  index += 1
  
  for pick in picks:
    if pick in wins:
      if index + correct < len(lines):
        copies[index + correct] += numcards
        correct += 1
      else:
        print(index, correct, index+correct, len(lines))
  

tot = sum(copies)
print(tot)
