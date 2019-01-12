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

print("well done you're not dumb")
dealer= str(input("who is dealing first"))
print("the first dealer is "+ dealer)
