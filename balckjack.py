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

def main():
    print("Shuffled cards:")
    for i in shuffle(createDesk()):
        print(i)
        
if __name__=="__main__":
    main()
