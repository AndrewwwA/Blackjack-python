import random
import tkinter as tk
# from tkinter import ttk
import time
import ttkbootstrap as ttk

        
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
            
# class to actually start the game 

class Game:
    # def __int__(self):
    def play(self):
        gameNumber = 0
        gameAmount = 0
        
        try:
            gameAmount = int(input('How many games would you like to play? '))
        except:
            print('Please enter a number')
            
        while gameNumber < gameAmount:
            if gameNumber > 0: time.sleep(2.5)
                
            gameNumber += 1
        
            gameDeck = Deck()
            gameDeck.shuffleCards()
            
            playerHand = Hand()
            dealerHand = Hand(house = True)
            
            for x in range(2):
                playerHand.addCard(gameDeck.dealCards(1))
                dealerHand.addCard(gameDeck.dealCards(1))
            
            print()
            print(f'Game {gameNumber} of {gameAmount}')
            print('-' * 30)
            playerHand.showHand()
            dealerHand.showHand()
            
            if self.checkWinner(playerHand, dealerHand):
                continue
            
            choice = " "
            
            while playerHand.getValue() < 21 and choice not in ['stand']:
                choice = input('Would you like to Hit or Stand?: ').lower()
                print()
                while choice not in ['hit', 'stand']:
                    choice = input('Please enter a valid input, inputs can be stand or hit: ')
                    print()
                if choice in ['hit']:
                    playerHand.addCard(gameDeck.dealCards(1))
                    playerHand.showHand()
                    
            if self.checkWinner(playerHand, dealerHand):
                continue
            
            playerValue = playerHand.getValue()
            dealerValue = dealerHand.getValue()
            
            while dealerValue < 17:
                dealerHand.addCard(gameDeck.dealCards(1))
                dealerValue = dealerHand.getValue()
            
            dealerHand.showHand(showDealer = True)
            
            if self.checkWinner(playerHand, dealerHand):
                continue
            
            print('The winner is:')
            print(f'Player\'s Hand: {playerValue}')
            print(f'Dealer\'s Hand: {dealerValue}')
            
            self.checkWinner(playerHand, dealerHand, gameStatus= True)
        
        print('Game Over')
                
                
    def checkWinner(self, playerHand, dealerHand, gameStatus = False):
        if not gameStatus:
            if playerHand.getValue() > 21:
                print('You busted!') 
                return True
            if dealerHand.getValue() > 21:
                print('Dealer busted! You won!') 
                return True
            if dealerHand.isBlackJack() and playerHand.isBlackJack():
                print('Both players have a blackJack! Tie')
                return True
            if playerHand.isBlackJack():
                print('YOu have a blackJack! You won!')
                return True
            if dealerHand.isBlackJack():
                print('Dealer has a blackJack! You lost!')
                return True
            return False
        else:
            print('testestest', playerHand.getValue, dealerHand.getValue)
            if playerHand.getValue() > dealerHand.getValue():
                print('You win')
            if playerHand.getValue() == dealerHand.getValue():
                print('It\'s a tie')
            else:
                print('Dealer won! You lost!')
            
# g = Game()
# g.play()
        
# GUI BLACKJACK TESTING
            
# def convert():
#     print(entry.get())
#     outputString.set(entry.get())
#     entry.delete(0, tk.END)

# window'

window = ttk.Window(themename = 'vapor')
window.title('BlackJack Game')
window.geometry('800x600')
window.iconbitmap('PICTURES/blackjack.ico')

# Title pretty much means text
titleLabel = ttk.Label(master = window, text = 'BlackJack Game', font = ('Arial', 18, 'bold'))
titleLabel.pack()

# # input field
gameFrame = ttk.Frame(master = window, relief = 'groove', height = 380, width = 500)
buttonFrame = ttk.Frame(master = window, relief = 'groove', width = 300, height = 100)
# # entry = ttk.Entry(master = buttonFrame, )
# button = ttk.Button(master = buttonFrame, text = 'Start Game')
# # entry.pack( side = 'left', padx = 10)
# button.pack()
gameFrame.place(rely = 0.09, relx = 0.2)
buttonFrame.place(rely = 0.75, relx = 0.31)

startNewGame = ttk.Button(window, text = 'Reset Game')
startNewGame.pack(side = 'bottom', pady = 10)

# # output
# outputString = tk.StringVar()
# outputLabel = ttk.Label(master = window, text = 'Output', font = ('Arial', 18), textvariable= outputString)
# outputLabel.pack( pady = 5)

# run main loop (pretty much start the file)
window.mainloop()
