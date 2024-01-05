class Hand():
  def __init__(self, name):
    # player name
    self.name = name

    # player hand
    self.cards = []

  def add_card(self, card):
    """ Adds a card to the hand """

    self.cards.append(card)

  def get_value(self):
    """ Gets number of points in the hand """

    result = 0

    # count of aces on the hand.
    aces = 0
    for card in self.cards:
      result += card.card_value()

      # increase the number of aces
      if card.get_rank() == "A":
        aces += 1

    # counting aces for 1 point or 11
    if result + aces * 10 <= 21:
      result += aces * 10

    return result

  def __str__(self):
    text = "%s's contains:\n" % self.name

    for card in self.cards:
      text += str(card) + " "
    text += "\nHand value: " + str(self.get_value())

    return text
