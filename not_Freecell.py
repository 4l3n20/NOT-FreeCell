from deck import Deck
from card import *
from stack import Stack # borrowed from Monash Alexandria article

import card

class notFreecell:

    # Temp_Cell_Slote are used for temporary and reserved cells on the left hand side
    Temp_Cell_Slots = 4

    # Fundation_Slots are used in form of stack to collect 4 ordered distinct suits
    Fundation_Slots = 4 #len(card.Card.Suits)

    # used for main part of game and dealing cards
    Tableau_Slots = 8

    def __init__(self):

        # make an instance of class deck with 3 parameters
        self.game_deck = Deck(1, 13, 4)

        # shuffle the the generated deck using Deck class's shuffle_in_place function.
        self.game_deck.shuffle_in_place(self.game_deck.the_deck)

        # temp_Cells is a list used as buffer ( 3 slots on the left side of the tableau)
        self.temp_Cells = [0] * self.Temp_Cell_Slots

        # 4 stacks for storing each suit's cards(Diamond, Heart, Club, Spade)
        self.foundation_D = Stack()
        self.foundation_H = Stack()
        self.foundation_C = Stack()
        self.foundation_S = Stack()

        # 8 lists for implementing cascades
        self.cascades = []
        for i in range(self.Tableau_Slots):
            self.Cascades_Col = []
            self.cascades.append(self.Cascades_Col)


    def __str__(self):
        return str(self.cascades)

    # This function is in charge of portraying tableau in form of freecell game
    def print_game(self):
        print("\n")
        print('Temp-Cells' + ' ' * 20 + 'Foundations(D,H,C,S)')

        # foundations are initiated in __init__ as place for foundations (type: Stack)
        if self.foundation_D.count != 0:
            last_foundation_D_item = str(self.foundation_D.peek()) #last item of foundation D
        else:
            last_foundation_D_item = "[ ]"

        if self.foundation_H.count != 0:
            last_foundation_H_item = str(self.foundation_H.peek())  # last item of foundation H
        else:
            last_foundation_H_item = "[ ]"

        if self.foundation_C.count != 0:
            last_foundation_C_item = str(self.foundation_C.peek())  # last item of foundation H
        else:
            last_foundation_C_item = "[ ]"

        if self.foundation_S.count != 0:
            last_foundation_S_item = str(self.foundation_S.peek())  # last item of foundation H
        else:
            last_foundation_S_item = "[ ]"

        # creating Temp_cell Slots (self.temp_Cells is initiated in __init__ for Cell slots)(type:list)
        # because I aimed to show empty Cell Slots with empty brackets[] I had to fill it with 0 to empower
        # game to check if cell value is 0 change it to [ ] when printing output
        t_cells = ""
        for item in self.temp_Cells:
            if item == 0:
                t_cells += "[   ]"
            else:
                t_cells += "[" + str(item) + "]"

        # printing Cells and  Foundations in one line
        print(t_cells + ' ' * 10 + "[" + last_foundation_D_item + "] [" \
              + last_foundation_H_item + "] [" + last_foundation_C_item + "] [" + last_foundation_S_item + "]")

        print("-" * 99)

        # creating cascades
        # assumed that maximum length of each cascade is 15
        output_string = ""
        i = 0
        while i < 15:
            j = 0
            while j < 8:
                if i < len(self.cascades[j]):
                    output_string += str(self.cascades[j][i]) + "    "
                else:
                    output_string += "       "
                j += 1
            output_string += "\n"
            i += 1
        # This string contain whole cascades cards
        print(output_string)

        # CHECKING FOR VICTORY
        self.victory_check()

    # Check Victory and Congrate user for persistance on checking
    # whether he/she can see the "Victory Congrats" in this PROTOTYPE. :)
    def victory_check(self):

        # check if all foundations are not empty
        if self.foundation_S.count != 0 and self.foundation_D.count != 0 and self.foundation_C.count != 0 and self.foundation_H.count != 0:
            foundation_S_lst_item = self.foundation_S.peek()
            foundation_D_lst_item = self.foundation_D.peek()
            foundation_C_lst_item = self.foundation_C.peek()
            foundation_H_lst_item = self.foundation_H.peek()

            # check if all foundations are filled up to KING
            if foundation_S_lst_item.get_rank() == "K" and foundation_D_lst_item.get_rank() == "K" and \
               foundation_C_lst_item.get_rank() == "K" and foundation_H_lst_item.get_rank() == "K":
                print("VICTORY! CONGRATS")

    # Draw cards from deck and fill tableau. After this deck is going to be empty
    def fill_tableau(self):

        i = 0

        while i <= (len(self.game_deck.the_deck)) or len(self.game_deck.the_deck) != 0:

            j = 0

            while j < 8 and self.game_deck.lenght != 0: # len(self.game_deck.the_deck) != 0:

                # fill tableau by calling draw_Card function from class Deck
                self.cascades[j].append(self.game_deck.draw_Card())
                j += 1
            i += 1

        self.print_game()

    # compare two cards in terms of their rank and inequality of suits
    # the result of this function is either True or false
    # the outcome will be used in cascade_move() if the value returned by this function is true
    # source and destination cards meet the rules of freecel card moving
    def compare_Cards(self, src_card, dest_card):
        src = src_card.upper()
        dest = dest_card.upper()
        ranks_dic = Card.Rank_dict
        black_suits = card.Card.B_Suits
        # recognization of source card colour, is it black?!
        if src[-1] in black_suits and dest[-1] in black_suits:
            print("Both cards are Black, Freecell suit colour rule violated!")
            self.print_game()
            return False
        # recognization of source card colour, is it red?!
        elif src[-1] not in black_suits and dest[-1] not in black_suits:
            print("Both cards are Red, Freecell suit colour rule violated!")
            self.print_game()
            return False
        # check if destination card is one rank greater or not!
        elif ranks_dic[dest[-3]] == str(int(ranks_dic[src[-3]]) + 1):
            print("destination has 1 higher rank")
            print("src < dest - Freecell move rule complied! ")
            return True
        elif ranks_dic[dest[-3]] > str(int(ranks_dic[src[-3]]) + 1):
            print("Destination has higher rank but more than one rank")
            self.print_game()
            return False
        else:
            print("source has higher rank")
            self.print_game()
            return False

    # Relocate one card "src_card" to destination, by checking the colour, suits
    # and whether cards are at the end of list or not
    # this function will be used and called in "MOVE()" function
    def find_cardAndremove(self, src_card, dest_card):
        #lst_ofCascades = self.cascades
        src = src_card.upper()
        dest = dest_card.upper()
        flag_src = False
        flag_dest = False

        # Find if source card object is at the end of any cascade
        for sublist_src in self.cascades:
            if len(sublist_src) != 0:
                if sublist_src[-1].get_suit() == src[-1] and sublist_src[-1].get_rank() == src[-3]:
                    flag_src = True
                    break
        # Find if Destination card object is at the end of any cascade
        for sublist_Dest in self.cascades:
            if len(sublist_Dest) != 0:
                if sublist_Dest[-1].get_suit() == dest[-1] and sublist_Dest[-1].get_rank() == dest[-3]:
                    flag_dest = True
                    break
        # check flag set by two prior loops if they are both True moves the source card to destination
        if flag_dest and flag_src:
            for sublist in self.cascades:
                if len(sublist) != 0:
                    if sublist[-1].get_suit() == src[-1] and sublist[-1].get_rank() == src[-3]:
                        src_To_Dest = sublist.pop()
                        for sublist_Destin in self.cascades:
                            if len(sublist_Destin) != 0:
                                if sublist_Destin[-1].get_suit() == dest[-1] and sublist_Destin[-1].get_rank() == dest[-3]:
                                    sublist_Destin.append(src_To_Dest)
            print('the card relocated')
        self.print_game()

    # check foundation is empty using suit argument and return number of item in it
    def check_foundation(self, suit):
        suit_foundation = int(suit)

        # return the number of cards in each foundation
        if self.foundations[suit_foundation] == 1: #Diamonds
            return self.foundations[0].count()
        if self.foundations[suit_foundation] == 2: #Harts
            return self.foundations[1].count()
        if self.foundations[suit_foundation] == 3: #Clubs
            return self.foundations[2].count()
        if self.foundations[suit_foundation] == 4: #Spades
            return self.foundations[3].count()

    # this function is used in menu to call "move_card2Foundation"
    # to move a card to foundations under the Freecell's foundation cells rules
    # the reason I used two function for moving to foundation is to empower the code change easily
    # in future if any changes in move_card-2Foundation occur it is easy to just replace with that
    # not whole game changing
    def call_move_2_foundation(self):
        print('which card you want to move to foundation?')
        src_card = input('source card: ').upper()
        self.move_card2Foundation(src_card)

    # add cards to foundation
    def move_card2Foundation (self, src_card):

        lst_ofCascades = self.cascades
        seled_Crd = src_card.upper()
        ranks_dic = Card.Rank_dict
        suits = card.Card.Suit_dict

        for sublist in lst_ofCascades:
            if len(sublist) != 0:
                # check the last item of each cascade in terms of rank and suit
                if sublist[-1].get_suit() == seled_Crd[-1] and sublist[-1].get_rank() == seled_Crd[-3]:
                    # Moving ACE,JACK,QUEEN,KING to corresponding foundation
                    # move ACE,JACK,QUEEN,KING of Diamond to foundation[0]
                    if ranks_dic['1'] == seled_Crd[-3] or ranks_dic['10'] == seled_Crd[-3] or ranks_dic['11'] == seled_Crd[-3] or ranks_dic['12'] == seled_Crd[-3] or ranks_dic['13'] == seled_Crd[-3] :
                        if suits['1'] == seled_Crd[-1]:
                            src_To_Dest = sublist.pop()
                            self.foundation_D.push(src_To_Dest)
                            print('move done to foundation Diamonds')
                        # move ACE,JACK,QUEEN,KING of Hearts to foundation[1]
                        elif ranks_dic['1'] == seled_Crd[-3] or ranks_dic['10'] == seled_Crd[-3] or ranks_dic['11'] == seled_Crd[-3] or ranks_dic['12'] == seled_Crd[-3] or ranks_dic['13'] == seled_Crd[-3] :
                            if suits['2'] == seled_Crd[-1]:
                                src_To_Dest = sublist.pop()
                                self.foundation_H.push(src_To_Dest)
                                print('move done to foundation Harts')
                            # move ACE,JACK,QUEEN,KING of Club to foundation[2]
                            elif ranks_dic['1'] == seled_Crd[-3] or ranks_dic['10'] == seled_Crd[-3] or ranks_dic['11'] == seled_Crd[-3] or ranks_dic['12'] == seled_Crd[-3] or ranks_dic['13'] == seled_Crd[-3] :
                                if suits['3'] == seled_Crd[-1]:
                                    src_To_Dest = sublist.pop()
                                    self.foundation_C.push(src_To_Dest)
                                    print('move done to foundation Clubs')
                                # move ACE,JACK,QUEEN,KING of Spade to foundation[3]
                                elif ranks_dic['1'] == seled_Crd[-3] or ranks_dic['10'] == seled_Crd[-3] or ranks_dic['11'] == seled_Crd[-3] or ranks_dic['12'] == seled_Crd[-3] or ranks_dic['13'] == seled_Crd[-3] :
                                    if suits['4'] == seled_Crd[-1]:
                                        src_To_Dest = sublist.pop()
                                        self.foundation_S.push(src_To_Dest)
                                        print('move done to foundation Spades')

                    elif seled_Crd[-1] == suits['1']:  # if suit is Diamond
                        if self.foundation_D.count != 0:
                            foundation_last_item = self.foundation_D.peek()
                            # a= src[-3]
                            # b= int(foundation_last[-3]) + 1
                            if int(ranks_dic[foundation_last_item.get_rank()]) + 1 == int(seled_Crd[-3]):
                                src_To_Dest = sublist.pop()
                                self.foundation_D.push(src_To_Dest)
                            else:
                                print('impossible to push in Diamond foundation')
                        else:
                            print('Diamond foundation is empty or cards left before this card to add foundation')

                    elif seled_Crd[-1] == suits['2']:  # if suit is Hearts
                        if self.foundation_H.count != 0:
                            foundation_last_item = self.foundation_H.peek()
                            # a= src[-3]
                            # b= int(foundation_last[-3]) + 1
                            if int(ranks_dic[foundation_last_item.get_rank()]) + 1 == int(seled_Crd[-3]):
                                src_To_Dest = sublist.pop()
                                self.foundation_H.push(src_To_Dest)
                            else:
                                print('impossible to push in Hearts foundation')
                        else:
                            print('Heart foundation is empty or cards left before this card to add foundation')


                    elif seled_Crd[-1] == suits['3']:  # if suit is clubs
                        if self.foundation_C.count != 0:
                            foundation_last_item = self.foundation_C.peek()
                            if int(ranks_dic[foundation_last_item.get_rank()]) + 1 == int(seled_Crd[-3]) :
                                src_To_Dest = sublist.pop()
                                self.foundation_C.push(src_To_Dest)
                            else:
                                print('impossible to push in Clubs foundation')
                        else:
                            print('Club foundation is empty or cards left before this card to add foundation')


                    elif seled_Crd[-1] == suits['4']:  # if suit is Spades
                        if self.foundation_S.count != 0:
                            foundation_last_item = self.foundation_S.peek()
                            if int(ranks_dic[foundation_last_item.get_rank()]) + 1 == int(seled_Crd[-3]):
                                src_To_Dest = sublist.pop()
                                self.foundation_S.push(src_To_Dest)
                            else:
                                print('impossible to push in Spades foundation')
                        else:
                            print('Spade foundation is empty or cards left before this card to add foundation')

        self.print_game()

    # move function use compare card to find out if they are in different colour.
    # move function reposition one card to destination location by calling "find_cardAndmove" function
    # this move used within cascades area
    def cascades_move(self):

        print('enter two cards to move')
        src_crd = input('source card: ').upper()
        dest_crd = input('destination card: ').upper()
        if self.compare_Cards(src_crd,dest_crd):
            if self.find_cardAndremove(src_crd,dest_crd):
                print("moved")

    #move to temporary cells
    def move_toTempCells (self):

        lst_ofCascades = self.cascades
        src = input("Which card you want to move to temp-cells? ").upper()
        tempCell_len = len(self.temp_Cells)

        find_flag = True

        for tempC_item in self.temp_Cells:
            if tempC_item == 0:
                #x = self.temp_Cells
                self.temp_Cells.remove(tempC_item)
                #y = self.temp_Cells
                tempCell_len = len(self.temp_Cells)
                if tempCell_len < 4:
                    for sublist in self.cascades:
                        if len(sublist) != 0:
                            if sublist[-1].get_suit() == src[-1] and sublist[-1].get_rank() == src[-3]:
                                src_To_Dest = sublist.pop()
                                self.temp_Cells.append(src_To_Dest)
                            else:
                                find_flag = False

        i = len(self.temp_Cells)
        if i < 4:
            while i < 4:
                self.temp_Cells.append(0)
                i += 1
        self.print_game()

    # used to move card from temp_cell or Slots to cascades
    def move_frmTempCell_to_Cascade(self):
        lst_ofCascades = self.cascades
        src_crd = input("Which card you want to move from temp-cells? ").upper()
        dest_crd = input("Where you want to put it? ").upper()
        tempCell_len = len(self.temp_Cells)

        for item in self.temp_Cells:
            if item != 0:
                if item.get_suit() == src_crd[-1] and item.get_rank() == src_crd[-3]:
                    for sublist in lst_ofCascades:
                        if len(sublist) != 0:
                            if sublist[-1].get_suit() == dest_crd[-1] and sublist[-1].get_rank() == dest_crd[-3]:
                                sublist.append(item)
                                self.temp_Cells.remove(item)
                                # we should add a 0 number to temcell for reserving space of [ ]
                                self.temp_Cells.append(0)

        self.print_game()

    # used to move card from temp_cell or Slots to foundation
    def move_frmTempCell_to_Foundation(self):
        ranks_dic = Card.Rank_dict
        suits_dic = Card.Suit_dict
        seled_Crd = input("which card you want to move to foundation").upper()

        for tmp_cell_item in self.temp_Cells:
            if tmp_cell_item != 0:
                # compare the rank and suit each TempCell element with source card
                if tmp_cell_item.get_suit() == seled_Crd[-1] and tmp_cell_item.get_rank() == seled_Crd[-3]:
                    # Moving ace to corresponding foundation
                    # move ACE:Diamond to foundation[0]
                    if ranks_dic['1'] == seled_Crd[-3]:
                        if suits_dic['1'] == seled_Crd[-1]:
                            self.foundation_D.push(tmp_cell_item)
                            self.temp_Cells.remove(tmp_cell_item)
                            self.temp_Cells.append(0)
                            print('move done to foundation Diamonds')
                        # move ACE:Hearts to foundation[1]
                        elif ranks_dic['1'] == seled_Crd[-3]:
                            if suits_dic['2'] == seled_Crd[-1]:
                                self.foundation_H.push(tmp_cell_item)
                                self.temp_Cells.remove(tmp_cell_item)
                                self.temp_Cells.append(0)
                                print('move done to foundation Harts')
                            # move ACE:Club to foundation[2]
                            elif ranks_dic['1'] == seled_Crd[-3]:
                                if suits_dic['3'] == seled_Crd[-1]:
                                    self.foundation_C.push(tmp_cell_item)
                                    self.temp_Cells.remove(tmp_cell_item)
                                    self.temp_Cells.append(0)
                                    print('move done to foundation Clubs')
                                # move ACE:Spade to foundation[3]
                                else:
                                    self.foundation_S.push(tmp_cell_item)  # move ACE:Spade to foundation[3]
                                    self.temp_Cells.remove(tmp_cell_item)
                                    self.temp_Cells.append(0)
                                    print('move done to foundation Spades')

                # check if selected card is not ACE and prior card to attempted one is exist in foundation
                    elif self.foundation_D.count != 0 and suits_dic['1'] == seled_Crd[-1]:
                        foundation_lst_card = self.foundation_D.peek()
                        if foundation_lst_card.get_suit() == suits_dic['1']: #if suit is Diamond
                            # x = int(ranks_dic[seled_Crd[-3]])
                            # z = int(ranks_dic[foundation_lst_card[-3]])
                            if int(ranks_dic[seled_Crd[-3]]) == int(ranks_dic[foundation_lst_card.get_rank()]) + 1:
                                self.temp_Cells.remove(tmp_cell_item)
                                self.foundation_D.push(tmp_cell_item)
                                self.temp_Cells.append(0)
                                print("moved to foundation")

                    elif self.foundation_H.count != 0 and suits_dic['2'] == seled_Crd[-1]:
                        foundation_lst_card = self.foundation_H.peek()
                        if foundation_lst_card.get_suit() == suits_dic['2']:  #if suit is Heart
                            q = int(ranks_dic[seled_Crd[-3]])
                            z = int(ranks_dic[foundation_lst_card.get_rank()])
                            if int(ranks_dic[seled_Crd[-3]]) == int(ranks_dic[foundation_lst_card.get_rank()]) + 1:
                                self.temp_Cells.remove(tmp_cell_item)
                                self.foundation_H.push(tmp_cell_item)
                                self.temp_Cells.append(0)
                                print("moved to foundation")

                    elif self.foundation_C.count != 0 and suits_dic['3'] == seled_Crd[-1]:
                        foundation_lst_card = self.foundation_C.peek()
                        if foundation_lst_card.get_suit() == suits_dic['3']:  #if suit is Club
                            # q = int(ranks_dic[seled_Crd[-3]])
                            # z = int(ranks_dic[foundation_lst_card.get_rank()])
                            if int(ranks_dic[seled_Crd[-3]]) == int(ranks_dic[foundation_lst_card.get_rank()]) + 1:
                                self.temp_Cells.remove(tmp_cell_item)
                                self.foundation_C.push(tmp_cell_item)
                                self.temp_Cells.append(0)
                                print("moved to foundation")

                    elif self.foundation_S.count != 0 and suits_dic['4'] == seled_Crd[-1]:
                        foundation_lst_card = self.foundation_S.peek()
                        if foundation_lst_card.get_suit() == suits_dic['4']: # if suit is Spade
                            # q = int(ranks_dic[seled_Crd[-3]])
                            # z = int(ranks_dic[foundation_lst_card.get_rank()])
                            if int(ranks_dic[seled_Crd[-3]]) == int(ranks_dic[foundation_lst_card.get_rank()]) + 1:
                                self.temp_Cells.remove(tmp_cell_item)
                                self.foundation_S.push(tmp_cell_item)
                                self.temp_Cells.append(0)
                                print("moved to foundation")

            self.print_game()

    # used to move card from Slot,foundation or cascades to one empty cascade.
    def move_to_empty_cascade(self):
        print("cascades numbers are starting from 0 to 7 from Left to Right")
        src_card = input("which card you want to move to empty cascade? ").upper()
        dest_cascade = int(input("which cascade you want to move your selected card?"))

        # move from one cascade to empty cascade
        if len(self.cascades[dest_cascade]) == 0 and dest_cascade != '':
            for sublist in self.cascades:
                if len(sublist) != 0:
                    if sublist[-1].get_suit() == src_card[-1] and sublist[-1].get_rank() == src_card[-3]:
                        crd_to_emty_casc = sublist.pop()
                        self.cascades[dest_cascade].append(crd_to_emty_casc)
                        print("move to empty cascade done")
                        self.print_game()
                        return

            # move from temp_cells to empty cascade
            for tmpCell_item in self.temp_Cells:
                if tmpCell_item != 0:
                    if tmpCell_item.get_suit() == src_card[-1] and tmpCell_item.get_rank() == src_card[-3]:
                        self.cascades[dest_cascade].append(tmpCell_item)
                        self.temp_Cells.remove(tmpCell_item)
                        # we should add a 0 number to temcell for reserving space of [ ]
                        self.temp_Cells.append(0)
                        print("move from temp_cells to an empty cascade occured")
                        self.print_game()
                        return

            # Move from foundation to empty cascades
            foundation_S_lst_item = self.foundation_S.peek()
            if foundation_S_lst_item.get_suit() == src_card[-1] and foundation_S_lst_item.get_rank() == src_card[-3]:
                src_to_dest = self.foundation_S.pop()
                self.cascades[dest_cascade].append(src_to_dest)
                print("move from foundation to an empty cascade occured")
                self.print_game()

        else:
            print("Destination cascade is not empty")
            self.print_game()


    # the would create menu of the game
    def game_menu(self):
        print( "-" * 40 , "NOT-FREECELL MENU", "-" * 40 )
        print("1. MOVE ONE CARD FROM A CASCADE TO ANOTHER")
        print("2. MOVE CARD FROM A CASCADE TO FOUNDATION")
        print("3. MOVE CARD FROM A CASCADE TO TEMP-CELLS")
        print("4. MOVE CARD FROM TEMP-CELLS TO CASCADES")
        print("5. MOVE CARD FROM TEMP-CELLS TO FOUNDATION")
        print("6. MOVE TO EMPTY CASCADE")
        print("7. Exit")
        print("-" * 99 )

