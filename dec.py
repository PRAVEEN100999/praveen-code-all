def dec_func(any_func):
    def wrap():
        print("hello im decorator")
        any_func()
    return wrap()
@dec_func # shortcut
def fun1():
    print("hello i m fun1")



@dec_func #shortcut
def fun2():
    print("hello i m fun2")

     