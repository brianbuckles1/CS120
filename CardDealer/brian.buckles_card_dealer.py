""" cards.py
    demonstrates functions
    manage a deck of cards db

"""
import random
import math

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    print("\nDeck of Cards:")
    print("------------------------")
    showDB(cardDB)

    print("\nPlayer hand:")
    print("------------------------")
    showHand(cardDB, PLAYER)

    print("\nComputer hand: ")
    print("------------------------")
    showHand(cardDB, COMPUTER)

def initCards():
    '''Initialize and return the cardDB which holds all the card assignments.
     By default they are all set to 0 which is assigned to the deck.'''
    cardDB = []
    for _ in range(0, 52):
        cardDB.append(0)

    return cardDB

def assignCard(cardDB, hand):
    '''Assign a random card not currently assigned to the hand passed in.'''
    keepgoing = True

    while(keepgoing):
        selectedCard = random.randint(0,51)

        if cardDB[selectedCard] == 0:
            cardDB[selectedCard] = hand
            keepgoing = False
            continue
    return

def showDB(cardDB):
    '''Show all the card assignments'''
    for index in range(len(cardDB)):
        # format nicely with 18 chars
        print(f'{index}\t{getCardName(index):<18}\t{HANDS[cardDB[index]]}')
    return

def showHand(cardDB, hand):
    '''Show the hand for the hand index passed in.'''
    for index in range(len(cardDB)):
        if cardDB[index] == hand:
            print(getCardName(index))
    return

def getCardName(cardIndex):
    '''return the card name from the card index passed in.'''

    # neat little function to get quotient and remainder
    suit, rank = divmod(cardIndex,13)
    return f'{RANKNAME[rank]} of {SUITNAME[suit]}'

main()