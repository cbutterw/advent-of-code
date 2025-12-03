def is_map(value, destination, source, length):
  if value >= int(source) and value < int(source) + int(length):
    return True
  return False

with open('20231205.in') as textfile:
  lines = [line.rstrip() for line in textfile]
  
min_loc = 9999999999999

seeds = lines[0].split()[1:]

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


for seed in seeds:
  #print (seed)
  mapped_value = int(seed)
  
  for row in seedtosoil:
    #     value, destination, source, range
    if is_map(mapped_value, row[0], row[1], row[2]):
      #        destination + value - source
      mapped_value = int(row[0]) + mapped_value - int(row[1])
      break
  
  for row in soiltofert:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[0]) + mapped_value - int(row[1])
      break
  
  for row in ferttowat:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[0]) + mapped_value - int(row[1])
      break
      
  for row in wattolight:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[0]) + mapped_value - int(row[1])
      break
  
  for row in lighttotemp:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[0]) + mapped_value - int(row[1])
      break
      
  for row in temptohumid:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[0]) + mapped_value - int(row[1])
      break
  
  for row in humidtoloc:
    if is_map(mapped_value, row[0], row[1], row[2]):
      mapped_value = int(row[0]) + mapped_value - int(row[1])
      break
      
  # print (mapped_value, min_loc)
  if mapped_value < min_loc:
    min_loc = mapped_value
    
print (min_loc)