# key - value

# 34 -> istanbul 

plakalar = {'kocaeli' : 41, 'istanbul' : 34}
print(plakalar['kocaeli'])
plakalar['ankara'] = 6
print(plakalar)

users = {
    'ST' : {
        'Age' : 36,
        'email' : 'st@gmail.com',
        'adress' : 'kocaeli',
        'phone' : 123123123,
        'roles' : ['user']
    },
    'CT' : {
        'Age' : 23,
        'email' : 'ct@gmail.com',
        'adress' : 'istanbul',
        'phone' : 456456456,
        'roles' : ['admin', 'user']
    }
}
print(users['ST'])
print(users['ST']['Age'])

students = {}

number = input("Student no: ")
name_2 = input("Student name: ")
surname = input("Student surname: ")

'''
This is first way
students[number] = {
    'ad' : name_2,
    'soyad' : surname
}
'''

# With update method we can add many students as we want

students.update({
    number : {
        'ad' : name_2,
        'soyad' : surname
    }
})

print(students)

studentNo = input('Student no: ')

print(students[studentNo])