class A:
    def show(self):
        print("Show from Class A")

class B(A):
    def show(self):
        super().show()
        print("Show from Class B")

class C(A):
    def show(self):
        super().show()
        print("Show from Class C") 

class D(B,C):
    def show(self):
        super().show()
        print("Show from Class D")

d1=D()
d1.show()






