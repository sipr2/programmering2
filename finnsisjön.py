import random
import collections 

cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

random.shuffle(cards)

player_1_cards = []
player_2_cards = []
player_3_cards = []

for i in range(7):
    random_card = cards[0]
    player_1_cards.append(random_card)
    cards.pop(0)

for i in range(7):
    random_card = cards[0]
    player_2_cards.append(random_card)
    cards.pop(0)

for i in range(7):
    random_card = cards[0]
    player_3_cards.append(random_card)
    cards.pop(0)


print("Spelare 1:", player_1_cards)
print("spelare 2", player_2_cards)
print("Spelare 3", player_3_cards)


def check_cards ():
    player_1_counter = collections.Counter(player_1_cards)
    player_2_counter = collections.Counter(player_2_cards)
    player_3_counter = collections.Counter(player_3_cards)

    for card in player_1_counter:               
        if player_1_counter[card] == 4:
            player_1_cards.remove(card)
            player_1_cards.remove(card)
            player_1_cards.remove(card)
            player_1_cards.remove(card)

    for card in player_2_counter:               
        if player_2_counter[card] == 4:
            player_2_cards.remove(card)
            player_2_cards.remove(card)
            player_2_cards.remove(card)
            player_2_cards.remove(card)


    for card in player_3_counter:               
        if player_3_counter[card] == 4:
            player_3_cards.remove(card)
            player_3_cards.remove(card)
            player_3_cards.remove(card)
            player_3_cards.remove(card)
    
check_cards()

while True:
    while True:
        print("välj ett av dina kort", player_1_cards)
        card_choice = input ()
        print ("välj spelare att fråga ut")
        player_choice = input ()

        if player_choice == "2":
            if card_choice in player_2_cards:
                player_2_cards.remove (card_choice)
                player_1_cards.append (card_choice)
                print("Spelaren har kortet!")
            
            else: 
                random_card = cards[0]
                player_1_cards.append(random_card)
                cards.pop(0)
                print ("finns i sjön!")
                break


        elif player_choice == "3":
            if card_choice in player_3_cards:
                player_3_cards.remove (card_choice)
                player_1_cards.append (card_choice)
                print("Spelaren har kortet!")

            
            else: 
                random_card = cards[0]
                player_1_cards.append(random_card)
                cards.pop(0)
                print ("finns i sjön")
                break
        
        else:
            print("Vad håller du på med, idiot!")




    check_cards()

    while True:
            print("välj ett av dina kort", player_2_cards)
            card_choice = input ()
            print ("välj spelare att fråga ut")
            player_choice = input ()

            if player_choice == "3":
                if card_choice in player_3_cards:
                    player_3_cards.remove (card_choice)
                    player_2_cards.append (card_choice)
                    print("Spelaren har kortet!")
                
                else: 
                    random_card = cards[0]
                    player_2_cards.append(random_card)
                    cards.pop(0)
                    print ("finns i sjön!")
                    break


            elif player_choice == "1":
                if card_choice in player_1_cards:
                    player_1_cards.remove (card_choice)
                    player_2_cards.append (card_choice)
                    print("Spelaren har kortet!")

                
                else: 
                    random_card = cards[0]
                    player_2_cards.append(random_card)
                    cards.pop(0)
                    print ("finns i sjön")
                    break
            
            else:
                print("Vad håller du på med, idiot!")


    check_cards()


    while True:
        print("välj ett av dina kort", player_3_cards)
        card_choice = input ()
        print ("välj spelare att fråga ut")
        player_choice = input ()

        if player_choice == "2":
            if card_choice in player_2_cards:
                player_2_cards.remove (card_choice)
                player_3_cards.append (card_choice)
                print("Spelaren har kortet!")
            
            else: 
                random_card = cards[0]
                player_3_cards.append(random_card)
                cards.pop(0)
                print ("finns i sjön!")
                break


        elif player_choice == "1":
            if card_choice in player_1_cards:
                player_1_cards.remove (card_choice)
                player_3_cards.append (card_choice)
                print("Spelaren har kortet!")

            
            else: 
                random_card = cards[0]
                player_3_cards.append(random_card)
                cards.pop(0)
                print ("finns i sjön")
                break
        
        else:
            print("Vad håller du på med, idiot!")


            check_cards()
            


            
