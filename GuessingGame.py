import random

number = int(input("Guess a number between 1 and 9: "))
  
random_number = random. randint(0, 9)

while chances < 5:
    if random_number > number:
        print("Your Gues Was Too High: Guess A Number Lower than",number)
        break
    else if random_number < number:
        print("Your Gues Was Too Low: Guess A Number Higher than",number)
    else:
        print("Congratulations YOU WON!!!")

if not chances < 5:
    print("YOU LOSE!!! The Number Is", number)