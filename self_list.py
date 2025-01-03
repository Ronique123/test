class selfList():
    def __init__ (self,n_list):
        self.n_list = n_list
    
    def custom_append(self, value):
        self.n_list+= [value]
        
    def display(self):
        print(self.n_list)
        

l1 = selfList([10,20])
l1.display()
l1.custom_append(50)
l1.display()
list()
len()