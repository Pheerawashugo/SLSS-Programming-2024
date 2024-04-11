i=0
showing_list =[
    'tshirt',
    'jeans',
    'pants',
    'cap'
]
bought=[]
money = int(input("How much money do you have?"))
def Hugo():
    while True:
        if money < 0:
            money = int(input("The number is wrong, please enter the amount of money you have again:"))
        elif 0<=money and money<20:
            money=int(input("You don't have enough money to buy anything, so please enter your money again:"))
        else:
            break
Hugo()
print (showing_list)
buy=input("what do you wanna buy?, type it one by one.")
while True: 
    while True:
        if buy.lower()=="tshirt"or"jeans"or"pants"or"cap":
            break
        else:
            buy=input("We don't have that thing, please enter which thing do you want again:")
    if buy.lower()=="tshirt":
        if money>=30:
            money-=30
            bought+=["tshirt"]
        else:
            print("You can't buy the tshirt, please enter what do you want more again.")
    elif buy.lower()=="jeans":
        if money>=50:
            money-=50
            bought+=["jeans"]
        else:
            print("You can't buy the jeans, please enter what do you want again. ")
    elif buy.lower()=="pants":
        if money>=25:
            money -=25
            bought+=["pants"]
        else:
            print("You can't buy the pants, please enter what do you want more again.")
    elif buy.lower()=="cap":
        if money>=20:
            money -=20
            bought+=["cap"] 
        else:
            print("You can't buy the cap, please enter what do you want more again.")
    if True:
        if i==0:
            if money<50:
                print ("You can't buy jeans now")
                i+=1
        if i==1:
            if money<30:
                print("You can't buy tshirt now")
                i+=1
        if i==2:
            if money<25:
                print("You can't buy pants now")
                i+=1
        if i==3:
            if money<20:
                print("You can't buy cap now")
                i+=1
    if money<20:
        print("You cannot buy anything else")
        break
    buy=input("what do you want more? If you've done, press '1'")
    if buy.lower()=="1":
        break
print("All stuff that you buy is:",bought,".","your money left is:",money,"dollars.")
