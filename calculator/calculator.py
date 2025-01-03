print("Choose an operation: ")
print("1 - add")
print("2 - substract")
print("3 - multiply")
print("4 - divide")
option = int(input("Choose an operation: ")) 
result = 0  #removing error

if(option in [1,2,3,4]):
    first_number = int(input("Enter 1st Number for calculation: "))
    second_number = int(input("Enter 2nd Number for calculation: "))
    
    if(option == 1):    #add
        from add import add
        result = add(first_number,second_number)
        
    elif(option == 2):  #substract
        from substract import substract
        result = substract(first_number,second_number)
    
    elif(option == 3):  #multiply
        from multiply import multiply
        result = multiply(first_number,second_number)
    
    elif(option == 4): #divide
        from divide import divide
        result = divide(first_number,second_number)
else:
    print("Invalid Option Selected")
print(result)