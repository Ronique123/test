try:
    class GrandFatherName:
        def grand_father_name(self):
            print("Tikaman")

    class FatherName(GrandFatherName):
        def father_name(self):
            print("Rojin")

    class ChildName(FatherName):
        def child_name(self):
            print("Rbson")
            
    family = ChildName()
    family.grand_father_name()
    family.father_name()
    family.child_name()

except Exception as exe:
    print("Error")
        
