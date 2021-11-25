import random


  
random_number = random.randint(0, 9)

chances = 0

while chances < 5:
    number = int(input("Guess a number between 1 and 9: "))

    if random_number < number:
        print("Your Gues Was Too High: Guess A Number Lower than",number)
       # break
    elif random_number > number:
        print("Your Gues Was Too Low: Guess A Number Higher than",number)
       # break
    elif random_number == number:
        print("Congratulations YOU WON!!!")
        break
    
    chances+=1

if not chances < 5:
    print("YOU LOSE!!! The Number Is", random_number)