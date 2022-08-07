#check a number is prime or not
 n=int(input())

for i in range(1,n+1):
	if(n%i==0):
		cnt+=1;

if(cnt==2)
 print("Prime")
else:
	print("Not Prime")


# Check a character is vowel or not.

ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")



 # check a number is odd or even
 n=int(input())
 if n%2==0:
 	print("the number is even")
 else:
 	print("the number is even")


 #sum of divisor
 n=int(input())
 sum=0
 for i in range(1,n+1):
 	if n%i==0:
 		sum+=i
 print(sum)


 # count numner of divisor
  n=int(input())
  cnt=0
  for i in range(1,n+1):
  	if n%i==0:
  		cnt+=1
print(cnt)


# sum of digits in a number

def getSum(n):
	
	sum = 0
	while (n != 0):
	
		sum = sum + (n % 10)  # add everytime last digit of the number
		n = n//10             # remove last digit
	
	return sum

n = int(input())
print(getSum(n))


# check a char present in a string or not

string=input()
ch=input()
if ch in string:
	print("the character is present in the string")
else
    print("the character is missing in the string")

# sum of series

n=int(input())
num=(n*(n+1))/2
print(num)


#sum of odd numbers

n=int(input())
print(n*n)


#sum of even numbers

n=int(input())
print(n*(n+1))



# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1





#area of triangle

a = float(input('Enter the length of first side: '))  
b = float(input('Enter  the length of second side: '))  
c = float(input('Enter  the length of third side: '))  
s = (a + b + c) / 2  
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %Area)


# area of a circle
import math as M  
Radius = float (input ("Please enter the radius of the given circle: "))  
area_of_the_circle = M.pi* Radius * Radius  
print (" The area of the given circle is: ", area_of_the_circle)  

