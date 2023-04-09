import random

cards = []
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = [{"rank": 'A', "value": 11}, {"rank": '', "value": 2}, {"rank": '3', "value": 3}, {"rank": '4', "value": 4}, {"rank": '5', "value": 5}, {"rank": '6', "value": 6}, {"rank": '7', "value": 7}, {"rank": '8', "value": 8}, {"rank": '9', "value": 9}, {"rank": '10', "value": 10}, {"rank": 'J', "value": 10}, {"rank": 'Q', "value": 10}, {"rank": 'K', "value": 10}]

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
     
def shuffleCards():
    random.shuffle(cards)   
def dealCard(num):
    deltCards = []
    for i in range(num):
        deltCards.append(cards.pop())
    return deltCards
    
    
shuffleCards()
cardsDelt = dealCard(2)
card = cardsDelt[0]
rank = card[1]

print(card)

