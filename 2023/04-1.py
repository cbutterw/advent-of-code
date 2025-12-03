f = open("20231204.in", "r")

tot = 0

for l in f:
  line = l.split(": ")
  nums = line[1].split(" | ")
  wins = [x.strip() for x in nums[0].split(" ") if x.strip()]
  picks = [x.strip() for x in nums[1].split(" ") if x.strip()]
  correct = 0
  
  
  for pick in picks:
    if pick in wins:
      #print(pick, wins)
      correct += 1
  
  if correct > 0:
    #print(tot, correct, pow(2, correct-1))
    tot += pow(2, correct-1)
    
    
print(tot)