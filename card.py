import random

class Card:

    Suits = ('D', 'H', 'C', 'S')
    B_Suits = ('CS')
    Faces = range(1, 14)
    Rank_dict = {'1':'A', 'A':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'T':'10', 'J':'11', 'Q':'12', 'K':'13', '10':'T', '11':'J', '12':'Q', '13':'K'}
    Suit_dict = {'1':'D' ,  '2':'H' , '3':'C' , '4':'S' }

    def __init__(self, theRank, theSuit):
        self.suit = theSuit
        self.rank = theRank

    #"A:S"
    def __str__(self):
        return self.rank + ":" + self.suit

    #return suit of a recieved card
    def get_suit(self):
        return str(self.suit)

    #return rank of recieved card
    def get_rank(self):
        return str(self.rank)

    def compare_2Cards (self,src_card, dest_card):
        src = src_card
        dest = dest_card
        ranks_dic = Card.Rank_dict

        if ranks_dic[src[-3]] > ranks_dic[dest[-3]]:
            print ("source has higher rank")
        else:
            print("destination has higher rank")


def main():
    theCard = Card("A", "C")
    print(theCard)
if __name__ == "__main__":
    main()
