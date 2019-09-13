import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

#1.
# plt.plot([1,2,3],[5,6,7])
#2

# x = [2,4,6]
# y = [5,8,11]
# x2 = [3,8,4]
# y2 = [6,9,0]
# plt.plot(x,y,'g',label = 'lineone',linewidth = 6)
# plt.plot(x2,y2,'c',label = 'linetwo',linewidth = 6)
# plt.title('information')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend()
# plt.grid(True, color = 'k')

#3 bar 
# plt.bar([3,4,6,2,3],[1,4,6,8,3],label = "exampleone") 
# plt.bar([3,4,6,23,2],[1,2,3,4,5],label = "exampletwo",color ='g')
# plt.title('bar graph')
# plt.xlabel('bar number')
# plt.ylabel('bar height')
# plt.legend()

#4 histogram
# population_ages = [22,55,345,65,7,8,234,5,1,4,87,64,63,45,12,23,34,45,56,67,7,7,8,98,8,78]
# bins = [10,20,30,40,50,60,70,80,90,100,500,1000]
# plt.hist(population_ages,bins,histtype='bar' ,rwidth=0.8)
# plt.title('histogram')
# plt.xlabel('x axis')
# plt.ylabel('y axis')

#5 scatter plot
# x = [1,3,5,6,7,8,5,3,4]
# y  = [1,2,3,4,5,6,7,8,9]
# plt.scatter(x,y, label='skitcat',color='k',s=24,marker="o")
# plt.xlabel("x axis ")
# plt.ylabel("y label")
# plt.title('scatter plot')

#6 stack plot
# days = [1,2,3,4,5]
# sleeping = [7,8,6,11,7]
# eating = [2,3,4,3,2]
# working = [7,8,7,2,2]
# playing = [8,5,7,8,13]

# plt.plot([],[],color = 'm',label ='sleeping',linewidth = 5)
# plt.plot([],[],color = 'c',label ='eating',linewidth = 5)
# plt.plot([],[],color = 'r',label ='working',linewidth = 5)
# plt.plot([],[],color = 'k',label ='playing',linewidth = 5)
# plt.stackplot(days,sleeping,eating,working,playing,colors = ['m','c','r','k'])
# plt.xlabel('x axis')
# plt.ylabel('y label')
# plt.title('stack k plot')
# plt.legend()
# plt.show()


#7 pie chart
# slices = [7,2,2,13]
# activies = ['sleeping','eating','working','playing']
# cols = ['c','m','r','b']
# plt.pie(slices,labels = activies,colors = cols,startangle = 90,
# shadow = True ,explode = (0,0.5,0,0),autopct = '%1.2f%%')
# plt.title('pie plot')

# 8 multiple plot
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.2)
plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2))
plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))    
plt.legend()
plt.show()

