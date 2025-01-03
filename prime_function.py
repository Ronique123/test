def prime(number):
    if (number > 1):
  
        for i in range(2,number):
  
            if (number % i == 0):
                print("Entered number is not a prime number")
                
            else:
                print("Entered number is a prime number")
    else:
        print("Enter a number Greater than 1")
    return(number)
def db_conn():
    pass