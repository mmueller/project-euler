#!/usr/bin/env python

"""
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

The file, p54_input.txt, contains one-thousand random hands dealt to two
players.  Each line of the file contains ten cards (separated by a single
space): the first five are Player 1's cards and the last five are Player 2's
cards. You can assume that all hands are valid (no invalid characters or
repeated cards), each player's hand is in no specific order, and in each hand
there is a clear winner.

How many hands does Player 1 win?
"""

class Card:
    VALID_RANKS = '23456789TJQKA'
    VALID_SUITS = 'CDHS'

    def __init__(self, string):
        self.rank = string[0]
        self.suit = string[1]
        if not (self.rank in Card.VALID_RANKS and
                self.suit in Card.VALID_SUITS):
            raise Exception("Invalid card: " + string)
        self.rank_value = Card.VALID_RANKS.find(self.rank)

    def __str__(self):
        return self.rank + self.suit

    def __cmp__(self, other):
        "Comparison only supports rank. Suit is ignored."
        return cmp(self.rank_value, other.rank_value)

class PokerHandKind:
    HIGH_CARD       = 0
    PAIR            = 1
    TWO_PAIR        = 2
    THREE_OF_A_KIND = 3
    STRAIGHT        = 4
    FLUSH           = 5
    FULL_HOUSE      = 6
    FOUR_OF_A_KIND  = 7
    STRAIGHT_FLUSH  = 8

    @staticmethod
    def name(kind):
        return ["High Card", "Pair", "Two Pair", "Three of a Kind",
                "Straight", "Flush", "Full House", "Four of a Kind",
                "Straight Flush"][kind]

class PokerHand:
    def __init__(self, cards):
        if len(cards) != 5:
            raise Exception("Poker hands require 5 cards.")
        self.cards = sorted(cards)
        self.kind, pcards, rcards = self._compute_kind()
        self.value = self._compute_value(self.kind, pcards, rcards)

    def __str__(self):
        return '<PokerHand: %s %s (%d)>' % (
            ' '.join(map(str, self.cards)),
            PokerHandKind.name(self.kind),
            self.value)

    def __cmp__(self, other):
        "Compare two poker hands for win/loss/tie!"
        return cmp(self.value, other.value)

    def is_straight(self):
        values = map(lambda c: c.rank_value, self.cards)
        start = values[0]
        return values[1:] == [start+1, start+2, start+3, start+4]

    def is_flush(self):
        suits = map(lambda c: c.suit, self.cards)
        return all(s == suits[0] for s in suits)

    # "Private" functions

    def _compute_value(self, kind, pcards, rcards):
        "An integer value for the hand for comparison purposes."
        # Using base 16 we can lump all the interesting attributes into a
        # place value and just sum them.  If an attribute is more important
        # it will have a higher place value.
        exp = 5
        value = self.kind * 16**exp
        cards = list(reversed(sorted(pcards))) + list(reversed(sorted(rcards)))
        for card in cards:
            exp -= 1
            value += card.rank_value * 16**exp
        return value

    def _compute_kind(self):
        "Return tuple of (kind, participating cards, remaining cards)."
        values = map(lambda c: c.rank_value, self.cards)
        # Straight flush
        if self.is_straight() and self.is_flush():
            return (PokerHandKind.STRAIGHT_FLUSH, self.cards, [])
        # Four of a kind
        if values[0] == values[1] == values[2] == values[3]:
            return (PokerHandKind.FOUR_OF_A_KIND,
                    self.cards[:4], [self.cards[4]])
        if values[1] == values[2] == values[3] == values[4]:
            return (PokerHandKind.FOUR_OF_A_KIND,
                    self.cards[1:], [self.cards[0]])
        # Full house
        if ((values[0] == values[1] == values[2] and values[3] == values[4]) or
            (values[0] == values[1] and values[2] == values[3] == values[4])):
            return (PokerHandKind.FULL_HOUSE, self.cards, [])
        # Flush
        if self.is_flush():
            return (PokerHandKind.FLUSH, self.cards, [])
        # Straight
        if self.is_straight():
            return (PokerHandKind.STRAIGHT, self.cards, [])
        # Three of a kind
        if (values[0] == values[1] == values[2]):
            return (PokerHandKind.THREE_OF_A_KIND,
                    self.cards[0:3], self.cards[3:])
        if (values[1] == values[2] == values[3]):
            return (PokerHandKind.THREE_OF_A_KIND,
                    self.cards[1:4], [self.cards[0], self.cards[4]])
        if (values[2] == values[3] == values[4]):
            return (PokerHandKind.THREE_OF_A_KIND,
                    self.cards[2:5], self.cards[:2])
        # Two pair
        if values[0] == values[1] and values[2] == values[3]:
            return (PokerHandKind.TWO_PAIR, self.cards[0:4], [self.cards[4]])
        if values[0] == values[1] and values[3] == values[4]:
            return (PokerHandKind.TWO_PAIR,
                    self.cards[0:2]+self.cards[3:], [self.cards[2]])
        if values[1] == values[2] and values[3] == values[4]:
            return (PokerHandKind.TWO_PAIR, self.cards[1:], [self.cards[0]])
        # Pair
        for i in range(0, 4):
            if values[i] == values[i+1]:
                return (PokerHandKind.PAIR,
                        self.cards[i:i+2], self.cards[:i]+self.cards[i+2:])
        # High card
        return (PokerHandKind.HIGH_CARD, [], self.cards)

def run_poker_games(filename):
    games = p1wins = p2wins = 0
    for line in open(filename, 'r').readlines():
        cards = map(Card, line.strip().split(' '))
        hand1 = PokerHand(cards[:5])
        hand2 = PokerHand(cards[5:])
        result = cmp(hand1, hand2)
        games += 1
        print 'Game %d:' % games
        if result < 0:
            print '  LOSER: ', hand1
            print '  WINNER:', hand2
            p2wins += 1
        elif result > 0:
            print '  WINNER:', hand1
            print '  LOSER: ', hand2
            p1wins += 1
        else:
            print '  TIE:', hand1
            print '  TIE:', hand2
    print ''
    print '  Total games:', games
    print 'Player 1 wins:', p1wins
    print 'Player 2 wins:', p2wins
    print '         Ties:', games - p1wins - p2wins

if __name__ == '__main__':
    run_poker_games('p54_input.txt')
