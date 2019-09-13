# example 1:
class Circle:
    pi = 3.14 #class variable 
    def __init__(self,radius):
        self.radius = radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius


c = Circle(4)
c1  = Circle(5)
print(c.calc_circumference())        


#example:
class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('ram','kumar',12)
p2 = Person('om','kum',14)
# p3 = Person('shiv','kmar',13)
print(Person.count_instance)