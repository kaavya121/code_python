def odd_even(num):
    if num%2==0:
        print("The number is even.")
    else:
        print("The number is odd.")

def maxoftwo(num1,num2):
    if num1>num2:
        print(num1, "Is Max")
    elif num1==num2:
        print("Both are equal,")
    else:
        print(num2, "Is Max")

def maxofthree(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            print("Number 1 is max.")
        else:
            print("Number 3 is Max.")
    elif num2>num3:
        print("Number 2 is Max.")
    else:
        print("Number 3 is Max.")
    
def fibonacci(n):
    a,b = 0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b = b, a+b

def prime(n):
    for i in range(3,int(n/2+1),2):
        if n%i==0:
            print("n is not prime.")
        else:
            print("n is prime.") 
