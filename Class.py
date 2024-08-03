class Student:
    def getData(self,fname,lname):
        print("getData called")
        self.f = fname
        self.l = lname
    def putData(self):
        print("putData called")
        print("First Name: ",self.f)
        print("Last Name: ",self.l)

s1=Student()
s2=Student()

s1.getData("Kaavya","Vyas")
s1.putData()
