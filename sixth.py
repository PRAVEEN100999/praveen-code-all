# days = ('mon','tues','wed')
# print(days.count("mon"))
# print(days.index("wed"))
# print(days[:2])#slicing


# print(len(days))
mixed =(1,2,3,4,5.0)
for i in mixed:
    print(i)

print(type(mixed)) #cheak the data type 
mixed = 1,2,3,4,5 # another way  to write tuple 
aa = 'ram','om','shiv'
print(type(mixed))
print(type(aa))
days =('mon','tues','wed')
day1,day2,day3 =(days) # unpacking
print(day1)
print(day2)
print(day3)
fav = ('a','b',['c','d'])
# fav[1].pop()
fav[2].pop()
print(fav)
print(min(mixed))
print(max(mixed))
print(sum(mixed))
#print(min(fav)) not work because string is used 