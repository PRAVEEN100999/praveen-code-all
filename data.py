def square(a):
    return a**2

l = [1,2,3,4]
def my(func , p):
    new= []
    for item in p :
        new.append(func(item))
    return new 
print(my(square,l))
print(my(lambda a :a**2,l))
  
#list comprehension 
def my2(func,l):
    return [func(item) for item in l] 
print(my2(lambda a:a**3,l))    

