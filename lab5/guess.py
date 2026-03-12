import random
secret=random.randint(0,100)
a=int(input("guess any number between 1 to 100 = "))
while(a!=1000):
    if(secret==a):
        print("you have successfully guessed")
        break
    elif(secret>a):
            print("TRY AGAIN!! , guess a number greater than your guessed number ",a)
            a=int(input("enter the new guess = "))
    else:
         print("TRY AGAIN!! , guess a number less than your guessed number ",a)
         a=int(input("enter the new guess = "))