import random
alternatives =["Sten", "Sax", "Påse"]
user_points = 0 
computer_points = 0
while user_points <3 and computer_points <3:

    user_choice = input ("Välj ett alternativ (Sten, Sax, Påse)")
    computer_choice = random.choice(alternatives)

    r = random.choice(alternatives)





    if user_choice == computer_choice:
        print(f" Båda valde {user_choice}. Det blev lika!")
    elif user_choice == "Sten":
        if computer_choice == "Sax":
            print("Sten vinner över sax! du vinner!")
            user_points += 1

        else:
            print("Påse tar Sten! Du förlorar.")
            computer_points += 1
    elif user_choice == "Påse":
        if computer_choice == "Sten":
            print("Påse tar Sten! Du vinner!")
            user_points += 1
        else:
            print("Sax tar Påse! Du förlorar.")
            computer_points += 1
    elif user_choice == "Sax":
        if computer_choice == "Påse":
            print("Sax tar Påse! Du vinner!")
            user_points += 1
        else:
            print("Sten tar Sax! Du förlorar.")
            computer_points += 1
    
    print(f"Player Score: {user_points} Computer Score: {computer_points}")

  
if user_points == 3: 
    print ("Du vinner!")
if computer_points ==3:
    print ("Du förlorar")