from random import *
from time import sleep
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

def playerTurn(cards,power,checkforA):
    total=power
    while True:
        play=input("Would you like to 'hit' or 'stay'?").strip().lower()
        sleep(0.5)
        if play!="hit" and play!="stay":
            continue
        if play=="hit":
            total,newcard=player(cards,'hit',total)
            if checkforA==1:
                if total>21:
                    total-=10
                    if total>21:
                        print(f"\nYou got {newcard} and your total is {total} which is more than 21!\n")
                        sleep(0.5)
                        print("YOU LOST!")
                        sleep(2)
                        exit()
                    else:
                        print(f"\nYou got {newcard} and your total is {total}.\n")
                        sleep(0.5)
                        checkforA=0
                elif total==21:
                    print(f"\nYou got {newcard} and it is BLACKJACK!(21).")
                    sleep(0.5)
                    return total
                else:#total<21
                    temp=total-10
                    print(f"You got {newcard} and your total is {temp}/{total}.\n")
                    sleep(0.5)
            else:#A=0
                if total>21:
                    print(f"\nYou got {newcard} and your total is {total} which is more than 21!\n")
                    sleep(0.5)
                    print("YOU LOST!")
                    sleep(2)
                    exit()###
                elif total==21:
                    print(f"\nYou got {newcard} and it is BLACKJACK!(21).")
                    return total               
                else:
                    print(f"\nYou got {newcard} and your total is {total}")
        else:#stay
            if checkforA==1:
                return total
            return total            
                
def dealerTurn(cards,power,z,checkforA):
    if checkforA==1:
        total=power
        if total==21:
            print(f"Okay, it's dealer's turn.\nHis hidden card was {z}.\nHe got BLACKJACK!(21).\n")
            sleep(1)
            return total
        if total>=17 and total<22:
            print(f"\nOkay, it's dealer's turn.\nHis hidden card was {z}.\nHis total was {temp}/{power}.\n")
            sleep(1)
            return total
        temp=power-10
        print(f"\nOkay, it's dealer's turn.\nHis hidden card was {z}.\nHis total was {temp}/{power}.\n")
        sleep(0.5)
        if total>=17:
            return
    else:
        print(f"\nOkat, it's dealer's turn.\nHis hidden card was {z}.\nHis total was {power}.\n")
        sleep(0.5)
        total=power
        if power>21:
            print("YOU WIN!")
            sleep(2)
            exit()
        if power>=17:
            return total
    while True:
        total,newcard=dealer(cards,'hit',total)
        if checkforA==1:
            if total>21:
                total-=10
                print(f"Dealer chooses to hit.\nHe draws {newcard}.\n\
His total is {total}\n")
                sleep(0.5)
                if total>21:
                    sleep(0.5)
                    print("YOU WIN!")
                    sleep(2)
                    exit()
                checkforA=0
                if total>=17:
                    print("Dealer stays.")
                    break
                continue
            if total==21:
                print(f"Dealer chooses to hit.\nHe draws {newcard}.\nHe got BLACKJACK!(21).\n")
                print("Dealer stays.")
                sleep(1)
                break
            else:
                if total>=17:
                    print(f"Dealer chooses to hit.\nHe draws {newcard}.\nHis total is {temp}/{total}\n")
                    sleep(1)
                    return total
                temp=total-10
                print(f"Dealer chooses to hit.\nHe draws {newcard}.\nHis total is {temp}/{total}\n")
                continue
        else:
            print(f"Dealer chooses to hit.\nHe draws {newcard}.\nHis total is {total}\n")
            sleep(0.5)
            if total>21:
                print("YOU WIN!")
                sleep(2)
                exit()
            if total>=17:
                print("Dealer stays.")
                break
        
    return total
        
def main():
    cards=shuffle(createDesk())
    A=0
    a,b,c=player(cards,'first')
    print("Welcome to Elvin's blackjack program!\n")
    sleep(1)
    print(f"You got {b} and {c}")
    if a==21:
        print("You got BLACKJACK!\n")
    elif b[0]=="A" or c[0]=="A":
        if b[0]=="A" and c[0]=="A":
            print("Your total is 2.\n")
            a=2
        else:
            temp=a-10
            print(f"Your total is {temp}/{a}.\n")
            A=1
    else:
        print(f"Your total is {a}.\n")
    sleep(1)
    X=0
    x,y,z=dealer(cards,'first')
    print(f"The dealer has a {y} showing and a hidden card.\n\
His total is hidden, too.\n")
    if y[0]=="A" or z[0]=="A":
        if y[0]=="A" and z[0]=="A":
            x=2
        else:
            X=1
    sleep(0.5)
    if a>21:
        print("\nYOU LOST!")
        sleep(2)
        exit()
    if a==21 and x==21:
        print(f"\nDealer's hidden card was {z} and he also got BLACKJACK!\nYOU LOST!")
        sleep(2)
        exit()
    totalofPlayer=playerTurn(cards,a,A)
    totalofDealer=dealerTurn(cards,x,z,X)
    sleep(0.5)
    print(f"\nDealer's total is {totalofDealer}.\nYour total is {totalofPlayer}.")
    if totalofDealer>=totalofPlayer :
        print("YOU LOST!")
    else:
        print("YOU WIN!")

if __name__=="__main__":
    main()
