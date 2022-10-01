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
        if card.rank == 'Ace':
            self.aces += 1
        self.cards.append(card)
        self.value += values[card.rank]
        if self.value > 21 and self.aces > 0:
            self.adjust_for_ace()

    def adjust_for_ace(self):
        adjusted_value = 0
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
            chips.bet = bet
            return
        else:
            print(f'Bet has to be between 1 ... {chips.total}. Try again')

def hit(deck,hand):

    hand.add_card(deck.deal())


def hit_or_stand():

    while player.value <= 21:
        reply = input('(H)it or (S)tand: ').upper()
        if reply == 'H':
            print('Player hits.')
            hit(deck, player)
            print('\nDealer hand: ')
            dealer.show(all=False)
            print('\nPlayer hand: ')
            player.show(all=True)
        elif reply == 'S':
            print('Player stands.')
            break

def player_busts(player_chips):
    print('Player busts.')
    player_chips.lose_bet()

def player_wins(player_chips):
    print('Player wins.')
    player_chips.win_bet()

def dealer_busts(player_chips):
    print('Dealer busts.')
    player_chips.win_bet()

def dealer_wins(player_chips):
    print('Dealer wins')
    player_chips.lose_bet()

def push(player_chips):
    print('Push. Returning bet.')
    player_chips.bet = 0


#### GAME LOGIC
# Print an opening statement

print('Welcome to Blackjack!')

# Set up the Player's chips
player_chips = Chips()

while True:



    while playing:  # recall this variable from our hit_or_stand function

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        for i in range(2):
            hit(deck, player)
            hit(deck, dealer)

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        print('\nDealer hand: ')
        dealer.show(all=False)
        print('\nPlayer hand: ')
        player.show(all=True)
            
        # Prompt for Player to Hit or Stand
        hit_or_stand()

        # Show cards (but keep one dealer card hidden)
        print('\nDealer hand: ')
        dealer.show(all=False)
        print('\nPlayer hand: ')
        player.show(all=True)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value < 17:
            hit(deck, dealer)
        # Show all cards
        print('\nDealer hand: ')
        dealer.show(all=True)
        print('\nPlayer hand: ')
        player.show(all=True)
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player_chips)
        elif dealer.value > player.value:
            dealer_wins(player_chips)
        elif dealer.value < player.value:
            player_wins(player_chips)
        else:
            push(player_chips)

        # Inform Player of their chips total
        print(f'You have {player_chips.total} chips.')
        # Ask to play again
        while True:
            replay = input('Replay? (Y)es or (N)o: ').upper()
            if replay == 'Y':
                print('Continuing.')
                playing = True
                break
            elif replay == 'N':
                print('Quitting.')
                playing = False
                break
