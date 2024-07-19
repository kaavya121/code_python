'''
1)
n = int(input("Enter N: "))
while n>0:
    print("Tops Technologies")
    n = n - 1 
2)
n = int(input("Enter N: "))
sum = 0
while n>0:
    sum = sum + n
    n = n-1
print("Sum is : ",sum)

#3)
#FORNSUM

n = int(input("Enter n: "))
sum = 0

for i in range(1,n+1):
    sum = sum + i
print("Sum is: ",sum)

#4) Fibonacci Series
a,b = 0,1
n = int(input("Enter the end number :"))
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b = b, a+b 

#5) Prime Numbers
n = int(input("Enter N:"))

if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n, "is not Prime")
            break
    else:
        print(n, "is prime")
else:
    print(n, "is not prime")
'''
#6) Guess A Number
import random
#print(random.randint(1,100))
#l = [1,2,10,20,"tops", "tech", "pytho", True, False,100,200]
#print(random.choice(l))

num= random.randint(1,20)

while True:
    guess= int(input("Enter your number between 1 and 20: "))
    if guess == num:
        print("You guessed the number right.")
        break
    elif guess>num :
        print("You guessed a greater number.")
    elif guess<num:
        print("You guessed a smaller number.")
