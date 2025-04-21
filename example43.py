# while loop

x = 3
while x < 57:
    print(x)
    x += 1
print("----------------------------\n")

name = ' ' 
while not name.strip():
    name = (input("Please enter your name: "))

print(f"Hello, {name}")
print("----------------------------\n")

# Solution of questions 

numbers = [1, 3, 5, 7, 9, 12, 13, 19, 23, 34]

# Answer 1

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
print("----------------------------\n")

# Answer 2 

start  = int(input("Start: "))
finish = int(input("Finish: "))

while start <= finish:
    if(start % 2 != 0):
        print(start)
    start += 1
print("----------------------------\n")


# Answer 3

number_5 = 100

while number_5 >= 1:
    print(number_5)
    number_5 -= 1
print("----------------------------\n")

# Answer 4

numbers_6 = []
number_6 = 0
i = 0

while i < 5:
    number_6 = int(input("Please enter a number: "))
    numbers_6.append(number_6)
    i += 1
numbers_6.sort()
print(numbers_6)
print("----------------------------\n")

# Answer 5

product_number = int(input("Enter product number: "))
i = 0
products = []

while i < product_number:
    product_name = input("Product Name: ")
    product_price = int(input("Product Price: "))
    products.append({
        'Product Name' : product_name,
        'Product Price' : product_price
    })
    i += 1
i = 0
while i < 3:
    print(products[i])
    i += 1

