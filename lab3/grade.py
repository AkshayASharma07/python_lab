marks=int(input("enter your marks = "))
if marks<=100:
    if marks>=90:
        print("A")
    elif marks>=80:
        print("B")
    elif marks>=70:
        print("C")
    elif marks>=60:
        print("D")
    elif marks>=50:
        print("E")
    else:
        print("F")
else:
    print("invaild input")