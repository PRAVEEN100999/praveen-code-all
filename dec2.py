def dec_func(any_func):
    def wrap_func(*args, **kwargs):
        print('hello im decorator')
        return any_func(*args, **kwargs)
    return wrap_func()

@dec_func # shortcut
def fun1(a):
    print(f'hello i m fun1{a}')
fun1(7)


@dec_func #shortcut
def add():
    return a + b
# dec_func(add)    
print (add(3,5))    

     