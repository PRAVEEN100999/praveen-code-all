l = [1,2,3]
for i in l:
    print(i)
print(map(lambda a : a*2 ,l))

def fun(n):
    for i in range(1,n+1):

        yield(i)

for  num in fun(10):
    print(num)