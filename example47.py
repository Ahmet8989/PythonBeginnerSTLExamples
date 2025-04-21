# Number guessing with random module

import random

value = random.randint(1, 100)
chance = 5
point = 100

new_chance = int(input("Chance: "))
minus = (point/new_chance)
i = 0

while (i < new_chance):
    guess = int(input("Value: "))
    if(guess == value):
        print(f"Congrats! You win! You have {point} points!")
        break
    else:
        point -= (minus)
        i += 1
        isLower = guess < value
        if(isLower):
            print(f"You have {point} points left. Guess again: (but upper, hssss)")
        else:
            print(f"You have {point} points left. Guess again: (but lower, hssss)")
        if(i == new_chance):
            print(f"Sorry mon ami, the value was {value}")
