import random

LIFE_SWITCH = True
easy_life = 10
hard_life = 5

number_list = list(range(1,101))
com_picked_no = random.choice(number_list)

def difficulty_choice() :
    print("Let's play a number guessing game! \nrule : choose a number between 1~100. \nIf you match the computer's number, you win")
    difficulty = input("plz choose a difficulty. if you want hard mode, input 'hard', if you wnat easy mode, input 'easy' \n")
    if difficulty == "easy" :
        return easy_life
    elif difficulty == "hard" :
        return hard_life

remained_life = difficulty_choice()


def win_lose_condition() :
    global LIFE_SWITCH
    if user_picked_no == com_picked_no :
        print(f"You win. Computer's number is <{com_picked_no}>")
        LIFE_SWITCH = False
    elif remained_life == 0 :
        LIFE_SWITCH = False
        print(f"You lose. Computer's number is <{com_picked_no}>")

def number_check() :    
    if user_picked_no > com_picked_no :
        print(f"<{user_picked_no}> is too high")
    elif user_picked_no < com_picked_no :
        print(f"<{user_picked_no}> is too low")

def life_subtract() :
    if user_picked_no != com_picked_no :
        remained_life -= 1
        print(f"your remained life is {remained_life}.")

difficulty_choice()
while LIFE_SWITCH :
    user_picked_no = int(input("plz input number between 1~100 : "))
    win_lose_condition()
    life_subtract()
    number_check()