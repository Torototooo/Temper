import random
print("")
print("******************************************************************************************")
print("")
print("1.rock | 2.paper | 3.scisior  |||  4.GAME OVER")
us=int(input("chose(1-4):"))
new=0
cm=random.randint(1,3)

while us!=4:
    
    if new>=1:
        print("******************************************************************************************")
        print("            ")
        print("1.rock | 2.paper | 3.scisior  |||  4.GAME OVER")
        us=int(input("chose(1-4):"))
        cm=random.randint(1,3)
    new=new+1

    print("")
    if us==1:
        print("your choice:ROCK") 
    elif us==2:
        print("your choice:PAPER")
    elif us==3:
        print("your choice:SCISIOR")
    elif us==4:
        a=10
    else:
        print("enter proper choice")

    if us!=4:

        print("")
        if cm==1:
            print("computer choice:ROCK") 
        elif cm==2:
            print("computer choice:PAPER")
        elif cm==3:
            print("computer choice:SCISIOR")
        else:
            print("enter proper choice")

        if us==cm:
            print("              ")
            print("---------------")
            print("|  IT'S TIE   |")
            print("---------------")
            print("              ")
        elif us==1 and cm==2:
            print("                                    ")
            print("-------------------------------------")
            print("| PAPER BEATS ROCK ....COMPUTER WIN |")
            print("-------------------------------------")
            print("                                    ")
        elif us==1 and cm==3:
            print("                               ")
            print("--------------------------------")
            print("| ROCK BAETS SCISIOR...YOU WIN |")
            print("--------------------------------")
            print("                               ")
        elif us==2 and cm==1:
            print("                               ")
            print("--------------------------------")
            print("| PAPER BEATS ROCK ....YOU WIN |")
            print("--------------------------------")
            print("                               ")
        elif us==2 and cm==3:
            print("                                     ")
            print("--------------------------------------")
            print("| SCISIOR BAETS PAPER...COMPUTER WIN |")
            print("--------------------------------------")
            print("                                     ")
        elif us==3 and cm==1:
            print("                                    ")
            print("-------------------------------------")
            print("| ROCK BAETS SCISIOR...COMPUTER WIN |")
            print("-------------------------------------")
            print("                                    ")
        elif us==3 and cm==2:
            print("                                ")
            print("---------------------------------")
            print("| SCISIOR BAETS PAPER...YOU WIN |")
            print("---------------------------------")
            print("                                ")
        else:
            print("ERORO IN GAME PLAY AGAIN")


if us==4:
    print(" ")
    print("             ")
    print("(=======================================================================)")
    print("(                               GAME OVER                               )")
    print("(=======================================================================)")
    print("             ")

    print("******************************************************************************************")
