'''
d = {145:"Ajay", 908:"Vijay", 765:"Jay", 654:"Kamal", 999:"Karan"}

print(d)
print(d[908])
print(d.get(765))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(908))
print(d)
print(d.popitem())
print(d)
d1= {1:"Vijay", 2: "Karan", 145:"Ketan"}
d.update(d1)
print(d)

for i in d:
    print((i), " : " ,d[i])


d = {}
n = int(input("Enter N: "))
for i in range(1, n+1):
    d[i] = i*i
print(d)
'''
l = []

for i in range(1999,2301):
    if i%5==0 and i%7!=0:
        l.append(i)
        
print(l)
