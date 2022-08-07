
print('Hello',end=" ")
print("Hello")
a = "Hello"
print(a)
b = "Hello World"
print(b[0])

for x in "banana":
    print(x,end="")
print(len(b))

c = "Amar sonar Bangla"
print("sonar" in c)

b = "Bangladesh"
print(b[0:6])
c = "bangladesh"
d = "BANGLADESH"
print(c.upper(),end=" ")
print(d.lower())

f= " Kire "
print(f)
print(f.strip())
print(len(f))
print(type(f))
print(d.replace("B","D"))
m = "amr,tumi"
print(m.split(","))

a= int(input("Enter a number : "))
b = int(input("Enter another number : "))
print(f"{a} + {b} = {a+b}")

a = input("Enter your name ")
print(f"Hello Mr {a}")

mlist  = ["apple","Banana","Mango"]
print(mlist[0])
print(mlist[-3:])
if "apple" in mlist:
    print("Yes, 'apple ' is in the lis")

a = ["Galib","Saif","Rubel","Tanim","Shamim"]
a.insert(0,"Yasin")
a.append("Yousuf")
print(a)
a.remove("Yasin")
a.pop(0)
print(a)

#a = ["f","a","g","c","d","b","v"]
a = [5,6,3,2,1,9,10]
#a.sort(reverse=False)
b = a.copy()
print(b)
for x in a:
    print(x,end=" ")
    
a = [1,2,3,1,2,3,1,2,3,1]
a.sort()
#print(a.count(1))
for x in a:
   print(f" {x} = {a.count(x)}")
