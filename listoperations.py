num=[6,11,14,21,24]
print(min(6,14,11,24,21))
print(max(6,14,11,24,21))
print(min(num))
del num
places=['paris','coorg','manali']
print(places)
places.append(24)
print(places)
places.insert(3,11)
print(places)
otherplaces=['delhi','goa','bali']
places.extend(otherplaces)
print("all places are",places)
print(places[2:5])
print(places[-5:-2])
