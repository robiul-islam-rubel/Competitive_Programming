s = {1,2,3,4,5,6}
print(s)
for x in s:
    print(x,end=" ")
    if x==6:
        break
s.add(8)
for x in s:
    print(x,end=" ")
print(1)
print(2)