# Identitiy operator -> is 

x = y = [4, 5, 6]
z = [4, 5, 5]

result   = (x == y)
result_2 = (x == z)
result_3 = (x is y) # There is an adress comparison here
result_4 = (x is z) # There is an adress comparison here
result_5 = (x is not z) # There is an adress comparison here

print(result, result_2, result_3, result_4, result_5)

# Membership operator -> in 

fruits = ['apple', 'banana', 'grape']
print('apple' in fruits)
print('a' not in (fruits))
