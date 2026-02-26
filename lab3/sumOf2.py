num=int(input("enter 2-digit number = "))
if num>=10 and num<=99:
    lastDig=num//10
    firstDig=int(num/10)
   
    print("sum of ",num," = ",lastDig+firstDig)
else:
    print("enter a valid number")