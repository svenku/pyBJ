#### Game "skeleton" opyright by Pierian Data (Udemy course on Python)

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        print('Deck contains : ' + str(len(self.deck)) + ' cards.' )
        contents = ''
        for card in self.deck:
            contents += str(card) + ', '
        return contents[:-2] + '. '

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        adjusted_value = 0
        if self.value > 21:
            for card in self.cards:
                if card.rank == 'Ace':
                    adjusted_value += 1
                else:
                    adjusted_value += values[card.rank]
            print(f'Adjusted hand value from {self.value} to {adjusted_value}.')
            self.value = adjusted_value

    def show(self, all=True):

        print(f'Hand contains : {str(len(self.cards))} cards.')

        if len(self.cards) == 0:
            return

        if all==False:
            print(f'Hand value: {self.value - values[self.cards[0].rank]}')
            contents = '********** '
        else:
            print(f'Hand value: {self.value}')
            contents = str(self.cards[0]) + ' '

        for i in range(1,len(self.cards)):
            contents += str(self.cards[i]) + ' '

        print(contents)

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        bet = input(f'{chips.total} chips left. Enter bet amount: ')
        try:
            bet = int(bet)

        except ValueError:
            print(f'Please enter integer value between 1 ... {chips.total}')
            continue

        if 1 <= bet <= chips.total:
            return bet
        else:
            print(f'Bet has to be between 1 ... {chips.total}. Try again')

def hit(deck,hand):

    hand.add_card(deck.deal())


def hit_or_stand(deck,hand):
    global playing

    while True:
        reply = input('(H)it or (S)tand: ').upper()
        if reply == 'H':
            hit(deck, hand)
        elif reply == 'S':
            playing = False
            break

def player_busts():
    print('Player busts.')
    player_chips.lose_bet()

def player_wins():
    print('Player wins.')
    player_chips.win_bet()

def dealer_busts():
    pass

def dealer_wins():
    pass

def push():
    pass


#### GAME LOGIC

while True:
    # Print an opening statement
    print('Welcome to Blackjack!')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    for i in range(2):
        hit(deck, player)
        hit(deck, dealer)

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    print('Dealer hand: ')
    dealer.show(all=False)
    print('Player hand: ')
    player.show(all=True)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # Show cards (but keep one dealer card hidden)
        print('Dealer hand: ')
        dealer.show(all=False)
        print('Player hand: ')
        player.show(all=True)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts()
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while dealer.value < 17:
    
        hit(deck, dealer)
        # Show all cards
        print('Dealer hand: ')
        dealer.show(all=True)
        print('Player hand: ')
        player.show(all=True)
        # Run different winning scenarios
        

    # Inform Player of their chips total

    # Ask to play again

        #break
