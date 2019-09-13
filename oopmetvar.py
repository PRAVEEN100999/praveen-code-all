class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        # instance variable 
        # print('init method / constructor get called')
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
    @ classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instance of {cls.__name__} class"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"    
p1  = Person('ram','kumar',24)
p2 = Person ('om','kumar',34)
print(Person.count_instances())