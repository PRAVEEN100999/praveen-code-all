def total(*args):
    print(args)
    print(type(args))
total(3,54,657,76,76,0,88,87,8)    
def func(l,**kwargs):
    if kwargs.get('reverse')==True :
        return [name [::-1].title() for name in l]
    else :
        return [name.title() for name in l ] 

name = ['praveen ','rakesh','pushpendra']
print(func(name,reverse = True))       