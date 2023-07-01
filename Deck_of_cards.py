import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def present(self):
        return self.value+' '+'of'+' '+self.suit



class Deck: 
    def __init__(self):
        reqlist = []
        suits = ['hearts','diamonds','clubs','spades']
        values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        for i in suits:
            for j in values:
                reqlist.append(Card(i,j))
        self.cards = reqlist
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        if len(self.cards)>0:
            tempvariable = self.cards.pop()
            return(tempvariable)
        else:
            return None
    
    def count_remaining(self):
        return len(self.cards)
    
    def get_remaining(self):
        templist = []
        for i in self.cards:
            templist.append(i.present())
        return templist
