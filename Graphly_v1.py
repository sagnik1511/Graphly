from tkinter import*
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
root=Tk()
root.title('Graphly')
root.geometry("700x850")

def eq_maker(ls1,ls2):
    fin='y= '
    for i in range(len(ls1)):
        if i>0 and ls1[i]>0:
            fin+='+'
        if ls1[i]==1:
            if ls2[i]==0:
                fin+='1'
            elif ls2[i]==1:
                fin+='x'
            else:
                fin+='x^'+str(ls2[i])
        else:
            if ls2[i]==0:
                fin+=str(ls1[i])
            elif ls2[i]==1:
                fin+=str(ls1[i])+'x'
            else:
                fin+=str(ls1[i])+'x^'+str(ls2[i])
    return fin
           
           
   
   
def coef():
    lst1=e1.get().split(",")
    for i in range(len(lst1)):
        lst1[i]=int(lst1[i])
    return lst1

def power():
    lst2=e2.get().split(",")
    for i in range(len(lst2)):
        lst2[i]=int(lst2[i])
    return lst2
def restart():
    e1.delete(0,END)

def plot():
    a1=coef()
    a2=power()
    e1.delete(0,END)
    e2.delete(0,END)
    if len(a1)!=len(a2):
        e1.inser(0,'Error \n click on restart')
    else:
        y=np.zeros(20)
        x=np.arange(1,21,1)
        for i in range(len(a1)):
            m=np.ones(20)
            m=np.power(x,a2[i])
            m=np.multiply(m,a1[i])
            y=np.add(y,m)
        string=eq_maker(a1,a2)
        fig=Figure(figsize=(5,5))  
        plot1=fig.add_subplot(111)
        plot1.plot(x,y)
        plot1.title.set_text("Plot of : "+string)
        canvas=FigureCanvasTkAgg(fig,master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=50,y=250)
        toolbar=NavigationToolbar2Tk(canvas, window)
        toolbar.update()
       
   

l1=Label(text='Enter the coeffecients of powers of x \nseparating with commas')
l2=Label(text='Enter the powers of x \nseparating with commas')
e1=Entry(width=50)
e2=Entry(width=50)
b1=Button(master=root,height=2,width=10,text='Plot',command=plot)
b2=Button(master=root,height=2,width=10,text='Restart',command=restart)
l1.place(x=30,y=10)
l2.place(x=70,y=70)
e1.place(x=240,y=10)
e2.place(x=240,y=70)
b1.place(x=100,y=130)
b2.place(x=100,y=170)
root.mainloop()
