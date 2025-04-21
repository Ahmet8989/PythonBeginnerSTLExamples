fruits = {'orange', 'apple', 'banana', 'lemon'}

print(fruits)
print(type(fruits))

# Sets can not be indexed, you can reach its elemenets with loops

for z in fruits: 
    print(z)

fruits.add('cherry')
print(fruits)
fruits.update(['mango', 'grape'])
print(fruits)
fruits.remove('mango')
print(fruits)
fruits.discard('orange')
print(fruits)
fruits.pop()
print(fruits)

# Inside the set, one elemenet exist only one time

my_list = [5, 5, 5, 5, 5,]
print(my_list)
my_new_list = set(my_list)
print(my_new_list)
my_new_list.clear()
print(my_new_list)
