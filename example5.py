name = "Ahmet"
length = len(name)
greeting = "Hello, my name is"

print(name[0])
print("---")
print(name[-1])
print("---")
print(name[length-1])
print("---")
print(greeting[3:5])
print("---")
print(greeting + " " + name)
print("---")
print(greeting[3:])
print("---")
print(greeting[:9])
print("---")
print(greeting[2:9:2]) # third parameter defines the selection intervals
print("---")
print(greeting + " {}".format(name))
print("---")
print("{} {}".format(greeting, name))
print("---")
print("{0} {1}".format(greeting, name))
print("---")
print("{1} {0}".format(greeting, name))
print("---")
print("{s} {g}".format(g = greeting, s = name))
print("---")
print("{} {} {} {} {}".format(name, name, name, name, name))
print("---")
result = 200/700
print(result)
print("The result is {r:10.4}".format(r = result))
print("---")
print(f"{greeting} {name}")
print("---")


website = "www.google.com"
course = "Python Course: Full Python Course Everything You Need"

# Solution 1

result = len(course)
print(result)
print("---")

# 2

cut = website[:3]
print(cut)
print("---")

# 3

cut4 = website[len(website)-3 : len(website)]
print(cut4)
print("---")

# 4

result4 = course[::-1]
print(result4)
print("---")

result5 = 'abc' * 5
print(result5)
print("---")

message = 'Hello there, my name is Ahmet'
print(message)
print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())
print(message.strip())
print(message.split())
print(message.split()[3])
result6 = message.split()
print('---'.join(result6))
print(message.find("Ahmet"))
print(message.center(100))
print(message.replace(" ", "*"))
print(message.count('l'))
print(message.index('l'))
print(message.isalpha())
print(message.isdigit())
