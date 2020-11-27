import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
com_cards = []
user_cards = []
def dealing(card) : 
    """shuffling card and pick up 1 card"""
    card = random.choice(cards)
    return card

def calculate_score(dealed_card) : 
    """special condition when calculate scores"""
    if sum(dealed_card) == 21 and len(dealed_card) == 2 :
        return 0
    elif sum(dealed_card) > 21 and 11 in dealed_card :
        dealed_card.append(1)
        dealed_card.remove(11)
        return sum(dealed_card)
    else :
        return sum(dealed_card)    

def victory_condition() :
    """victory conditions"""
    if calculate_score(user_cards) == 0 and calculate_score(com_cards) == 0 :
        print("\nit draws.")
    elif calculate_score(user_cards) == 0 :
        print("\nyou win. and you've got blackjack!")
    elif calculate_score(com_cards) == 0 :
        print("\ncomputer wins. and it has got blackjack!")
    else : 
        if calculate_score(user_cards) > 21 and calculate_score(com_cards) > 21 :
            print("\nit draws")    
        elif calculate_score(user_cards) > 21 :
            print("\ncomputer wins. your score is over 21.")
        elif calculate_score(com_cards) > 21 :
            print("\nuser win. computer's score is over 21.")
        elif calculate_score(com_cards) == calculate_score(user_cards) : 
            print("\nit draws.")     
        elif calculate_score(com_cards) > calculate_score(user_cards) : 
            print("\ncomputer wins!")
        elif calculate_score(com_cards) < calculate_score(user_cards) : 
            print("\nyou win!")      
        print(f"my final deck is {user_cards}. point is {calculate_score(user_cards)}")
        print(f"computer's final deck is {com_cards}. point is {calculate_score(com_cards)}")      

        
def pick_up_card(card) :
    """pick 2 computer's cards and 2 user's cards. and show the current deck up"""
    for _ in range(2) :
        com_cards.append(dealing(card))
        user_cards.append(dealing(card))
    com_sumup = calculate_score(com_cards)
    user_sumup = calculate_score(user_cards)
    print(f"my current deck is {user_cards}. point is {user_sumup}")
    print(f"computer's first card is [{com_cards[0]}].")

def go_ahead_or_not(card) : 
    """organizing conditions to keep running the game or not"""
    switch_go_ahead_or_not = True
    while switch_go_ahead_or_not : 
        if calculate_score(com_cards) == 0 or calculate_score(user_cards) == 0 :
            switch_go_ahead_or_not = False
            victory_condition()     
        elif calculate_score(com_cards) > 21 or calculate_score(user_cards) > 21 :
            switch_go_ahead_or_not = False
            victory_condition()    
        else :
            ask_go_or_not = input("do you want to go ahead?? plz answer Y or N : ").upper()
            if ask_go_or_not == "N" :
                switch_go_ahead_or_not = False
                victory_condition()
            elif ask_go_or_not == "Y" :
                com_cards.append(dealing(card))
                user_cards.append(dealing(card))
                com_sumup = calculate_score(com_cards)
                user_sumup = calculate_score(user_cards)
                print(f"my current deck is {user_cards}. point is {user_sumup}")
                print(f"computer's first card is [{com_cards[0]}].")


dealing(cards)
pick_up_card(cards)
go_ahead_or_not(cards)
