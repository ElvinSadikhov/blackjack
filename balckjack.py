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
            if temp>=21:
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

def main():
    cards=shuffle(createDesk())
    a=player(cards,"first")
    b=dealer(cards,"first")
    print(a,a[0])
    print(b,b[0])
    print(player(cards,"hit",a[0]))
    print(dealer(cards,"hit",b[0]))
    print(len(cards))
if __name__=="__main__":
    main()
