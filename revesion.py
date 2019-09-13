# name = input("enter your name ")
# i = 0
# temp_var =""
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]}:{name.count(name[i])}")
#         i += 1  
def squarelist(l):
    square =[]
    for i in l:
        square.append(i**2)
    return square
    # print(square)
number = list(range(1,11))
print(squarelist(number))    

list = [1,2,3,4,5,6]
a = list.pop()
print(a)
print(list)  