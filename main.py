deck = []
suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
hands = []
games = []

for i in range(0,4):
    for j in range(0,13):
        deck.append(values[j] + " of " + suits[i])
    
for a in range(0,52):
    for b in range(a+1,52):
        for c in range(b+1,52):
            for d in range(c+1,52):
                for e in range(d+1,52):
                    for f in range(e+1,52):
                        for g in range(f+1,52):
                            for h in range(g+1,52):
                                for i in range(h+1,52):
                                    game = [deck[a], deck[b], deck[c], deck[d], deck[e], deck[f], deck[g], deck[h], deck[i]]
                                    print(a,b,c,d,e,f,g,h,i)
                                    games.append(game)