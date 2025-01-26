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
            level.append([deck[12-i], deck[25-i], deck[38-i], deck[12-j], deck[25-j]]) # no 51
            level.append([deck[12-i], deck[38-i], deck[51-i], deck[12-j], deck[25-j]]) # no 25
            level.append([deck[12-i], deck[25-i], deck[51-i], deck[12-j], deck[25-j]]) # no 38
            level.append([deck[51-i], deck[25-i], deck[38-i], deck[12-j], deck[25-j]]) # no 12

            level.append([deck[12-i], deck[25-i], deck[38-i], deck[12-j], deck[38-j]]) # no 51
            level.append([deck[12-i], deck[38-i], deck[51-i], deck[12-j], deck[38-j]]) # no 25
            level.append([deck[12-i], deck[25-i], deck[51-i], deck[12-j], deck[38-j]]) # no 38
            level.append([deck[51-i], deck[25-i], deck[38-i], deck[12-j], deck[38-j]]) # no 12

            level.append([deck[12-i], deck[25-i], deck[38-i], deck[12-j], deck[51-j]]) # no 51
            level.append([deck[12-i], deck[38-i], deck[51-i], deck[12-j], deck[51-j]]) # no 25
            level.append([deck[12-i], deck[25-i], deck[51-i], deck[12-j], deck[51-j]]) # no 38
            level.append([deck[51-i], deck[25-i], deck[38-i], deck[12-j], deck[51-j]]) # no 12

            level.append([deck[12-i], deck[25-i], deck[38-i], deck[25-j], deck[38-j]]) # no 51
            level.append([deck[12-i], deck[38-i], deck[51-i], deck[25-j], deck[38-j]]) # no 25
            level.append([deck[12-i], deck[25-i], deck[51-i], deck[25-j], deck[38-j]]) # no 38
            level.append([deck[51-i], deck[25-i], deck[38-i], deck[25-j], deck[38-j]]) # no 12

            level.append([deck[12-i], deck[25-i], deck[38-i], deck[25-j], deck[51-j]]) # no 51
            level.append([deck[12-i], deck[38-i], deck[51-i], deck[25-j], deck[51-j]]) # no 25
            level.append([deck[12-i], deck[25-i], deck[51-i], deck[25-j], deck[51-j]]) # no 38
            level.append([deck[51-i], deck[25-i], deck[38-i], deck[25-j], deck[51-j]]) # no 12

            level.append([deck[12-i], deck[25-i], deck[38-i], deck[38-j], deck[51-j]]) # no 51
            level.append([deck[12-i], deck[38-i], deck[51-i], deck[38-j], deck[51-j]]) # no 25
            level.append([deck[12-i], deck[25-i], deck[51-i], deck[38-j], deck[51-j]]) # no 38
            level.append([deck[51-i], deck[25-i], deck[38-i], deck[38-j], deck[51-j]]) # no 12

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
