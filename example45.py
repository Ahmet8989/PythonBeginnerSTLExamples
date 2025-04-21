# Range, 

for item in range(19):
    print(item)
print("-------------------------\n")
for item in range(5, 19):
    print(item)
print("-------------------------\n")
for item in range(5, 19, 3):
    print(item)
print("-------------------------\n")
print(list(range(5, 19, 3)))
print("-------------------------\n")

greeting = "Hello, hi, how are you?"
for letter in greeting:
    print(letter)
print("-------------------------\n")
for item in enumerate(greeting):
    print(item)
print("-------------------------\n")

# zip method -> it does matching
list_4 = [4, 5, 6, 7, 8, 9]
list_5 = ['a', 'b', 'c', 'd', 'e', 'f']
print(list(zip(list_4, list_5)))

for a,b in zip(list_4, list_5):
    print(a, b)
print("-------------------------\n")

print("-------------------------\n")