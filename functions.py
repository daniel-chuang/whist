import random # importing the random package for the shuffle() function (shuffling has to be random, right?)
from termcolor import colored
# ["♢", "♤", "♡", "♧"] different suits


print("\033[H\033[J") # Clear terminal

def makeDeck():
  deck = [[suit, i] for suit in ["D", "S", "H", "C"] for i in range(2, 15)]
  return(deck)

def printSuit(suit):
  suits = {"D" : "♢", "S" : "♤", "H" : "♡", "C" : "♧"}
  suit = suits[suit]
  if suit in ["♢", "♡"]:
    print(colored(suit, "red"))
  else: 
    print(colored(suit, "blue"))
  

def printCard(card, ending="\n"):
  faceCards = {11 : "J", 12 : "Q", 13 : "K", 14 : "A"}
  suits = {"D" : "♢", "S" : "♤", "H" : "♡", "C" : "♧"}
  if card[0] in ["S", "C"]:
    if card[1] in [11, 12, 13, 14]:
      print(colored (suits[card[0]] + " " + str(faceCards[card[1]]) + " ", "blue"), end=ending)
    else:
      print(colored (suits[card[0]] + " " + str(card[1]), "blue") + " " * (2-len(str(card[1]))), end=ending)
  else:
    if card[1] in [11, 12, 13, 14]:
      print(colored (suits[card[0]] + " " + str(faceCards[card[1]]), "red"), end=ending)
    else:
      print(colored (suits[card[0]] + " " + str(card[1]), "red") + " " * (2-len(str(card[1]))), end=ending)

def printDeck(deck):
  for i in deck: # prints the deck
    printCard(i, "  ")


def compareCards(card1, card2, trump):
  print("Player 1 Played: ", end="")
  printCard(card1, ending=" | ")
  print("Player 2 Played: ", end="")
  printCard(card2)
  if card1[0] == trump and card2[0] != trump: # if only card 1 is a trump
    return(card1, 1)
  elif card2[0] == trump and card1[0] != trump: # if only card 2 is a trump
    return(card2, 2)
  elif card1[0] != card2[0]: # if card2 isn't the same suit
    return(card1, 1)
  elif card1[1] > card2[1]: # if card1 is greater than card2
    return(card1, 1)
  else:
    return(card2, 2)