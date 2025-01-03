# # l1 = [10,20,"Rbson",30.5,"MT15"]
# # print(l1)
# # print(l1[4])
# l2=[20,30]
# l2.append("Ram") #append add value to the last
# print(l2)
# l2.insert(0,"Hari")    #insert value to the given position
# print(l2)
# l2.insert(3,45)
# print(l2)
# l2[1]=5     #changing the position value (modify)
# print(l2)
# l2.remove(5) #remove value acc. pos
# print(l2)
# l2.pop(1)    #remove value acc. pos
# print(l2)
st_num = input("Enter a starting number: ")
st_num = int(st_num) 
lst_num = input("Enter a  last number: ")
lst_num = int(lst_num)
div_num = input("Enter a number for division: ")
div_num = int(div_num)
can_mul = []
cant_mul = []
for i in range(st_num,lst_num):
    if(i%div_num==0):
        can_mul.append(i)
    else:
        cant_mul.append(i)
print(st_num)
print(lst_num)
print(can_mul)
print(cant_mul)
