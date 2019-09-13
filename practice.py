# from tkinter import *
# m1 = PanedWindow() 
# m1.pack(fill = BOTH, expand = 1) 
# left = Entry(m1, bd = 5) 
# m1.add(left) 
# m2 = PanedWindow(m1, orient = VERTICAL) 
# m1.add(m2) 
# top = Scale( m2, orient = HORIZONTAL) 
# m2.add(top) 
# mainloop() 


# pactice 1
# def pac():
#     while True :
#         a = input("enter the string you want")
#         if (a=='quit'):
#             break;
#         if (len(a)<3):
#             print("too small")
#             continue
#         print("sufficient length")

# pac()        

# practice 
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,5,6,8,4]
plt.scatter(x,y,label='skitscat',color='m',s=24,marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title('scatter plot')
plt.legend()
plt.show()