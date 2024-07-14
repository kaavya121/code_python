a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
if a>b:
    if a>c:
        print("a is max")
    else:
        print("c is max")
elif b>c:
    print("b is max")
else:
    print("c is max")
