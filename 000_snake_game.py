import random

tg=pw=cw=tie=0
def game(pl_c,comp_c):
        res_pl=True
        tie=False
        if pl_c == 2 and comp_c == 1:
            res_pl=False
        elif pl_c==1 and comp_c== 0:
            res_pl=False
        elif pl_c==0 and comp_c ==2:
            res_pl=False

        print(f"in this game you choose {pl}")
        print(f"in this game computer choose {comp}")
    
        if pl_c == comp_c:
            print("It's a tie")
            tie=True
        elif res_pl == True:
            print("player wins")
        else:
            print("computer wins") 
        return res_pl,tie  


per=input("Enter 'yes' to start with the game: ")
per.lower()

while per == 'yes':
    print("enter 0 for snake, 1 for water and 2 for gun")
    comp=random.randint(0,2)
    pl=int(input("Enter your choice please: "))
    if(pl > 2 ):
        print("please enter the value accordingly")
    else:
        tg+=1    
        res,res_tie=game(pl,comp)  
        if res == False :
            cw+=1
        elif res == True and res_tie == False:
            pw+=1
        else:
            tie+=1         

    t=input("if you wish to stop playing please enter 'stop' or to continue playing enter anything: ")
    if t== 'stop':
        break
           

print("Your total number of games were: ",tg)
print("total games won by player ",pw)
print("number of games lost by user ",cw)   