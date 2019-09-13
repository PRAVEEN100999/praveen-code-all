# name = input("enter your name :")
# age = int(input("enter your name and age :"))
# if (name[0]=='a'or name[0] =='A') and age >= 10:
#     print("you are eligble..for movie")
# else :
# #     print("not eligble for movie :")    
# name =""
# if name:
#     print("a")
# else :
#     print("b")   
# n = input("enter your no")
# a = len(n)
# print (a)
# total =0
# i = 1
# while i<=a:
#     total += int(n[i-1])
#     print(total) 
#     i +=1
# name = input("enter your name ")
# i = 0
# temp = ""
# while i <len(name):
#     if name[i] not in temp:
#         temp += name[i]
#         print(f"{name[i]}: {name.count(name[i])}")
#     i += 1
win = 87
guess = 0
no = int(input("guess the no btwn 1 to 100"))
game = False 
while not game :
    if no == win:
        print(f"you win and you guess this no in {guess} times ....")
        game =True 
    else :
        if no <win:
            print("too low") 
            guess += 1
            no = int(input("enter again "))
        else :
            print("too high") 
            guess += 1
            no = int(input("enter again "))
        
