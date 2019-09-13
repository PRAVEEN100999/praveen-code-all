# names = ['praveen','rakesh','pushpendra']
# a = list(map(len, names))
# print(a)
# for i in a:
#     print(i)
def ieven (a):
    return a%2 == 0    
bb = [2.4,55,65,6,7,7,7,88,5,4,3,4]
aa = tuple(filter(ieven, bb))
print(aa)    