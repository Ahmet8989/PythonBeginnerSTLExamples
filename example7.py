tuple = (3, 'iki', True)

print(type(tuple))
print(tuple[2])
print(len(tuple))

tuple = ('Sally', 'Jane') 

# We can do this, we can rewrite the tuple, but we can not do the addition 

# We can not do this -> tuple[0] = 'Sally'

print(tuple)

names = ('Rowan', 'Sandy', 'Kathrine') + tuple

print(names)
