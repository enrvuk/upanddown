numberplayers=int(input("How Many Players?"))
print("Number of players is:"+str(numberplayers))
player_list = []
for x in range (0,numberplayers):
    player_list.append(input("what is the name of player "+str(x + 1)+"?"))
    #this is a comment and can be deleted
for x in range (0,numberplayers):
    print("name of player "+ str(x + 1) +" is " + player_list[x])
