import datetime

if True:
    print("Welcome")

user_name = "ST"
password = 456456

entered_user_name = input("User Name: ")
entered_password = int(input("Password: "))

isLoggedin = (user_name == entered_user_name) and (password == entered_password)

if isLoggedin:
    print("Welcome")

num = int(input("Please enter a number: "))
if (num > 0):
    print("Nmuber is positive")
elif (num < 0):
    print("Number is negative")
else:
    print("Number equals to zero")

date_ref = input("Year of vehicle (yyyy/mm/dd): ")
date_ref = date_ref.split("/")
date = datetime.datetime(int(date_ref[0]), int(date_ref[1]), int(date_ref[2]))
current_date = datetime.datetime.now()
diff = (current_date - date)
print(f"Your vehicle on the roads roughly about {diff.days}")
