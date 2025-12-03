with open('07.in') as textfile:
  lines = [line.rstrip() for line in textfile]

ranks = [('90', '1', '1')] * len(lines)
index = 0

for line in lines:
  hand = line.split()[0]
  value = line.split()[1]
  
  # Get hand type
  cardstmp = [*hand]
  replacements = {'2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09','T':'10', 'J':'11', 'Q':'12', 'K':'13', 'A':'14'}
  replacer = replacements.get
  cards = [replacer(n, n) for n in cardstmp]
  
  max_count = 0
  second_count = 0
  pair_check = '0'
  
  for card in cards:
    count = cards.count(card)
    if count >= max_count:
      if pair_check != card:
        second_count = max_count
      pair_check = card
      max_count = count
    elif count > second_count:
      second_count = count
  
  if max_count == 5:
    ranks[index] = (['96', *cards, value])
  elif max_count == 4:
    ranks[index] = (['95', *cards, value])
  elif max_count == 3:
    if second_count == 2:
      ranks[index] = (['94', *cards, value])
    else:
      ranks[index] = (['93', *cards, value])
  elif max_count == 2:
    if second_count >= 2:
      ranks[index] = (['92', *cards, value])
    else:
      ranks[index] = (['91', *cards, value])
  elif max_count == 1:
    ranks[index] = (['90', *cards, value])
  
  index += 1
  
ranked_hands = sorted(ranks)

total = 0
multiplier = 1

for hand in ranked_hands:
  total += multiplier * int(hand[-1])
  multiplier += 1


print (ranked_hands)
print (total)

# 251271168 too low
# 251941679 too high
# 251806792