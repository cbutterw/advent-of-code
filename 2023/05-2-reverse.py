def is_map(value, source, destination, length):
  if value >= int(source) and value < int(source) + int(length):
    return True
  return False

with open('20231205.in') as textfile:
  lines = [line.rstrip() for line in textfile]

seeds = lines[0].split()[1::2]
ranges = list(map(int, lines[0].split()[2::2]))

print (seeds)
print (ranges)

fileindex = 0

seedtosoil = []
soiltofert = []
ferttowat = []
wattolight = []
lighttotemp = []
temptohumid = []
humidtoloc = []

for line in lines:
  splitline = line.split()
  if 'map:' in splitline:
    fileindex += 1
    continue
    
  if not splitline:
    continue
  
  if fileindex == 1:
    seedtosoil.append(splitline)
  elif fileindex == 2:
    soiltofert.append(splitline)
  elif fileindex == 3:
    ferttowat.append(splitline)
  elif fileindex == 4:
    wattolight.append(splitline)
  elif fileindex == 5:
    lighttotemp.append(splitline)
  elif fileindex == 6:
    temptohumid.append(splitline)
  elif fileindex == 7:
    humidtoloc.append(splitline)
  else:
    print("AHHHHHHHHHH!", splitline)

index = 0
  
while index < 199728751:
  location = index
  mapped_value = index
  if (index + location) % 100000 == 0:
    print("iter: ", index, mapped_value)
  for row in humidtoloc:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[1]) + mapped_value - int(row[0])
      break
  for row in temptohumid:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[1]) + mapped_value - int(row[0])
      break
  for row in lighttotemp:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[1]) + mapped_value - int(row[0])
      break
  for row in wattolight:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[1]) + mapped_value - int(row[0])
      break
  for row in ferttowat:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[1]) + mapped_value - int(row[0])
      break
  for row in soiltofert:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[1]) + mapped_value - int(row[0])
      break
  for row in seedtosoil:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[1]) + mapped_value - int(row[0])
      break
  
  seedindex=0
  for seed in seeds:
    if mapped_value >= int(seed) and mapped_value < int(seed)+ranges[seedindex]:
      print (location) # 37384986
      exit()
    seedindex += 1
  
  index += 1
print ("NOOOO")