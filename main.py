# Make a deck

deck = []
suits = ["C", "H", "D", "S"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

for i in range(0,4):
    for j in range(0,13):
        deck.append([values[j], suits[i]])

#print(deck)

card1 = 0
card2 = 1
card3 = 2
card4 = 3
card5 = 4
card6 = 5
card7 = 50
card8 = 10
card9 = 8

tmp_hero = [deck[card1],deck[card2]]
tmp_table = [deck[card3],deck[card4],deck[card5],deck[card6],deck[card7]]
tmp_villain = [deck[card8],deck[card9]]


def evaluate_hands(Hero_Hand, Villain_Hand, Table): # redo to do individual 5 card analysis then do range of possible hands
    Hero_Ranking = 9
    Villain_Ranking = 9
    Hero_Flush = False 
    Villain_Flush = False

    Hero_Suits = [0,0,0,0]
    Hero_Values = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    Villain_Suits = [0,0,0,0]
    Villain_Values = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for x in Hero_Hand:
        Hero_Suits[suits.index(x[1])] += 1
        Hero_Values[values.index(x[0])] += 1

    for x in Villain_Hand:
        Villain_Suits[suits.index(x[1])] += 1
        Villain_Values[values.index(x[0])] += 1

    for x in Table:
        Hero_Suits[suits.index(x[1])] += 1
        Hero_Values[values.index(x[0])] += 1
        Villain_Suits[suits.index(x[1])] += 1
        Villain_Values[values.index(x[0])] += 1
   
    if 5 in Hero_Suits or 6 in Hero_Suits or 7 in Hero_Suits:
        Hero_Flush = True 

    if 5 in Villain_Suits or 6 in Villain_Suits or 7 in Villain_Suits:
        Villain_Flush = True
    
    while True:
        if Hero_Flush:
            for i in range(0,8):
                if Hero_Values[i] == 1 and Hero_Values[i+1] == 1 and Hero_Values[i+2] and Hero_Values[i+3] and Hero_Values[i+4]:
                    Hero_Ranking = 1
            if Hero_Ranking == 1:
                break
        
        if 4 in Hero_Values:
            Hero_Ranking = 2
            break

        if 2 in Hero_Values and 3 in Hero_Values:
            Hero_Ranking = 3
            break

        if Hero_Flush:
            Hero_Ranking = 4
            break

        for i in range(0,8):
            if Hero_Values[i] == 1 and Hero_Values[i+1] == 1 and Hero_Values[i+2] and Hero_Values[i+3] and Hero_Values[i+4]:
                Hero_Ranking = 5
        if Hero_Ranking == 5:
            break

        if 3 in Hero_Values:
            Hero_Ranking = 6
            break

        counter = 0
        for i in range(0,13):
            if Hero_Values[i] == 2:
                counter += 1
        if counter >= 2:
            Hero_Ranking = 7
            break

        if 2 in Hero_Values:
            Hero_Ranking = 8
            break

    while True:
        if Villain_Flush:
            for i in range(0,8):
                if Villain_Values[i] == 1 and Villain_Values[i+1] == 1 and Villain_Values[i+2] and Villain_Values[i+3] and Villain_Values[i+4]:
                    Villain_Ranking = 1
            if Villain_Ranking == 1:
                break
        
        if 4 in Villain_Values:
            Villain_Ranking = 2
            break

        if 2 in Villain_Values and 3 in Villain_Values:
            Villain_Ranking = 3
            break

        if Villain_Flush:
            Villain_Ranking = 4
            break

        for i in range(0,8):
            if Villain_Values[i] == 1 and Villain_Values[i+1] == 1 and Villain_Values[i+2] and Villain_Values[i+3] and Villain_Values[i+4]:
                Villain_Ranking = 5
        if Villain_Ranking == 5:
            break

        if 3 in Villain_Values:
            Villain_Ranking = 6
            break

        counter = 0
        for i in range(0,13):
            if Villain_Values[i] == 2:
                counter += 1
        if counter >= 2:
            Villain_Ranking = 7
            break

        if 2 in Villain_Values:
            Villain_Ranking = 8
            break

    print(Hero_Ranking)
    print(Villain_Ranking)

    if Hero_Ranking < Villain_Ranking:
        print("Hero Wins")
        return 0
    
    if Hero_Ranking > Villain_Ranking:
        print("Villain Wins")
        return 0
    

    if Hero_Ranking == 1: # need to fix
        if Hero_Values.index(1) > Villain_Values.index(1):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(1) < Villain_Values.index(1):
            print("Villain Wins")
            return 0 
        print("Draw")

    if Hero_Ranking == 2:
        if Hero_Values.index(4) > Villain_Values.index(4):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(4) < Villain_Values.index(4):
            print("Villain Wins")
            return 0 
        print("Draw")

    if Hero_Ranking == 3:
        if Hero_Values.index(3) > Villain_Values.index(3):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(3) < Villain_Values.index(3):
            print("Villain Wins")
            return 0 
        if Hero_Values.index(2) > Villain_Values.index(3):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(2) < Villain_Values.index(3):
            print("Villain Wins")
            return 0 
        print("Draw")

    if Hero_Ranking == 4:
        if Hero_Values.index(1) > Villain_Values.index(1):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(1) < Villain_Values.index(1):
            print("Villain Wins")
            return 0 
        print("Draw")

    if Hero_Ranking == 5:
        if Hero_Values.index(1) > Villain_Values.index(1):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(1) < Villain_Values.index(1):
            print("Villain Wins")
            return 0 
        print("Draw")

    if Hero_Ranking == 6:
        if Hero_Values.index(3) > Villain_Values.index(3):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(3) < Villain_Values.index(3):
            print("Villain Wins")
            return 0 
        print("Draw")

    if Hero_Ranking == 7:
        if Hero_Values.index(2) > Villain_Values.index(2):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(2) < Villain_Values.index(2):
            print("Villain Wins")
            return 0 
        print("Draw")

    if Hero_Ranking == 8:
        if Hero_Values.index(1) > Villain_Values.index(1):
            print("Hero Wins")
            return 0 
        if Hero_Values.index(1) < Villain_Values.index(1):
            print("Villain Wins")
            return 0 
        print("Draw")






print(tmp_table)
print(tmp_hero)
print(tmp_villain)
print(" ")
evaluate_hands(tmp_hero, tmp_villain, tmp_table)