# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        self.face_down = False
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        if self.face_down:
            return "XX"
        else:
            return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
      
        if not self.face_down:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                          CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0] + 1, pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)
            

    def set_face_down(self, state):
        self.face_down = state
    
    def is_face_down(self):
        return self.face_down
        
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def __str__(self):
        hand_string = ""
        for card in self.cards:
            hand_string += str(card) + " "
        return  hand_string

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        self.value = 0
        for card in self.cards:
            if not card.is_face_down():
                self.value += VALUES[card.rank]
        for card in self.cards:
            if  card.get_rank() == "A" and (self.value + 10) <= 21:
                return self.value + 10
        return self.value

    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 10
            card.draw(canvas, pos)
    
    def flip_cards(self):
        for card in self.cards:
            card.set_face_down(False)
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card
    
    def __str__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += str(card) + " "
        return deck_string

deck = Deck()

#define event handlers for buttons
def deal():
    global outcome, in_play, dealers_hand, players_hand, deck, score
    outcome = "Hit or Stand?"
    if in_play:
        outcome = "You were already playing and now lost a point for giving up!"
        print outcome
        score -= 1
        in_play = False
    
    in_play = True
    deck.shuffle()
    dealers_hand = Hand()
    players_hand = Hand()	
    players_hand.add_card(deck.deal_card())
    players_hand.add_card(deck.deal_card())
    dealers_hand.add_card(deck.deal_card())
    dealers_second_card = deck.deal_card()
    dealers_second_card.set_face_down(True)
    dealers_hand.add_card(dealers_second_card)
    print "Dealer's hand " + str(dealers_hand)
    print "Player's hand " + str(players_hand) + " Value " + str(players_hand.get_value())
 
    if dealers_hand.get_value() == 21:
        dealers_hand.flip_cards()
        outcome = "Dealer gets Blackjack.  Dealer wins. Press the Deal button for a new game."
        score -=1
        in_play = False
        print outcome
        outcome = "No hand in play.  Press the Deal button for a new game."
        print outcome
    elif players_hand.get_value() == 21:
        dealers_hand.flip_cards()
        outcome = "Player gets Blackjack.  Dealer has chance to tie ( and win). Press Stand button to continue."
        print outcome
        

def hit():
    global in_play, score, outcome
    # if the hand is in play, hit the player
    if in_play:
        players_hand.add_card(deck.deal_card())
        print "Dealer's hand " + str(dealers_hand) 
        print "Player's hand " + str(players_hand) + " Value " + str(players_hand.get_value())
    # if busted, assign a message to outcome, update in_play and score
        if  players_hand.get_value() > 21 and in_play:
            outcome = "Player Busted and lost a point! New Deal?"
            print outcome
            in_play = False
            score -= 1
        elif players_hand.get_value() == 21 and in_play:
              outcome = "Player gets Blackjack.  Dealer has chance to tie (and win!). Press Stand button to continue."
        print outcome 
    else:
        outcome = "No hand in play.  Press the Deal button for a new game."
        print outcome
         
       
def stand():
    global in_play, score, outcome
    dealers_hand.flip_cards()
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealers_hand.get_value() < 17 and in_play:
        outcome = "Dealer hits"
        print outcome
        dealers_hand.add_card(deck.deal_card())
        print "Dealer's hand " + str(dealers_hand) + " Value " + str(dealers_hand.get_value())
        print "Player's hand " + str(players_hand) + " Value " + str(players_hand.get_value())
    if dealers_hand.get_value() > 21 and in_play:
        outcome = "Dealer Busted!  Press the Deal button for a new game."
        print outcome
        score +=1
        in_play = False
    else:
        if dealers_hand.get_value() >= players_hand.get_value() and in_play:
            outcome = "Dealer wins!  Press the Deal button for a new game."
            score -= 1
            print outcome
            in_play = False
        elif in_play:
            outcome = "Player wins!  Press the Deal button for a new game."
            print outcome
            score += 1
            in_play = False
        elif in_play == False:
            outcome = "No hand in play.  Press the Deal button for a new game."
        print outcome
# draw handler    
def draw(canvas):
    global outcome,  players_hand, dealers_hand
    canvas.draw_text("Blackjack",[30,50],40,"White")
    canvas.draw_text("Score "+str(score),[300,50],40,"White")
    
    canvas.draw_text("Dealer",[30,140],30,"White")
    canvas.draw_text("Showing " + str(dealers_hand.get_value()), [120, 140], 30, "White")
    #canvas.draw_text(str(dealers_hand), [300, 100], 30, "Red")
    dealers_hand.draw(canvas, [200,75])
    
    canvas.draw_text(outcome,[30,220],20,"Yellow")
    
    canvas.draw_text("Player",[30,300],30,"White")
    #canvas.draw_text(str(players_hand), [300, 200], 30, "Red")
    canvas.draw_text("Showing " + str(players_hand.get_value()), [120, 300], 30, "White")
    players_hand.draw(canvas, [200,250])
  
 
frame = simplegui.create_frame("Blackjack", 800, 400)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric