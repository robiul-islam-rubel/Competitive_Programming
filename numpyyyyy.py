import numpy as np
"""ar = np.array([1,2,3,4,5,6,7,8])
for x in ar:
    print(x,end=" ")
# 2d array
a = np.array([[1,2,3],[4,5,6]])
print(a)
# access array elements
b = np.array((1,2,3,4))
print(b[0]+b[1])
# access 2 d array elements
h = np.array([[1,2,3],[4,5,6]])
print(h[1,2])
# slicing array
g = np.array([1,2,3,4])
print(g[0:4])

# copy array
f = np.array([1,2,3,4,5])
d = f.copy()
f[0]=10

print(f)
print(d)

# view array
s = np.array([1,2,3,4,5])
c = s.view()
s[0]=43
print(s)
print(c)

# array shape
j = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(j.shape)

# reshape the array
r = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
n = r.reshape(4,3)
print(n)
# access 1d array elements
e = np.array((1,2),(4,5))
for x in e:
    for y in x:
        print(y,end=" ")
    print()

# array search
k = np.array([1,2,3,4,3,6,3])
t = np.where(k%2==0)
print(t)

s = np.array([2, 3, 1, 5])
f = np.searchsorted(s,)
print(f)
"""
# sort the array
f = np.array([1,4,3,2,0])
print(np.sort(f))