import random

lower_bound = 1
upper_bound = 100
number_of_guesses = 0

random_number = random.randint(lower_bound, upper_bound)

   

while True:
 

    try:
        guess = int(input("Guess the number: "))
    except KeyboardInterrupt:
        exit()
    except:
        print("Det där var int ett nummer!")
        continue

    if random_number == guess:
        print("Du gissade rätt!.")
        break
    elif random_number < guess:
        print("Talet är lägre!") 
    else:
        print("Talet är högre!")
        number_of_guesses += 1
 




 
   