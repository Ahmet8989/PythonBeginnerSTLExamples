# Value and reference types

# Value types -> string, number, float 
x = 5
y = 35
x = y 
y = 55
print(x,y)

# Refence types -> lists 

list_a = ['apple', 'banana', 'grape']
list_b = ['banana', 'mango', 'watermelon']
list_a = list_b
list_b[0] = 'carrot'
print(list_a)
print(list_b)
