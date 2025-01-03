from funcsum import funsum
def mon(n1,n2):

    n1=input("Enter a number:")
    n2=input("Enter second number:")
    n1=int(n1)
    n2=int(n2)
    sum = funsum(n1,n2)
    print (sum)
    if(sum % 2==0):
        print("The number is even")
    else:
        print("The number is odd")
mon(n1=0,n2=0)
    