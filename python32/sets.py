#Create an empty set
s = set()
#add elements to set
#no elemnt appears twice
s.add(1)
s.add(2)
s.add(3)
s.add(3)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements")