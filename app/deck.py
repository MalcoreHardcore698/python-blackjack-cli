import random

from card import Card

class Deck(object):
  def __init__(self):
    ranks = "23456789TJQKA"
    suits = "DCHS"

    # list generator creating a 52 card deck
    self.cards = [Card(r,s) for r in ranks for s in suits]

    # shuffle a deck
    random.shuffle(self.cards)

  def deal_card(self):
    """ Deals a card to the player """
    return self.cards.pop()
