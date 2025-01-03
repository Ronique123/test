try:
    age = 16 
    if age > 16:
        print("You can drive")
    else:
        raise Exception("You cannot Drive")
except Exception as exe:
    print(exe)
