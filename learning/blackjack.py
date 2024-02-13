############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
import random

def deal_card():
    """
    Returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

computer_hand = []
user_hand = []

for _ in range(2):
    computer_hand.append(deal_card())
    user_hand.append(deal_card())

def score(hands):
    """
    Takes a list of cards and returns the score
    """
    result = sum(hands)
    if result > 21 and 11 in hands:
        result -= 10

    return result

def is_blackjack(hand):
    return score(hand) == 21

def end_game(computer_score, user_score):
    print ("Your final hand: " + str(user_hand))
    print ("Computer's final hand: " + str(computer_hand))
    
    if user_score == computer_score:
        print ("Draw!")
    if computer_score == 21:
        print ("I Win. I have blackjack!")
    elif user_score == 21:
        print ("You Win. You have blackjack!")
    elif user_score > 21:
        print ("You went over. You lose!")
    elif computer_score > 21:
        print ("I went over. You Win!")
    elif user_score > computer_score:
        print ("You Win!")
    else:
        print ("You lose!")
        

print ("User Hand: " + str(user_hand) + ", User Score: " + str(score(user_hand)))
print ("Computer's first card: " + str(computer_hand[0]))

end_of_game = False

while not(end_of_game):
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        user_hand.append(deal_card())
        
        computer_score = score(computer_hand)
        user_score = score(user_hand)

        print ("\nNew User Hand: " + str(user_hand) + ", User Score: " + str(user_score))

        if user_score == 21 or computer_score == 21 or user_score > 21:
            end_of_game = True
            end_game(computer_score, user_score)
    else:
        end_of_game = True
        while score(computer_hand) < 17:
            computer_hand.append(deal_card())

        end_game(score(computer_hand), score(user_hand))