def main():
    game = notFreecell()
    game.fill_tableau()

    loop = True

    while loop:  ## While loop which will keep going until loop = False
        game.game_menu()  ## Displays menu
        choice = int(input("Enter your choice [1-7]: "))

        ## For moving cards from one cascade to anonther
        if choice == 1:
            print ("MOVE ONE CARD FROM A CASCADE TO ANOTHER is requested")
            game.cascades_move()
        ## MOVE ONE CARD TO FOUNDATION
        elif choice == 2:
            print("MOVE ONE CARD TO FOUNDATION")
            game.call_move_2_foundation()
        ## MOVE ONE CARD TO TEMP_CELLS
        elif choice == 3:
            print ("MOVE ONE CARD TO TEMP_CELLS")
            game.move_toTempCells()
        ## MOVE ONE CARD FROM TEMP_CELLS TO CASCADES
        elif choice == 4:
            print ("MOVE ONE CARD FROM TEMP_CELLS TO CASCADES")
            game.move_frmTempCell_to_Cascade()
        ## MOVE ONE CARD FROM TEMP_CELLS TO FOUNDATIONS
        elif choice == 5:
            print ("MOVE ONE CARD FROM TEMP_CELLS TO FOUNDATIONS")
            game.move_frmTempCell_to_Foundation()
        ## MOVE TO EMPTY CASCADE
        elif choice == 6:
            print("MOVE TO EMPTY CASCADE")
            game.move_to_empty_cascade()
        ## End of game
        elif choice == 7:
            print("EXIT GAME! Good Luck!")
        ## You can add your code or functions here
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
        # Any integer inputs other than values 1-7 we print an error message
            print ("Wrong option selected. Enter any key between 1-6 or 7 to EXIT..!")

if __name__ == "__main__":
    main()

