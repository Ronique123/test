try:
    def add(n_args, *args, **kwargs):
        total = n_args + sum(args)
        print(args)
        print(total)
    
    add(20,30,40,50)

except Exception as exe:
    print("Error Occured.")

print("ok")