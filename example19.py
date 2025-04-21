# for loop

numbers = [4, 5, 6, 7, 8, 9]

for number in numbers:
	print(number)
print("***************************\n")

for i in range(len(numbers)):
	print(f"Index: {i}, number: {numbers[i]}")
print("***************************\n")

name = "Jonathan"
for letter in name:
	print(letter)
print("***************************\n")

tuple_a = ((3,5), (4,6), (4,7), (5,6), (5,7))
for t,l in tuple_a:
	print(t,l)
print("***************************\n")

tuple_a = ((3,5), (4,6), (4,7), (5,6), (5,7))
for t,l in tuple_a:
	print(t)
print("***************************\n")

d = {'key_1' : "value_1", 'kay_2' : "value_2", 'key_3' : "value_3"}

for item in d:
	print(item)
print("***************************\n")

for item in d.items():
	print(item)
print("***************************\n")

for key,value in d.items():
	print(key)
print("***************************\n")

for key,value in d.items():
	print(value)
print("***************************\n")

for key,value in d.items():
	print(key, value)
print("***************************\n")




# SOLUTION OF QUESTIONS

# Answer 1

numbers_2 = [1, 3, 5, 7, 9, 12, 13, 19, 23, 34]
count = 0
numbers_three = []
for number in numbers_2:
	if(number % 3 == 0):
		print(number)
print("***************************\n")

# Answer 2

total = 0

for number in numbers_2:
	total += number
print(total)
print("***************************\n")

#Answer 3

for number in numbers_2:
	if(number % 2 !=0):
		print(number ** 2)
print("***************************\n")

#Answer 4

cities = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

for city in cities:
	if(len(city) <= 5):
		print(city)
print("***************************\n")

#Answer 5

products = [
	{'Name' : 'Samsung S6', 'Price' : '3000'},
	{'Name' : 'Samsung S7', 'Price' : '4000'},
	{'Name' : 'Samsung S8', 'Price' : '5000'},
	{'Name' : 'Samsung S9', 'Price' : '6000'},
	{'Name' : 'Samsung S10', 'Price' : '7000'}
]
totall = 0

for product in products:
	totall += int(product['Price'])
print(totall)
print("***************************\n")

#Answer 6

for product in products:
	if(int(product['Price']) <= 5000):
		print(product['Name'])
print("***************************\n")

