# implementation of card game - Memory

import simplegui
import random

WIDTH = 800
HEIGHT = 100
TOTAL_CARDS = 16
CARD_WIDTH = WIDTH // TOTAL_CARDS


# helper function to initialize globals
def new_game():
    global exposed_cards, state, turns, deck
    global index_of_first_chosen_card, index_of_second_chosen_card
    index_of_first_chosen_card = -1
    index_of_second_chosen_card = -1
    turns = 0
    state = 0  #State 0 corresponds to the start of the game. 
    print "Start game"
    
    exposed_cards = []
    for card in range(TOTAL_CARDS):
        exposed_cards.append(False)
    deck = []
    for card in range(TOTAL_CARDS / 2):
        deck.append(card)
    deck += deck
    random.shuffle(deck)
    turn_label.set_text("Turns = " + str(turns))

def mouseclick(pos):
    global exposed_cards, state, deck, turns
    global index_of_first_chosen_card, index_of_second_chosen_card
    click_position = list(pos)
    chosen_card_index = click_position[0] // CARD_WIDTH
    
    if exposed_cards[chosen_card_index] == False:  #Ignore exposed card
        
        
        #In state 0 if you click on a card, that card is exposed, and you switch to state 1
        if state <= 0:
            exposed_cards[chosen_card_index] = True
            index_of_first_chosen_card = chosen_card_index
            state = 1
  
        elif state == 1:
            
            #State 1 corresponds to a single exposed unpaired card.
            #In state 1, if you click on an unexposed card, that card is exposed and you switch to state 2
            exposed_cards[chosen_card_index] = True
            turns += 1
            turn_label.set_text("Turns = " + str(turns))
            index_of_second_chosen_card = chosen_card_index
            state = 2
        
        #State 2 corresponds to the end of a turn. In state 2, if you click on an unexposed card, that card is exposed and you switch to state 1.
        else:
            if deck[index_of_first_chosen_card] == deck[index_of_second_chosen_card]:
                print "Match!!"
                exposed_cards[index_of_first_chosen_card] = True
                exposed_cards[index_of_second_chosen_card] = True
                index_of_second_chosen_card = -1
  
            else:
                print "No Match"
                exposed_cards[index_of_first_chosen_card] = False
                exposed_cards[index_of_second_chosen_card] = False
                index_of_first_chosen_card = -1
                index_of_second_chosen_card = -1
            state = 1
            exposed_cards[chosen_card_index] = True
            index_of_first_chosen_card = chosen_card_index
            
        
    else:
        print "That card is already face up"


def draw(canvas):
   for i in range(TOTAL_CARDS):
        if exposed_cards[i]:
            canvas.draw_text(str(deck[i]), [CARD_WIDTH * i + WIDTH / 60, HEIGHT / 2], 60, "White")
        else:
            canvas.draw_polygon([(i*CARD_WIDTH,0),((i+1)*CARD_WIDTH,0),((i+1)*CARD_WIDTH,HEIGHT),(i*CARD_WIDTH,HEIGHT),(i*CARD_WIDTH,0)],1,"White","Red")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory",WIDTH , HEIGHT)
frame.add_button("Reset", new_game)
turn_label = frame.add_label("Turns = 0")

# register event handler
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric