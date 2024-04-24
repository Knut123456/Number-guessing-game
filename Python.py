from random import randint
import time

min = 1
max = 10
upgrade = 10


answer = randint(min, max)

input_number = int(input("Guess a number between 1 and 10: "))


check = True 
while check == True:
    if input_number == answer:
        print("Congratulations! You guessed the correct number.")
        check = False
        time.sleep (2)
        upgrade_random = randint(1, 5)
        upgrade = upgrade * upgrade_random
        max = max * upgrade
        answer = randint(min, max)
        input_number = int(input("Guess a number between " + str(min) +  " and "  +  str(max ) + ": " ))
    elif input_number < answer:
        input_number = int(input ("you guess is too low try again. "))
    elif input_number > answer:
        input_number = int (input ("your guess is high try again. "))



