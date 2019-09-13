import tkinter as tk
from tkinter import ttk 
win = tk.Tk()
win.title("PRAVEEN KUMAR")
   

# create lebel 

namel =ttk.Label(win, text= "enter your name:")
namel.grid(row =0 ,column = 0,sticky= tk.W) 
agel =ttk.Label(win, text= "enter your age:")
agel.grid(row =2 ,column = 0 , sticky = tk.W)   
emaill =ttk.Label(win, text= "enter your email:")
emaill.grid(row =1 ,column = 0 , sticky = tk.W)  
genderl =ttk.Label(win, text= "enter your gender:")
genderl.grid(row =3 ,column = 0 , sticky = tk.W)  

# create a entry box or text box
namev = tk.StringVar()
namee = ttk.Entry(win, width= 16 , textvariable = namev)
namee.grid(row=0,column =1)
namee.focus()
emailv = tk.StringVar()
emaile = ttk.Entry(win, width= 16 , textvariable = emailv)
emaile.grid(row=1,column =1)

agev = tk.StringVar()
agee = ttk.Entry(win, width= 16 , textvariable = agev)
agee.grid(row=2,column =1)


# create combo  box
genderv = tk.StringVar()
genderc = ttk.Combobox(win , width= 14, textvariable=genderv,state= 'readonly')
genderc['values'] = ('male', 'female', 'other')
genderc.current(0)
genderc.grid(row =3,column = 1) 
   
#  # create button
def action():
    nameu = namev.get()
    emailu = emailv.get()
    ageu = agev.get() 
    print(f'{nameu} : name, {emailu}: email, {ageu}: age')
submitb =ttk.Button(win ,text ='Submit', command = action) 
submitb.grid(row = 4 ,column = 3)
  


win.mainloop()