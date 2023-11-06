
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []


def deal():
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))
    print(f"player card,{player}")
    print(f"dealer card,{dealer}")
    return

def burst(cards):
    if sum(cards)>21:
        return True
    
    
def compare():
    if sum(player)>sum(dealer):
        print(f"player lose,{player}")
    else:
        print(f"player lose,{player}")
        
def blackjack():
    print ("wanna make money through gamble? thats wonderful a thought hhh, my suggestion is all in from the begining")
    deal()
    hit = input("hit or not, y/n")
    if hit=="y":
        player.append(random.choice(cards))
        print(f"player card,{player}")
        print(f"dealer card,{dealer}")
        if burst(player) == True:
            print("player lose")
        else:
            print(compare())
    else:
        while sum(dealer)<=16:
            dealer.append(random.choice(cards))
        if burst(dealer)== True:
            print("player win")
        else:
            print(compare())
            
while True:
    play = input("wanna play,y/n")
    if play == "y":
        blackjack()
    else:
        break
    
    
    
    

