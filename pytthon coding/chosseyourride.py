print("what type of ride do you want?:")
print("1.bike")
print("2.car")
choice=int(input("enetr your choice:"))
if(choice==1) :
    print("what type of bike?")
    print("1.scooty/n")
    print("2.scooter/n")
    choice2=int(input("enter your choice2:"))
    if choice2==1 :
        print("you have picked scooty")
    else :
        print("you have picked scooter")
elif(choice==2) :
    print("what type of car?")
    print("1.sedan")
    print("2.XUV")
    choice3=int(input("enter your choice3:"))
    if choice3==1 :
        print("you have picked sedan")
    else :
        print("you haved picked XUV")
else :
    print("WRONG CHOICE!")