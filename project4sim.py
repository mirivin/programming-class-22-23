from random import randint
counter = 0
roll = randint(1,6)
print("would you like to roll the die?")
answer = input("Enter yes or no: ") 
if answer == "yes": 
    while roll != 6:
        roll = randint (1,6)
        counter = counter + 1
    if roll == 6:
        print(counter)
        print("^ this is how many tries it took to roll a 6!")
        if counter <= 3:
            print("you had some good luck this round! restart to play again")
        else:
            print("your luck wasnt that good this round. restart to try again")

else: 
    print("For my sake, please enter yes.")
    
