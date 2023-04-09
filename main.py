import random

        
# Class to create a new card

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'

# Class to create a new deck of cards 

class Deck: 
    def __init__(self):
        self.cards = []
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        ranks = [{"rank": 'A', "value": 11}, {"rank": '', "value": 2}, {"rank": '3', "value": 3}, {"rank": '4', "value": 4}, {"rank": '5', "value": 5}, {"rank": '6', "value": 6}, {"rank": '7', "value": 7}, {"rank": '8', "value": 8}, {"rank": '9', "value": 9}, {"rank": '10', "value": 10}, {"rank": 'J', "value": 10}, {"rank": 'Q', "value": 10}, {"rank": 'K', "value": 10}]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
            
    def shuffleCards(self): 
        if (len(self.cards) != 0):
            random.shuffle(self.cards)   
    def dealCards(self, num):
            deltCards = []
            for i in range(num):
                if len(self.cards) != 0: 
                    deltCards.append(self.cards.pop())
            return deltCards   
        
# Class to create a hand of cards

class Hand:
    def __init__(self, house = False):
        self.cards = []
        self.value = 0
        self.house = house
    def addCard(self, cardsList):
        self.cards.extend(cardsList)
    def calculateHand(self):
        self.value = 0
        Ace = False
        for card in self.cards:
            if card == 'A':
                Ace = True
            cardValue = int(card.rank["value"])
            self.value += cardValue
        if Ace and self.value > 21:
            self.value -= 10
    def getValue(self):
        self.calculateHand()
        return self.value
    def isBlackJack(self):
        if self.getValue() == 21: return True
        return False
    def showHand(self, showDealer = False):
        if self.house == True: 
            print(f'Dealer\'s Hand: ')
            for index, card in enumerate(self.cards):
                if index == 0 and not showDealer and not self.isBlackJack(): print()
                else: print(card)
            print(f'Value: {self.getValue()}')
            print()
        else: 
            print(f'Player\'s Hand: ')
            for card in self.cards:
                print(card)
            print(f'Value: {self.getValue()}')
            print()

# deck = Deck()
# deck.shuffleCards()

# hand = Hand()
# hand.addCard(deck.dealCards(2))
# hand.showHand()

# Testing purposes = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
# newCard = Card('hearts', {"rank": 'A', "value": 11})
# print(newCard)
# newdeck = Deck()
# newdeck.shuffleCards()
# print(newdeck.cards)