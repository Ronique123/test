class Employee:
    def __init__(self, salary):
        self.salary = salary
        
    def check_age(self, age):
        print("age is", age)
        
    def check_salary(self):
        print("salary is",self.salary)
        
    def avg_salary(self):
        print(f"the average salary is:", self.salary/2)   
            
employee = Employee(100)
employee.check_age(23)
employee.check_salary()
employee.avg_salary()



# l1 = [10, 20, 50]
l1 = list((10, 20, 50))
l1.append(50)