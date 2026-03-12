a=input("enter any word = ")
b=""
k=0
start=int(input("enter the start position of extraction = "))
start-=1
for j in a:
    if(k>=start):
        b+=j
    k=k+1
print(b)
    
