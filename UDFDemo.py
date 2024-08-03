import UDF

print("*"*40)

print("1. Odd Even. ")
print("2. MaxOfTwo. ")
print("3. MaxOfThree. ")
print("4. Fibonacci. ")
print("5. Prime ")
print("6. Exit ")

choice= int(input("Enter your choice: "))

if choice==1:
    a= int(input("Enter your number: "))
    UDF.odd_even(a)

elif choice==2:
    num1= int(input("Enter your number: "))
    num2= int(input("Enter your number: "))
    UDF.maxoftwo(num1,num2)

elif choice==3:
    num1= int(input("Enter your first number: "))
    num2= int(input("Enter your second number: "))
    num3= int(input("Enter your third number: "))
    UDF.maxofthree(num1,num2,num3)

elif choice==4:
    n= int(input("Enter the number: "))
    UDF.fibonacci(n)

elif choice==5:
    b= int(input("Enter the number: "))
    UDF.prime(b)

elif choice==6:
    print("Thankyou for using our service ")

else:
    print("Invalid Choice. ")
