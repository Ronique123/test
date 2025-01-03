# # l1 = [20,30,30,40,50]
# # l1.append(90)
# class Animal:
    
#     print("hello")
#     def bark(self):
#        print("bark")
       
#     def eat(self):
#        print("eat")
    
# dog = Animal()
# dog.bark()
# dog.eat()

# class Operation:
#   def addition(self,first_number,second_number):
#     print("The sum is: ",first_number + second_number)
    
#   def multiply(self,first_number,second_number):
#     print("The multiplication is: ",first_number*second_number)
    
#   def division(self,first_number,second_number):
#     print("The division is: ",first_number/second_number)
  
#   def substract(self,first_number,second_number):
#     print("The substraction is: ",first_number-second_number)
# calculation = Operation()
# calculation.addition(10,20)
# calculation.multiply(20,30)
# calculation.division(60,3)
# calculation.substract(10,10)


class Operation:
 
  def __init__ (self,first_number,second_number):
    self.first_number=first_number
    self.second_number=second_number
    
  def add(self):
    print(self.first_number+self.second_number)
  
  def substract(self):
    print(self.first_number-self.second_number)
    
  def multiply(self):
    print(self.first_number*self.second_number)
    
  def divide(self):
    print(self.first_number/self.second_number)

first_number=(int(input("Enter the first number: ")))
second_number=(int(input("Enter second number: ")))
object = Operation(first_number,second_number)
object.add()
object.substract()
object.multiply()
object.divide()