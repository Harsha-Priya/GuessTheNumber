import random
from math import sqrt
num= random.randint(1,101)
attempts = 10
maxpoints = attempts
guess = False
hintcount = 0
composite = False

print(num)
print("Guess the number I am thinking of between 1 to 100. You are allowed a maximum of "+str(attempts)+" attemps.")

for i in range(0,attempts):
    print("Attempt " +str(i+1)+ ":")
    guessnum=int(input())
    if(guessnum==num):
        print("The guessed number is correct!")
        guess = True
        break
    elif(guessnum<num):
        print("The number is greater than the guessed number")
        maxpoints = maxpoints - 1
    else:
        print("The  number is lesser than the guessed number")
        maxpoints = maxpoints - 1

    if(i<(attempts-1)):
        print("Do you need a hint? Type 'y' for yes and any other key for no")
        ans = input()
        if('y'==ans) and (0!=maxpoints):
            if (0 == hintcount) and (num % 2 == 0):
                print("The number is an even number")
                maxpoints = maxpoints - 1
                hintcount = hintcount + 1
            elif(0 == hintcount):
                print("The number is an odd number")
                maxpoints = maxpoints - 1
                hintcount = hintcount + 1
            elif (1== hintcount):
                if num>3:
                    for k in range(2,int(sqrt(num))):
                        if(num%k==0):
                            composite = True
                            break
                if (False == composite):
                    print("The number is a prime")
                else:
                    print("The number is not a prime")
                maxpoints = maxpoints - 1
                hintcount = hintcount + 1
            else:
                print("No more clues!")
        elif('y' == ans):
            print("Points exhausted!")
            break


if(False==guess):
    print("Attempts exhausted! The number was " +str(num))
    print(maxpoints)
else:
    print("You got " +str(maxpoints)+ " points")

