import random
from random import shuffle
from card import Card


class Deck:

    lenght = 0

    def __init__(self, value_start, value_end, number_of_suits):
        self.the_deck = []
        self.star_val = value_start
        self.end_val = value_end
        self.num_of_suits = number_of_suits

        face_lst = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        suits_lst = ['S', 'D', 'H', 'C']
        #j = self.star_val
        for i in range(self.num_of_suits):
            for j in range(self.star_val - 1, self.end_val, 1):
                theCard = Card(str(face_lst[j]), str(suits_lst[i]))
                self.the_deck.append(theCard)
                Deck.lenght +=1

    def __str__(self):
        return str(self.the_deck)

    def __len__(self):
        return self.lenght

    def shuffle_in_place(self, lst):
        my_list = lst
        for i in range(len(my_list)):
            for j in range(random.randint(0, len(my_list) // 2), len(my_list), 2):
                my_list[i], my_list[j] = my_list[j], my_list[i]

        return my_list

    def draw_Card(self):
        self.lenght -= 1
        return self.the_deck.pop(0)

    def is_inDeck(self, face, suit):

        one_card = Card(face, suit)

        i = 0
        q = len((self.the_deck))

        while (i < len(self.the_deck)):

            if str(one_card) in self.the_deck:
                return True
            elif self.the_deck[i] != str(one_card) and (i == len(self.the_deck) - 1):
                return False
            i += 1

    def add2_deck(self, face, suit):
        new_face = face
        new_suit = suit
        new_card = Card(face, suit)

        if self.is_inDeck(new_face, new_suit):
            return "Already exist"
        else:
            self.the_deck.append(str(new_card))
        return self.the_deck


    def shuffle(self):
        #return self

        self.shuffle_in_place(self.the_deck)
        return self.the_deck

    def shuffle_1(self):

        face_lst = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits_lst = ['S', 'D', 'H', 'C']

        j = self.star_val

        for i in range(self.num_of_suits):
                for j in range(self.star_val - 1, self.end_val,1):
                    theCard = Card(str(face_lst[j]),str(suits_lst[i]))
                    return (theCard)


    def random_card(self):

        face_lst = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits_lst = ['S', 'D', 'H', 'C']

        spades_tmp_lst = []
        clubs_tmp_lst = []
        diamond_tmp_lst = []
        hearts_tmp_lst = []

        for i in range(len(suits_lst)):
            for j in range(len(face_lst)):
                rand_card = str(face_lst[j]) + ":" + str(suits_lst[i])

                if suits_lst[i] == 'S':
                    spades_tmp_lst.append(rand_card)
                elif suits_lst[i] == 'D':
                    diamond_tmp_lst.append(rand_card)
                elif suits_lst[i] == 'H':
                    hearts_tmp_lst.append(rand_card)
                else:
                    clubs_tmp_lst.append(rand_card)


        ordered_pack =  spades_tmp_lst + diamond_tmp_lst + hearts_tmp_lst + clubs_tmp_lst
        shuffled_pack = ordered_pack[:]
        random.shuffle(shuffled_pack)


        #return shuffled_pack
        return ordered_pack





def main():

    my_d = Deck(1,1,4)
    print(str(my_d))
    print(str(my_d.is_inDeck("6","H")))
    print(str(my_d.add2_deck("6","H")))

    my_d.shuffle_in_place(my_d.the_deck)

    #my_d2 the second generated deck
    my_d2 = Deck(1,6,1)
    print(str(my_d2.shuffle_in_place(my_d2.the_deck)))

    #my_d the first generated deck
    print('Original Deck' + '\n' + str(my_d.shuffle_in_place(my_d.the_deck)))

    print('-' * 20)
    print ('Original Deck length: ' , len((my_d)))
    print(my_d.draw_Card())
    print('Deck length after drawing one card' , len(my_d))
    print(str(my_d))
if __name__ == "__main__":
    main()