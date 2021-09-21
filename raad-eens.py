# random Generator:
point = 0
import random
import time

'''
for i in range (1,21):
    print("")
    question = 'Question '+ str(i) + ':                       (or type QUIT to quit)'
    print(question)
    print("")
    number = int(random.randint(1,5))
    incorr = 'the correct awnser was '+ str(number)
    point_num = 'your points: '+ str(point)
    awnser = input('guess the number! ')
    if (awnser.lower() == "quit"):
        exit()
    elif (number == int(awnser)):
        print("that was the correct awnser!!")
        
        point = point + 1
        point_num = 'your points: '+ str(point)
    else: 
        print("That was  the incorrect awnser")
        print(incorr)
        point_num = 'your points: '+ str(point)
    print(point_num)
'''
##ronde :

for p in range(1,21): 
    right = 0  
    number = int(random.randint(1,1000))
    awnser = input('guess the number! ')
    stopper = 11
    while number != int(awnser):
        stopper = stopper - 1
        if stopper <1:
            break
        stopper_01 = 'tries left: '+ str(stopper)
        print("")
        question = 'Round '+ str(p) + ':                       (or type QUIT to quit)'
        print(stopper_01)
        range_02 = range(20,50)
        if number >= int(awnser):
            print("The number is higher")
            range_01 = number - int(awnser)
            if range_01 <= 50:
                print("you're hot!")
            elif range_01 <= 20:
                print("you're VERY hot!")
        elif number<= int(awnser):
            print("The number is lower")
            range_01 = int(awnser) - number
            if range_01 in range_02:
                print("you're hot!")
            elif range_01 <= 20:
                print("you're VERY hot!")
        print(question)        
        print("")
        print("")
        if (awnser.lower() == "quit"):
            exit()
        awnser = input('guess the number! ')
        if (awnser.lower() == "quit"):
            exit()
        elif number >= int(awnser):
            print("The number is higher")
            range_01 = number - int(awnser)
            if range_01 <= 50:
                print("you're hot!")
            elif range_01 <= 20:
                print("you're VERY hot!")
        elif number<= int(awnser):
            print("The number is lower")
            range_01 = int(awnser) - number
            if range_01 in range_02:
                print("you're hot!")
            elif range_01 <= 20:
                print("you're VERY hot!")
    if (awnser.lower() == "quit"):
                print("ok lol")
                time.sleep(1)
                exit()

    if (number == int(awnser)):
            print("that was the correct awnser!!")
            point = point + 1

    print("you've moved onto the next round!")
    point_num = 'your points: '+ str(point)
    print(point_num)

    nog_eens = input('wil je nog een getal raden? [JA/NEE] ')
    if (nog_eens.lower() == "nee"):
        exit()
#endscore
print("                ENDSCORE:")
end_01 = 'your endscore is '+ str(point)+' points'



if point >= 20:
    print("         CONGRATULATIONS!!")
    print("YOU GOT ALL THE QUESTIONS RIGHT!!")
    time.sleep(1)
    print("you cheater")


