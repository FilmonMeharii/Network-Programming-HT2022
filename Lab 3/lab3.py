import random

print("\n\n")

Suit = ["spades","hearts","diamonds","clubs"]
Value = ["Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

class Card:
    def __init__(self, suit, value):
        assert 1 <= suit[0] <= 4 and 1 <= value[0] <= 13
       
        self._suit = suit
        self._value = value
       
    def getValue(self):
        return self._value
#Shall return the card's value as an integer between 1 and 13


    def getSuit(self):
        return self._suit
#Shall return the card's suit as an integer between 1 and 4

    def __str__(self):
        return "{} of {}".format(self._value[1],self._suit[1])

class CardDeck:
    def __init__(self):
        self.reset()

#shall shuffle the cards
    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def getCard(self):
        return self.cards.pop()
#reduce the list by one

    def size(self):
        return len(self.cards)

    def reset(self):
        self.cards = []
        for suit in enumerate(Suit, 1):
            for value in enumerate(Value,1):
                self.cards.append(Card(suit,value))

    def getDeck(self):
        return self.cards


deck = CardDeck()
li = deck.getDeck()

for i in range(deck.size()):
    print(' ', str(i+1)+'. ', li[i])
    
deck.shuffle()
while deck.size()>0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()[0]))
