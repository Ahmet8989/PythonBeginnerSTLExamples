# Assignment operators 

x, y, z = 5, 7, 9
print(x, y, z)
x, z = z, x
print(x, y, z)
x += 5 # x = x + 5
print(x, y, z)
x -= 5
print(x, y, z)
x *= 5
print(x, y, z)
x /= 5
x = int(x)
print(x, y, z)
x %= 5
print(x, y, z)
x += 5
print(x, y, z)
x //= 5
print(x, y, z)
x += 8
print(x, y, z)
x **= 8
print(x, y, z)

print('---------')

r,t,y = 5, 'Seven', True
print(r, t, y)
r, y = y, r
print(r, t, y)

print('---------')

values = 1, 2, 3
print(type(values))
x,y,z = values
print(type(x))
print(x,y,z)
values = 1, 2, 3, 4, 5
x,y,*z = values
print(type(x))
print(type(y))
print(type(z))
print(x,y,z)

# print('---------')

