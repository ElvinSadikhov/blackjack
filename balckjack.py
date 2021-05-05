'''
Крести-\u2663
Пики-\u2660
Кирпичи-\u2666
Черви-\u2665
'''
from random import *
def createDesk():
    cards=list()
    for value in range(2,11):
        for suit in ('\u2660','\u2663','\u2666','\u2665'):
            card=""
            card+=str(value)+suit
            cards.append(card)
    for value in ('J','Q','K','A'):
        for suit in ('\u2660','\u2663','\u2666','\u2665'):
            card=""
            card+=str(value)+suit
            cards.append(card)
    return cards

def shuffle(cards):
    for i in range(len(cards)):
        new=randint(0,51)
        cards[i],cards[new]=cards[new],cards[i]
    return cards

def cardPower(card,aim,temp=0):
    power=0
    if aim=="first":
        if card[:2]=="10":
            power+=10
        elif card[0].isdigit():
            power+=int(card[0])
        elif card[0] in ["J","Q","K"]:
            power+=10
        else:#A
            power+=11
    elif aim=="hit":
        if card[:2]=="10":
            power+=10
        elif card[0].isdigit():
            power+=int(card[0])
        elif card[0] in ["J","Q","K"]:
            power+=10
        else:#A
            if temp+11>21:
                power+=1
            else:
                power+=11
    return power
def player(cards,aim,power=0):
    if aim=="first":
        card1p=cards.pop()
        card2p=cards.pop()
        power+=cardPower(card1p,aim)
        power+=cardPower(card2p,aim)
    elif aim=="hit":
        card3p=cards.pop()
        power+=cardPower(card3p,aim,power)
    if aim=="first":
        return power,card1p,card2p
    #aim="hit"
    return power,card3p

def dealer(cards,aim,power=0):
    if aim=="first":
        card1d=cards.pop()
        card2d=cards.pop()
        power+=cardPower(card1d,aim)
        power+=cardPower(card2d,aim)
    elif aim=="hit":
        card3d=cards.pop()
        power+=cardPower(card3d,aim,power)###
    if aim=="first":
        return power,card1d,card2d
    #aim="hit"
    return power,card3d

def playerTurn(cards,power):
    total=power
    while True:
        play=input("Would you like to 'hit' or 'stay'?").strip().lower()
        if play!="hit" and play!="stay":
            continue
        if play=="hit":
            total,newcard=player(cards,'hit',total)
            if total>21:
                print(f"\nYou got {newcard} and your total is {total} which is more than 21!\n\nYOU LOST!")
                exit()###
            elif total==21:
                print(f"\nYou got {newcard} and your total is 21!(BLACKJACK)")
                return total               
            else:
                print(f"\nYou got {newcard} and your total is {total}")
        else:#stay
            return total            
            
def dealerTurn(cards,power,z):
    print(f"\nOkat, it's dealer's turn.\nHis hidden card was {z}.\nHis total was {power}.\n")
    total=power
    if power>21:
        print("YOU WIN!")
        exit()#
    if power>=17:
        return total
    while True:
        total,newcard=dealer(cards,'hit',total)
        print(f"Dealer chooses to hit.\nHe draws {newcard}.\nHis total is {total}\n")
        if total>21:
            print("YOU WIN!")
            exit()#
        if total>=17:
            print("Dealer stays.")
            break
        
    return total
        
def main():
    cards=shuffle(createDesk())
    a,b,c=player(cards,'first')
    print("Welcome to Elvin's blackjack program!\n")
    print(f"You got {b} and {c}\n\
Your total is {a}\n")
    if a==21:
        print("You got BLACKJACK!")
    x,y,z=dealer(cards,'first')
    print(f"The dealer has a {y} showing and a hidden card.\n\
His total is hidden, too.\n")
    if a>21:
        print("\nYOU LOST!")
        exit()
    if a==21 and x==21:
        print(f"\nDealer's hidden card was {z} and he also got BLACKJACK!\nYOU LOST!")
        exit()
    totalofPlayer=playerTurn(cards,a)
    totalofDealer=dealerTurn(cards,x,z)    
    print(f"\nDealer's total is {totalofDealer}.\nYour total is {totalofPlayer}.")
    #if totalofDealer>21 or totalofPlayer>21:
    if totalofDealer>=totalofPlayer :
        print("YOU LOST!")
    else:
        print("YOU WIN!")
        
if __name__=="__main__":
    main()
