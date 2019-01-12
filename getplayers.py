numberplayers=int(input("How Many Players?"))
print("Number of players is:"+str(numberplayers))
#if numberplayers == 2:
    #print("get more friends then come back, you loser")
    #exit()
player_list = []
for x in range (0,numberplayers):
    player_list.append(input("what is the name of player "+str(x + 1)+"?"))
for x in range (0,numberplayers):
    print("name of player "+ str(x + 1) +" is " + player_list[x])
numberoftricks=int(52/numberplayers)
while 52%numberoftricks <= 1:
    numberoftricks-=1
print("You can deal a maximum of "+ str(numberoftricks) + " cards to each person.")
print("when  you deal the maximum amount of card(s) to each person there will be " + str(52%numberoftricks)+" cards left")
cardmax= int(input("what is the maximum ammount of cards you want to be dealt?"))
cardmin= int(input("what is the minimum ammount of cards you want to be dealt?"))
while cardmin>cardmax or cardmax>numberoftricks or cardmin<1:
    if cardmin<1 :
        print("the minimum amount of cards is 1")
    if cardmin>cardmax:
        print("the maximum needs to be more than the minimum")
    if cardmax>numberoftricks:
        print("the maximum cards that each peson can have is "+ str(numberoftricks))
    cardmax= int(input("what is the maximum ammount of cards you want to be dealt?"))
    cardmin= int(input("what is the minimum ammount of cards you want to be dealt?"))

current_dealer=0
for card_dealt in range (cardmax,cardmin - 1,-1):
    print("the dealer is "+player_list[current_dealer])
    first_bidder=current_dealer+1
    if first_bidder==numberplayers:
        first_bidder=0
    print("the ammount of cards being dealt is "+str(card_dealt))
    numberbid_list=[]
    for player in range(0,numberplayers):
        numberbid_list.append(input("What is your bid " + player_list[first_bidder] +"?"))
        print("your bid is "+ numberbid_list[first_bidder])
#    for player in range(0,numberplayers):
#        numberbid_list.append(input("How many tricks did " + player_list[first_bidder] +" win?"))

    current_dealer+=1
    if current_dealer+1 > numberplayers:
        current_dealer=0
