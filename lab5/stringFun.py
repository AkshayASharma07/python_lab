s="PYTHON"
print(s[0])
print(s[-1])
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])
print("hello".upper())
print("HeLlO".lower())
print("   hi   ".strip())
print("a,b,c".split(","))
print("akshay".replace("a","z"))
#print("-".join("a","b"))
print("hello".startswith("he"))
print("banana".count("a"))
print("hello".find("ll"))
print("abc123".isalpha())
print("ha"*3)
print("lo" in "hello")
 
s="madam"
if(s==s[::-1]):
    print("it is a pallendrome")
else:
    print("it is not a pallendrome")

s="education"
count=0
for ch in s:
    if ch.lower() in "aeiou":
        count+=1
print(count)

s="education"
count=0
for ch in s:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count+=1
print(count)

print("I like java".replace("java","python"))

s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print("it is an anagram")
else:
    print("not a anagram")

s="programming"
result=""
for ch in s:
    if ch not in result:
        result+=ch
print(result)

s="programming" 
max_char=max(s,key=s.count)
print(max_char)

s="python is powerfull"
print(s.title())

s="PyTHOn"
print(s.swapcase())

s="PYTHON"

s = "PyTHOn"
r = ""

for i in s:
    if "A"<=i >= "Z":
        
        r += i.lower()
    else:
        r += i.upper()

print(r)