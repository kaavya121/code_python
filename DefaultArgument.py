def test(a,b,c,d):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)

test(10,20,30,40)

def test(a=1,b=2,c=3,d=4):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)

test()

def test(a,b,c,d=10):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)

test(10,20,30)

def test(a,b,c=30,d=20):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)

test(10,40)

def test(a=40,b=30,c=20,d=10):
    print("A: ",a,"B: ",b,"C: ",c,"D: ",d)

test(b=100,d=200)
