class Card():
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def card_value(self):
    if self.rank in "TJQK":
      # 10 for ten, jack, lady and king
      return 10
    else:
      # the number of points for any other card
      return " A23456789".index(self.rank)

  def get_rank(self):
    return self.rank

  def __str__(self):
    return "%s%s" % (self.rank, self.suit)
