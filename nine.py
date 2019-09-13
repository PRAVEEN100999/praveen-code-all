def cube(n):
    d ={}
    for i  in range(1,n+1):
        d[i]=i**3
    # d = dict.fromkeys(range(1,n+1),range(1**3,n**3))
    return d
# no = int(input('enter the no')) 
print(cube(10))  