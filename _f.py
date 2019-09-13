def out_func():
    def in_func():
        print("inside inner func ")
    return in_func

var = out_func()
var()
  

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power
cude = to_power(3)
print(cube(5))  
