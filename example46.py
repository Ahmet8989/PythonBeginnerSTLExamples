# List comprehension 

numbers   = [x for x in range(10)]
numbers_2 = [x**2 for x in range(10)]
numbers_3 = [x**2 for x in range(10) if x % 3 == 0]
myList    = [letter for letter in 'Hello World']
years     = [1983, 1984, 1985, 1986, 1987]
ages      = [2023 - year for year in years]
results   = [x if x % 2 == 0 else 'TEK' for x in range(10)]
numbers_4 = [(x, y, z) for x in range(10) for y in range(10) for z in range(10)]

print(numbers)
print("*******************\n")
print(numbers_2)
print("*******************\n")
print(numbers_3)
print("*******************\n")
print(myList)
print("*******************\n")
print(ages)
print("*******************\n")
print(results)
print("*******************\n")
print(numbers_4)
print("*******************\n")