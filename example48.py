# Prime Number Example 

value = int(input("Please enter a number: "))

i = 2 
isMatched = False

while (i < value):
    if(value % i == 0):
        print(f"The number you entered ({value}), is not a prime number")
        isMatched = True
        break
    break

if(not(isMatched)):
    print(f"The number you entered ({value}), is prime number")