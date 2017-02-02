#Sarah Nicholson

from random import *

def main():
    shuffle1test()
    print()
    shuffletest()
    print()
    for i in range(10):
        hand = []
        deck = Deck()
        deck.shuffle()
        for j in range(5):
            hand.append(deck.dealCard())
        print(hand)
    
def shuffle1(myList):
    #function created to shuffle a list without using shuffle in it
    newList = []
    for i in range(len(myList)):
        newList.append(myList.pop(randint(0,len(myList)-1)))
    myList += newList
        
def shuffle1test():
    #testing the shuffle function that doesn't use shuffle
    #returns how many times 1 is in each position in the list
    myList = [1,2,3,4,5,6,7,8,9,10]
    onePosition = [1]*10
    for i in range(1000):
        shuffle1(myList)
        onePosition[myList.index(2)] += 1
    print(onePosition)

def shuffletest():
    #testing shuffle using the shuffle provided by random
    #returns how many times 1 is in each position in the list
    myList = [1,2,3,4,5,6,7,8,9,10]
    onePosition = [0]*10
    for i in range(1000):
        shuffle(myList)
        onePosition[myList.index(1)] += 1
    print(onePosition)
    
class Deck:
    def __init__(self):
        #creates the deck
        self.deck = []
        for i in range(1,14):
            for suits in ('c','d','h','s'):
                self.deck.append((i,suits))
        
    def shuffle(self):
        #shuffles the deck
        shuffle(self.deck)
    
    def dealCard(self):
        #deals a card and then gets rid of it
        return self.deck.pop(0)

    def cardsLeft(self):
        #returns how many cards are left in the deck
        return str(len(self.cards))

main()
