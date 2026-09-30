import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def display_score(score):
    if score == 0:
        return 21
    else:
        return score

def deal_cards():
    chosen_cards = random.choice(cards)
    return chosen_cards

def calculate_score(cards):
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    while 11 in cards and score > 21:
        ace_pos = cards.index(11)
        cards[ace_pos] = 1
        score = sum(cards)
    return score


def play_game():

    user_cards = []
    computer_cards = []

    for c1 in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)



    print(f"Your cards: {user_cards}, current score: {display_score(user_score)}")
    print(f"Computer's first card: {computer_cards[0]}")

    game_on = True

    if user_score == 0 or computer_score == 0:
        game_on = False

    while game_on:
        question = input("Type 'y' to get another card, type 'n' to pass:").lower()
        while question not in ["y", "n"]:
            question = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if question == "n":
            game_on = False
        elif question == "y":
            user_cards.append(deal_cards())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {display_score(user_score)}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score > 21:
                game_on = False

    if user_score <= 21 and user_score != 0 and computer_score != 0:
        while computer_score < 17:
                computer_cards.append(deal_cards())
                computer_score = calculate_score(computer_cards)


    print(f"Your final Hand: {user_cards} and final score: {display_score(user_score)}")
    print(f"Computer's final Hand: {computer_cards} and final score: {display_score(computer_score)}")

    if user_score == computer_score:
        print("Draw!")
    elif user_score == 0:
        print("Blackjack!")
    elif computer_score == 0:
        print("Computer has Blackjack!")
    elif user_score > 21:
        print("You Lose!")
    elif computer_score > 21:
        print("You Win!")
    elif user_score > computer_score:
        print("You Win!")
    elif computer_score > user_score:
        print("You Lose!")


question2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
while question2 not in ["y", "n"]:
    question2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
while question2 == "y":
    play_game()
    question2 = input("Do you want to keep playing Blackjack 'y' or 'n'\n").lower()
    while question2 not in ["y", "n"]:
        question2 = input("Do you want to keep playing Blackjack 'y' or 'n'\n").lower()
print("Thank you for playing Blackjack!")
