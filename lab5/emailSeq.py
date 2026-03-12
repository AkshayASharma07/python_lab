email=input("enter your email = ")
dig=""
char=""
special_char=""
for i in email:
    if(i.isalpha):
        char+=i
    elif(i.isnumeric):
        dig+=i
    else:
        special_char+=i
print("digits = ",dig)
print("character = ",char)
print("special character = ",special_char)
