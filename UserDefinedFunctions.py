# Function with no arguments and no return value

def printLine():
    print("*"*50)

printLine()
print("Welcome To User Defined Function In Python.")
printLine()

#Function with argument but no return value

def add(a,b):
    print("Addition is : ",a+b)

printLine()
add(10,20)
printLine()

#Function with argument and with return value

def sub(a,b):
    return a-b

ans = sub(10,20)
print("Subtraction is: ",ans)
printLine()
print("Subtaction is: ",sub(10,20))
printLine()
