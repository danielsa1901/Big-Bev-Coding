#Get input information
import random

packs = int(input("Enter the amount of cigarette packs you smoke on a weekly basis\n"))
smokerYears = int(input("Enter the amount of months you have been an avide smoker\n"))
quit = int(input("Enter the amount of weeks you wish to be smoke free\n"))

if(packs<=quit):

    weekNum = quit
    

    week = []
    weekDays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    reduction = 1

    for i in range(weekNum):
        week.append(packs)
        packs = packs-reduction
        roundP = round(packs,2)

        #Find out how many packs you can smoke a week
        if(packs<=0.1):
            print("\nIn week ",i+1," you will be allowed to smoke 0 packs\n","Congradulations, you are smoke free!")
            break
        print("\nIn week ",i+1," you will be allowed to smoke ",roundP,"packs\n")

        #Find out what days of the week you will be able to smoke
        packPerDay = roundP/5 #Divide packs to smoke across 5 days, 2 smoke free days
        noSmokeDays = []

        for k in range(2): #randomly generate 2 smoke free days
            randnum = random.randint(0,6)
            noSmokeDays.append(randnum)
        if(noSmokeDays[0]==noSmokeDays[1]): #if number generator gives 2 of the same values, just make the 2 days Monday and Thursday
            noSmokeDays[0] = 1
            noSmokeDays[1] = 3
        
        for j in range(7):
            if(j == noSmokeDays[0] or j == noSmokeDays[1]):
                print(weekDays[j],"= 0 packs\n")
            spackPerDay = round(packPerDay,1)
            print(weekDays[j],"=",spackPerDay, "packs\n")
    

            
        extra = int(input("\nPlease specify the amount of extra packs you smoked, if any during this week\n"))
        if(extra>0):
            reduction = 1 + (extra/4)
        else:
            reduction = 1

else:
    print("\nSorry, that time frame is not fesible, please slect a more generous time frame to assume a smooth transistion")


