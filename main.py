import random

cards = []
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

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

if rank == 'A': value = 11
elif rank == 'J' or rank == 'Q' or rank == 'K': value = 10
else: value = rank

cardInfo = {'rank': rank, 'value': value}

print(cardInfo)

