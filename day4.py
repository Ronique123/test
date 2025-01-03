# l1=(2,4,5,"ram")
# print(l1)
# #l1[0]="hari"   #in tuple value can not be changed
# l2=2,3,4
# print(type(l2))
# s1={55,1,2,3,4,5,5}    #set = no index and duplicate value doesnt print
# print(s1)
# l2 = set(l1)
# print(l2)
d1 = {"name":"Ram"  , "address":"kathmandu" }   #name=key , Ram = value
name = d1["name"]       #if error displays key error 
address = d1.get("address") #if error displays none
print(name)
print(address)
d1["age"]=20    #adding age on dictionary
age = d1.get("age")
print(age)
d1["name"]="rbson"  #name already exists. so overwriting value in key name
name = d1.get("name")
print(name)
print(d1)   #print dic
d1.pop("name")
print(d1)

#list-[] allows multiple value
#set-{}   no multiple value - prints on ascending order
#tuple-() allow multiple value but doesnt print
#dictionary={} {key:value , Key:value}