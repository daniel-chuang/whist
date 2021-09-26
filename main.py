from functions import makeDeck, printDeck, printCard, compareCards, printSuit
import random
from termcolor import colored

# https://repl.it/@DanielChuang1/wist3#main.py
# Added the feature to make sure that people are playing suits of the same type if possible, added "continue" breaks so that players dont see each other's hands

deck = makeDeck() # Makes a deck
random.shuffle(deck) # Shuffles the deck
faceCards = {"J" : 11, "Q" : 12, "K": 13, "A" : 14} # Declares facecard values

samps = random.sample(range(52), 13)
hand1 = [deck[x] for x in samps] # Creates a hand of 13 cards for player 1 randomly
for i in hand1: # Removes the cards in the hand from the deck
  deck.remove(i)

samps = random.sample(range(39), 13)
hand2 = [deck[x] for x in samps] # Creates a hand of 13 cards for player 2 randomly
for i in hand2: # Removes the cards in the hand from the deck
  deck.remove(i)

# Printing the trump for the first round
trump = deck[0][0]
print("The rules for this game:")
print("Two players have 13 random cards each, and the deck has 26 cards (which adds up to 52). The top card of the deck is flipped, and the suit of that card is the trump for the rest of the game. From there on, each player takes turns playing cards (whoever won the last round gets to go first), to compete for the top card of the deck. The player who plays a card with the higher value wins the top card and puts it in their hand, while the runner up gets the card underneathed the revealed card. Then, another card is flipped and this process is repeated until there are no more cards in the deck.")
print("\nCards are compared using their numerical value (2 is the smallest, A is the largest). The player going second in the round must play a card of the same suit as the first player, if they can, unless they choose a trump. Trumps automatically win over any other suit.")
print("\nAfter there are no more cards in the deck, and each player has a new set of 13 cards, the same process of playing cards and comparing them is repeated, but instead of cards, they recieve points. This repeats until both players have played all 13 cards in their hand. The player with the most points at the end wins the game.\n")
input("Press enter to continue. ")
print("\033[H\033[J")
print(colored("General Information", "green"), end="\n\n")
print("The top card of the deck has been revealed: ", end="")
printCard(deck[0])
print("The trump for this game is ", end="")
printSuit(deck[0][0]) 
print("\nYou can input card by typing the first character of their suit, and then the value of the card (eg: C5 for ♧ 5, and HK ♡ K.)\n")
input("Make sure Player 2 is looking away, then press enter to continue. ")
print("\033[H\033[J")

handDict = {1 : hand1, 2 : hand2}

def revealTop():
  print("The top card of the deck has been revealed: ", end="")
  printCard(deck[0], ending="\n\n")

def turn(playernum, cardPlayed=["", ""]):
  print("Player %s's hand: " % (playernum) + str(len(handDict[playernum])))
  printDeck(handDict[playernum])
  print("\nThe card in contest is: ", end="")
  printCard(deck[0])

  card = " "
  handMod = [handDict[playernum][x][0] + str(handDict[playernum][x][1]) for x in range(len(handDict[playernum]))]

  suitInHand = False
  if cardPlayed != ["", ""]:
    for i in handMod:
      if i[0] == cardPlayed[0]:
        suitInHand = True

  while card not in handMod:
    card = input("\nWhich card would you like to play?\n").upper()
    
    if cardPlayed != ["", ""] and cardPlayed[0] != card[0] and suitInHand == True and card[0] != trump:
      card = input("\nYou must choose a card of the same suit as the played card if possible, as long as the suit of the card you played is not a trump. \n").upper()
    
    if card[1:] in faceCards.keys():
      card = card[0] + str(faceCards[card[1:]])

  cardIndex = handMod.index(card)
  cardReturn = handDict[playernum][cardIndex]
  print(cardReturn)
  del(handDict[playernum][cardIndex])
  print("\033[H\033[J")
  return(cardReturn)

# first stage
winPlayer = 1 # the winner of the last turn goes first
while len(deck) != 0:
  if winPlayer == 1:
    revealTop()
    card1 = turn(1)
    input("Make sure Player 1 is looking away, then press enter to continue. ")
    print("\033[H\033[J")
    revealTop()
    print("Player 1 played ", end="")
    printCard(card1)
    card2 = turn(2, card1)
  else:
    revealTop()
    card2 = turn(2)
    input("Make sure Player 1 is looking away, then press enter to continue. ")
    print("\033[H\033[J")
    revealTop()
    print("Player 2 played ", end="")
    printCard(card2)
    card1 = turn(1, card2)

  # Distribute Cards
  winCard, winPlayer = compareCards(card1, card2, trump)
  if winPlayer == 1:
    hand1.append(deck[0])
    hand2.append(deck[1])
    print("Player 1 won that round and got ", end="")
    printCard(deck[0])
    print("Player 2 got a secret card...", end="\n\n")
    print("Both cards are the last card in their respective player's hand.")
  else:
    hand1.append(deck[1])
    hand2.append(deck[0])
    print("Player 2 won that round and got ", end="")
    printCard(deck[0])
    print("Player 1 got a secret card...", end="\n\n")
    print("Both cards are the last card in their respective player's hand.")
  del(deck[0:2])
  input("The winner of this round, Player %s, will go first on the next round. Make sure Player %s is looking away, then press enter to continue. " % (winPlayer, str(3-int(winPlayer))))
  print("\033[H\033[J")

points1, points2 = 0, 0
# second stage
while len(deck) != 0:
  if winPlayer == 1:
    revealTop()
    card1 = turn(1)
    input("Make sure Player 1 is looking away, then press enter to continue. ")
    print("\033[H\033[J")
    revealTop()
    print("Player 1 played ", end="")
    printCard(card1)
    card2 = turn(2, card1)
  else:
    revealTop()
    card2 = turn(2)
    input("Make sure Player 2 is looking away, then press enter to continue. ")
    print("\033[H\033[J")
    revealTop()
    print("Player 2 played ", end="")
    printCard(card2)
    card1 = turn(1, card2)

  # Distribute Points
  winCard, winPlayer = compareCards(card1, card2, trump)
  if winPlayer == 1:
    points1 += 1
  else:
    points2 += 1
  input("The winner of this round, Player %s, will go first on the next round. Make sure Player %s is looking away, then press enter to continue. " % (winPlayer, str(3-int(winPlayer))))
  print("\033[H\033[J")

print(points1, points2)