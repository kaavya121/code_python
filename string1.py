s = input("Enter string: ")

al = 0
nm = 0
sp = 0
uc = 0
lc = 0
sc = 0
for i in s:
    if i.isalpha():
        al = al + 1
    elif i.isnumeric():
        nm = nm + 1
    elif i.isspace():
        sp = sp + 1
    elif i.isspecial():
        sc = sc + 1
    if i.isupper():
        uc = uc + 1
    elif i.islower():
        lc = lc + 1
print("Total alphabets : ", al)
print("Total numeric :  ",nm)
print("Total space :  ",sp)
print("Total upper case letters: ",uc)
print("Total lower case letters: ",lc)

#also add the statements to print the special characters
