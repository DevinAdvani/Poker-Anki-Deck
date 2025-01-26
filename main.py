from itertools import combinations

# Make a deck

deck = []
suits = ["C", "H", "D", "S"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

for i in range(0,4):
    for j in range(0,13):
        deck.append([values[j], suits[i]])

# Make card rankings

card_rankings = []

# Straight Flushes
for i in range(0,9):
    card_rankings.append([deck[8-i:13-i], deck[21-i:26-i], deck[34-i:39-i], deck[47-i:52-i]])

# Four of a Kind
for i in range(0,13):
    level = []
    for j in range(0,52):
        if ((j != 12-i) and (j != 25-i) and (j != 38-i) and (j != 51-i)):
            level.append([deck[12-i], deck[25-i], deck[38-i], deck[51-i], deck[j]])
    card_rankings.append(level)

# Full House

for i in range(0,13):
    for j in range(0,13):
        if (i != j):
            level = []
            positions = [12, 25, 38, 51]
            threes = list(combinations(positions, 3))
            twos = list(combinations(positions, 2))
            for k in range(0,4):
                for l in range(0,6):
                    level.append([deck[threes[k][0]-i], deck[threes[k][1]-i], deck[threes[k][2]-i], deck[twos[l][0]-j], deck[twos[l][1]-j]])
            card_rankings.append(level)

# Flush

# Straight

# Three of a Kind

# Two Pair

# Pair

# High Card

# Cycle through all possible dealings


for x in card_rankings:
    print(x)
    print(" ")
