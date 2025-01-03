def func_in_func(normal_arg,*arg,**keyarg):
    print(keyarg)
    print(type(arg))
    total = 0
    for i in arg:
        total = total + i
    print("sum is",total)
    
    print(max(arg))
    print(min(arg))

func_in_func(909, 20,30,40,50,name = "Ram", address = "ktm")