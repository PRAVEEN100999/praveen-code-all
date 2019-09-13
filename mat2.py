from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [2,5,4,4,4]
y = [4,4,7,3,6]
x1 = [1,3,5,6,7]
y1 = [2,4,6,7,8]
plt.plot(x,y,'g',label='line one',linewidth = 5)
plt.plot(x1,y1,'c',label='lne two',linewidth = 5)
plt.title("hello sir")
plt.xlabel("x axis ")
plt.ylabel("y axis ")
plt.legend()
plt.grid(True,color = 'k')
plt.show()
