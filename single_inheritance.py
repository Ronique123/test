# class Father_Name:
#     def first_name(self):
#         print("Rojin")

# class Child_Name(Father_Name):
#     def last_name(self):
#         print("Rbson")
        
# name1 = Child_Name()
# name1.last_name()



class FatherName:
    def father_name(self):
        print("Rojin")

class MotherName():
    def mother_name(self):
        print("Bimu")

class ChildName(FatherName, MotherName):
    def child_name(self):
        print("Rbson")
        
child = ChildName()
child.child_name()
child.father_name()
child.mother_name()