from operator import le


my_list   = [4, 5, 6]
my_list_2 = ['Ahmet', 2, True, 2.3]
my_list_3 = ['one', 'two', 'three']
my_list_4 = ['four', 'five', 'six']
my_list_5 = my_list_3 + my_list_4
length = len(my_list_5)
print(f"List: {my_list_5}, Length: {length}")
my_list_6 = [my_list_3, my_list_4]
length2 = len(my_list_6)
print(f"List: {my_list_6}, Length: {length2}")
my_list_7 = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print(len(my_list_7))
print(my_list_7[0])
print(my_list_7[-1])
my_list_8 = my_list_7
my_list_8[3] = 'Toyota'
print(my_list_8)
print('Mercedes' in my_list_8)
print(my_list_8[-2])
print(my_list_8[0:3])
my_list_8[-2:] = ['Toyota', 'Renault']
'''
my_list_8[-2] = 'Toyota'
my_list_8[-1] = 'Renault'
'''
print(my_list_8)
my_list_8 += ['Nissan', 'Audi']
print(my_list_8)
del my_list_8[-1]
print(my_list_8)
print(my_list_8[::-1])

numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 'b', 'y', 's', 'a', 's']
val     = min(numbers)
val_2   = max(numbers)
val_3   = max(letters)
val_4   = min(letters)

print(val)
print(val_2)
print(val_3)
print(val_4)

numbers[4] = 40
print(numbers)
numbers.append(47)
print(numbers)
numbers.insert(3, 77)
print(numbers)
numbers.insert(-1, 53)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(4) # 4. indexteki elemani siler.
print(numbers)
numbers.remove(9) # Degeri 9 olan elemani siler. 
print(numbers)

numbers.sort()
letters.sort()
print(numbers)
print(letters)

numbers.reverse()
letters.reverse()

print(numbers)
print(letters)
print(len(letters))
print(numbers.count(10))

index = letters.index('y')
print(index)

result = 'y' in letters
print(result)

