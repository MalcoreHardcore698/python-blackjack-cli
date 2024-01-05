from deck import Deck
from hand import Hand

from helpers import print_separator

def new_game():
  # creating a deck
  d = Deck()

  # set "hands" for player and dealer
  player_hand = Hand("Player")
  dealer_hand = Hand("Dealer")

  # deal two cards to the player
  player_hand.add_card(d.deal_card())
  player_hand.add_card(d.deal_card())

  # deal one card to dealer
  dealer_hand.add_card(d.deal_card())

  print_separator()

  print(player_hand)

  # shall we keep playing?
  in_game = True

  # it only makes sense for a player to have fewer than 21 points
  while player_hand.get_value() < 21:
    print("\n")

    ans = input("Hit or stand? (h/s) ")

    if ans == "h":
      player_hand.add_card(d.deal_card())
      print(player_hand)

      if player_hand.get_value() > 21:
        print("END: You lose\n")
        in_game = False
        new_game()
    else:
      print("END: You stand!\n")
      new_game()
      break

  print_separator()

  if in_game:
    # the dealer to draw cards
    while dealer_hand.get_value() < 17:
      dealer_hand.add_card(d.deal_card())
      print(dealer_hand)

      # the player wins because the dealer has too much
      if dealer_hand.get_value() > 21:
        print ("END: Dealer bust")
        in_game = False
        new_game()

  if in_game:
    # no one had too much - compare the number of points of the player and dealer
    if player_hand.get_value() > dealer_hand.get_value():
      print("END: You win\n")
      new_game()
    else:
      print("END: Dealer win\n")
      new_game()

def main():
  answer = input("Did you want play in Blackjack? (y/n)\nAnswer: ")

  print()

  if answer == "y":
    new_game()

  input("Game has been closed!\nEnter any key...")

if __name__ == '__main__':
  main()
