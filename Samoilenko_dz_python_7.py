
number = int(input("add number: "))
total = 0
while number > 0:
    total += number % 10
    number //= 10
print("Sum number:", total)

number = int(input("add number: "))
original = abs(number)
temp = original
reversed_num = 0
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
if original == reversed_num:
    print(f"Number {number} is a palindrome.")
else:
    print(f"Number {number} is not a palindrome.")

import random
print ("Greetings player, let's play a game of 'Guess the number'?\nGuess a number from 1 to 100. You have 10 tries.")
randomp = random.randint(1,100)
player = int(input("Your guess: "))
tryp = 9
while tryp > 0:
    if player == randomp:
        if tryp == 9:
            print ("Great intuition! You guessed it right on the first try!")
            break
        x = 10 - tryp
        print (f"Congratulations! You guessed the number: {randomp} in {x} attempts. Excellent result!")
        break
    elif player > randomp:
        tryp -= 1
        print (f"The guessed number is less than yours")
        player = int(input("Your guess: "))
    else:
        tryp -= 1
        print(f"The guessed number is greater than yours")
        player = int(input("Your guess: "))
print ("Game Over")
