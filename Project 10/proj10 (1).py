import cards        # this is required

YAY_BANNER = """
__   __             __        ___                       _ _ _ 
\ \ / /_ _ _   _    \ \      / (_)_ __  _ __   ___ _ __| | | |
 \ V / _` | | | |    \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | | |
  | | (_| | |_| |_    \ V  V / | | | | | | | |  __/ |  |_|_|_|
  |_|\__,_|\__, ( )    \_/\_/  |_|_| |_|_| |_|\___|_|  (_|_|_)
           |___/|/                                            

"""

RULES = """
    *------------------------------------------------------*
    *-------------* Thumb and Pouch Solitaire *------------*
    *------------------------------------------------------*
    Foundation: Columns are numbered 1, 2, ..., 4; built 
                up by rank and by suit from Ace to King. 
                You can't move any card from foundation, 
                you can just put in.

    Tableau:    Columns are numbered 1, 2, 3, ..., 7; built 
                down by rank only, but cards can't be laid on 
                one another if they are from the same suit. 
                You can move one or more faced-up cards from 
                one tableau to another. An empty spot can be 
                filled with any card(s) from any tableau or 
                the top card from the waste.
     
     To win, all cards must be in the Foundation.
"""

MENU = """
Game commands:
    TF x y     Move card from Tableau column x to Foundation y.
    TT x y n   Move pile of length n >= 1 from Tableau column x 
                to Tableau column y.
    WF x       Move the top card from the waste to Foundation x                
    WT x       Move the top card from the waste to Tableau column x        
    SW         Draw one card from Stock to Waste
    R          Restart the game with a re-shuffle.
    H          Display this menu of choices
    Q          Quit the game
"""

def valid_fnd_move(src_card, dest_card):
    """
        Checks for the suit and the rank of the source card and the destination\
        card. If both pass conditions move will be valid. 
    """
    if dest_card is None: 
        if src_card.value() == 1:
            return True
    else:
        if src_card is not None:
            if src_card.suit() == dest_card.suit() and \
               src_card.rank()- dest_card.rank() == 1:
                   return True
            else:
                return False
        else:
             return False
            


def valid_tab_move(src_card, dest_card):
    """
        Check that suit of source card and destination card are not the same. \
        And the rank of source card must be one less than destination card. 
    """
    
    if src_card != None: 
        if dest_card == None:
            if src_card.rank() == 13:
                return True
            else:
                return False
        elif src_card.suit() != dest_card.suit(): # suit of cards cannot be the same
            if dest_card.rank() == src_card.rank()+1: #src card must be one less
                return True
            else:
                return False
        else:
            return False 
    else:
        return False #if they are the same suit, move invalid

  
def tableau_to_foundation(tab, fnd):
    """
        Will move a single card, determines if the move is valid from valid_fnd\
        _move(). If move invalid, proper error message will display.
    """
    if len(tab)>=1:
        src = tab[-1]
    else:
        src = None
    if len(fnd) >= 1:
        dest = fnd[-1]
    else:
        dest = None
    print(src)
    print(dest)
    if valid_fnd_move(src, dest):
        fnd.append(src) #adds the source card to the foundation
        tab.pop()
        if len(tab) >= 1:
            #if not tab[-1].is_flip_up():
            tab[-1].flip_card()
                #checks whether the card left is flipped up or down and flips it\
                #   if its not flipped up

    else:
        raise RuntimeError ("Invalid Move")
            
    
        
      # stub; delete and replace it with your code
            

def tableau_to_tableau(tab1, tab2, n):
    """
        Will move a card (or a set of cards) from one tableau column to another\
        tableau column. 
        
    """  
    
    if n >=1:# and tab1 >= 0 and tab1 <= 6 and tab2 >= 0 and tab2 <= 6:       
        if len(tab1) >=n:
            src = tab1[-n]
            src_list = tab1[-n:]
        else:
            src = None
            
        if len(tab2) >= 1:
            dest = tab2[-1]
            
        else:
            dest = None
        if valid_tab_move(src,dest):
            tab2.extend(src_list)
            #tab1 = tab1[0:-n]
            for i in range(n):
                tab1.pop()
            
            if len(tab1) >= 1:
                #if not tab[-1].is_flip_up():
                tab1[-1].flip_card()
            
        else:
            raise RuntimeError ("Invalid Move")
            
    else:
       raise RuntimeError ("Invalid Input")
    
    
def waste_to_foundation(waste, fnd, stock):
    """
        add your function header here.
    """   
    src_card = waste[-1]
    
    if len(fnd) >= 1:
        dest_card = fnd[-1]
            
    else:
        dest_card = None
            
    if valid_fnd_move(src_card, dest_card) == True:
        l=waste.pop(-1)
        fnd.append(l)
        #waste.append(stock.deal())
        
    else:
        raise RuntimeError ("Invalid Move")
    
      # stub; delete and replace it with your code

def waste_to_tableau(waste, tab, stock):
    """
        add your function header here.
    """    
    src_card = waste[-1]
    
    if len(fnd) >= 1:
        dest_card = fnd[-1]
            
    else:
        dest_card = None
            
    if valid_tab_move(src_card, dest_card) == True:
        j = waste.pop(-1)
        tab.append(j)
        waste.append(stock.deal())
    else:
        raise RuntimeError("Invalid Move")
        # stub; delete and replace it with your code
                    
def stock_to_waste(stock, waste):
    """
        add your function header here.
    """    
    if len(stock) >= 1:
        waste.append(stock.deal())
    else:
        raise RuntimeError ("Move Invalid")
        
    # stub; delete and replace it with your code
                            
