rno = int(input("Enter your roll number: "))
sname = input("Enter your name: ")
s1= int(input("Enter your marks of subject 1:"))
s2= int(input("Enter your marks of subject 2:"))
s3= int(input("Enter your marks of subject 3:"))
total = s1+s2+s3
per = total/3

print("Roll No:", rno)
print("Name :", sname)
print("Total:", total)
print("percentage:", per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First class")
elif per>=50:
    print("Second class")
elif per>=40:
    print("Pass class")
else:
    print("Fail")

