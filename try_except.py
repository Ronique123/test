try:
    
    name = "Rbson"
    num = 1
    print(name)
    print(name + sum)
    
    
except NameError as exe:
    print("Invalid")

except Exception as exe:
    print(exe.__class__)
    print("Error Occured.")