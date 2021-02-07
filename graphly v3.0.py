from tkinter import*
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
%matplotlib inline
root=Tk()
root.title('Graphly')
root.geometry("700x500")
coef=[]
power=[]
def eq_maker(ls1,ls2,fin):
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
        elif ls1[i]==-1:
            if ls2[i]==0:
                fin+='1'
            elif ls2[i]==1:
                fin+='- x'
            else:
                fin+='- x^'+str(ls2[i])
        else:
            if ls2[i]==0:
                fin+=str(ls1[i])
            elif ls2[i]==1:
                fin+=str(ls1[i])+'x'
            else:
                fin+=str(ls1[i])+'x^'+str(ls2[i])
    return fin
           
           
def adpo():
    s=e.get()
    s=int(s)
    power.append(s)
    e.delete(0,END)
    #e.insert(0,coef)
def adco():
    s=e.get()
    s=int(s)
    coef.append(s)
    e.delete(0,END)

def restart():
    e.delete(0,END)
    coef=[]
    power=[]
    
def backspace():
    e.delete(len(e.get())-1,END)
def plot1():
    plot(coef,power)
    
    
def plot(c,d):
    a1=[]
    a2=[]
    for i in range(len(c)):
        a1.append(c[i])
    for i in range(len(d)):
        a2.append(d[i])
    d=[]
    c=[]
    if len(a1)!=len(a2):
        e.insert(0,'Error \n click on restart')
        print(a1,"   ",a2)
        
    else:
        y=np.zeros(20)
        x=np.arange(1,21,1)
        for i in range(len(a1)):
            m=np.ones(20)
            m=np.power(x,a2[i])
            m=np.multiply(m,a1[i])
            y=np.add(y,m)
        fin='y = '
        string=eq_maker(a1,a2,fin)
        fig=Figure(figsize=(5,5),dpi=70)  
        plot1=fig.add_subplot(111)
        plot1.plot(x,y)
        plot1.title.set_text("Plot of : "+string)
        canvas=FigureCanvasTkAgg(fig,master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=330,y=120)
   
    
def click(x):
    st=e.get()
    st+=str(x)
    e.delete(0,END)
    e.insert(0,st)

e=Entry(width=50)
l1=Label(root,text='❄︎❄︎❄︎GRAPHLY    ❄︎❄︎❄︎')
bx=Button(master=root,height=2,width=10,text='Plot',command=plot1)
by=Button(master=root,height=2,width=10,text='Restart',command=restart)
ba=Button(master=root,height=2,width=10,text='Add as \nCoeffecient',command=adco)
bb=Button(master=root,height=2,width=10,text='Add as \nPower',command=adpo)
bc=Button(master=root,height=2,width=10,text='Backspace',command=backspace)



b1=Button(root,text="0",height=3,width=9,command=lambda: click(0))
b2=Button(root,text="1",height=3,width=9,command=lambda: click(1))
b3=Button(root,text="2",height=3,width=9,command=lambda: click(2))
b4=Button(root,text="3",height=3,width=9,command=lambda: click(3))
b5=Button(root,text="4",height=3,width=9,command=lambda: click(4))
b6=Button(root,text="5",height=3,width=9,command=lambda: click(5))
b7=Button(root,text="6",height=3,width=9,command=lambda: click(6))
b8=Button(root,text="7",height=3,width=9,command=lambda: click(7))
b9=Button(root,text="8",height=3,width=9,command=lambda: click(8))
b10=Button(root,text="9",height=3,width=9,command=lambda: click(9))
b11=Button(root,text=".",height=3,width=9,command=lambda: click('.'))
b12=Button(root,text="-",height=3,width=9,command=lambda: click('-'))
l1.place(x=400,y=20)

ba.place(x=20,y=70)
bb.place(x=120,y=70)
bc.place(x=220,y=130)
e.place(x=20,y=20)
bx.place(x=20,y=130)
by.place(x=120,y=130)


b2.place(x=20,y=210)
b3.place(x=110,y=210)
b4.place(x=200,y=210)
b5.place(x=20,y=280)
b6.place(x=110,y=280)
b7.place(x=200,y=280)
b8.place(x=20,y=350)
b9.place(x=110,y=350)
b10.place(x=200,y=350)
b11.place(x=200,y=430)
b1.place(x=110,y=430)
b12.place(x=20,y=430)


root.mainloop()