def is_winner(tableau, stock, waste):
    """
        add your function header here.
    """    
    # stub; delete and replace it with your code
    for row in range(0,7):
        for columns in range (row +1, 7):
            if tableau[columns] == None:
                return True
            else:
                return False
            if stock == None:
                return True
            else:
                return False
            if waste == None:
                return True
            else: 
                return False
    if tableau[columns] == None and stock == None and waste == None:
        print(YAY_BANNER)
        return True
    else:
        return False

#    if len(foundation) == 52:
#        print(YAY_BANNER)
def setup_game():
    """
        The game setup function, it has 4 foundation piles, 7 tableau piles, 
        1 stock and 1 waste pile. All of them are currently empty. This 
        function populates the tableau and the stock pile from a standard 
        card deck. 

        7 Tableau: There will be one card in the first pile, two cards in the 
        second, three in the third, and so on. The top card in each pile is 
        dealt face up, all others are face down. Total 28 cards.

        Stock: All the cards left on the deck (52 - 28 = 24 cards) will go 
        into the stock pile. 

        Waste: Initially, the top card from the stock will be moved into the 
        waste for play. Therefore, the waste will have 1 card and the stock 
        will be left with 23 cards at the initial set-up.

        This function will return a tuple: (foundation, tableau, stock, waste)
    """
    # you must use this deck for the entire game.
    # the stock works best as a 'deck' so initialize it as a 'deck'
    stock = cards.Deck()
    # the game piles are here, you must use these.
    foundation = [[], [], [], []]           # list of 4 lists
    tableau = [[], [], [], [], [], [], []]  # list of 7 lists
    waste = []                              # one list
    # your setup code goes here
    stock.shuffle()
    for row in range(0,7):
        deal = stock.deal()
        tableau[row].append(deal)
        for column in range (row +1,7):
            deal = stock.deal()
            deal.flip_card()
            tableau[column].append(deal)
    #waste.append(stock.deal())
    
#    print(tableau)
#    print(waste)
    
    return foundation, tableau, stock, waste

def display_game(foundation, tableau, stock, waste):
    """
        add your function header here.
    """    
    print("=================== FOUNDATIONS ==================")
    print("{0:9} {1:9}{2:9}{3:9}".format('f1','f2','f3','f4'))
    #print("f1         f2        f3       f4".format())
    
    f1 = str(foundation[0])
    f2 = str(foundation[1])
    f3 = str(foundation[2])
    f4 = str(foundation[3])

#    foundation = [[], [], [], []] 
#    print("{0:9} {1:9}{2:9}{3:9}".format(fnd))
    
    print("{:9}{:9}{:9}{:9}".format(f1,f2,f3,f4))
    
    print("==================== TABLEAU =====================")
        
    t1 = tableau[0]
    t2 = tableau[1]
    t3 = tableau[2]
    t4 = tableau[3]
    t5 = tableau[4]
    t6 = tableau[5]
    t7 = tableau[6]
    tab = t1, t2, t3, t4, t5, t6, t7

#    for t in tab:
#        print("{} {} {} {} {} \n{} \n{} ".format(t1,t2[1],t3[2],t4[3],t5[4],t6[5],t7[6]))
#        tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6]
#        {} {} {} {} {} {}
#        t1,t2, t3, t4, t5, t6, t7
    print("[{}".format(t1))    
    print(" {}".format(t2))
    print(" {}".format(t3))
    print(" {}".format(t4))
    print(" {}".format(t5))
    print(" {}".format(t6))
    print(" {}]".format(t7))
    
    print("=================== STOCK/WASTE ==================")
    k=len(stock)
    print("Stock #(",k,")","-->",waste)
    
    
    return fnd, tab, stock, waste
      # stub; delete and replace it with your code






print(RULES)
fnd, tab, stock, waste = setup_game()
display_game(fnd, tab, stock, waste)
print(MENU)
command = input("prompt :> ")
while command.strip().lower() != 'q':
    command_lst = command.strip().lower().split()
    try:
        if command.lower() == 'h':
            print (MENU)
        elif command.lower() == 'r':
            fnd, tab, stock, waste = setup_game()
        elif command.lower() == 'sw':
            stock_to_waste(stock, waste)
            
        elif command_lst[0].lower() == 'tf':
            x = int(command_lst[1])
            if x in range(1,8):
                x = int(command_lst[1])-1
            else:
                raise RuntimeError ("Tab input out of range")
            y = int(command_lst[2])
            if y in range (0,5):          
                y = int(command_lst[2])-1
            else:
                raise RuntimeError ("Fnd input y out of range")
                
            tableau_to_foundation(tab[x],fnd[y])
            
        elif command_lst[0].lower() == 'tt':
            if x in range(1,8):
                x = int(command_lst[1])-1
            else:
                raise RuntimeError ("Tab1 input out of range")
                
            if y in range(0,8):
                y = int(command_lst[2])-1
            else:
                raise RuntimeError ("Tab2 input out of range")
            
            n = int(command_lst[3])
            tableau_to_tableau(tab[x],tab[y],n)
            
#########################          
        elif command_lst[0].lower() == 'wf':
            
            if x in range(0,5):
                x = int(command_lst[1])-1
            else:
                raise RuntimeError ("Fnd input out of range")
            
            waste_to_foundation(waste, fnd[x], stock)
   
        elif command_lst[0].lower() == 'wt':           
            x = int(command_lst[1])-1       
            waste_to_tableau(waste,tab[x],stock)


            
        
        
        
    
    #pass  # stub; delete and replace it with your code
    
    except RuntimeError as error_message: # any RuntimeError you raise lands here
        
        print("{:s} Error: invalid command because of \nTry again.".format(str\
        (error_message)))       
    display_game(fnd, tab, stock, waste)                
    command = input("prompt :> ")





'''
Questions:


waste to tableau
is winner correct?

How to format into columns
how to format foundation to only display top card instead of all cards
-how to display error message after the string

'''