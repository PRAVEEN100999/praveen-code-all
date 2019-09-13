class Person:
    def __init__(self,f_name,l_name,age):
        # instance variable 
        print('init method / constructor get called')

        self.first_name = f_name
        self.last_name = l_name 
        self.age = age
p1  = Person('ram','kumar',24)
p2 = Person ('om','kumar',34)
print(p1.first_name)