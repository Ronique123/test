class Employee:
 
    def __init__ (self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    
    def display_profile(self):
       print(f"The name of Employee is {self.name} age {self.age} salary {self.salary}" )
       
    def view_salary(self):
        if(self.salary > 10000):
            print(f"The salary is {self.salary}")
        else:
            print("The salary is less than 10,000")
    
    def check_age(self):
        if (self.age>=16 and self.age<=60):
            # if(self.age<=60):
                # print(f"The age of the employee is{self.age}")
           # else:
                print(f"The age is {self.age} ")
        else:
            print("The age is not valid")
            
name=(input("Enter the name of the Employee: "))
salary=(int(input("Enter the salary of employee: ")))
age=(int(input("Enter age of employee: ")))
employee_details=Employee(name,salary,age)
employee_details.display_profile()
employee_details.view_salary()
employee_details.check_age()