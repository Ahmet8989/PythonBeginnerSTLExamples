# Break, Continue statements 

name = 'Jonathan'

for letter in name:
    if(letter == 'a'):
        continue
    print(letter)
print("------------------------\n")

for letter in name:
    if(letter == 'a'):
        pass
    print(letter)
print("------------------------\n")

for letter in name:
    if(letter == 'a'):
        break
    print(letter)
print("------------------------\n")