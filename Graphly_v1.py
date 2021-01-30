from tkinter import*
import numpy as np
import matplotlib.pyplot as plt
root=Tk()
root.title('Graphly')
root.geometry("700x250")


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
        e1.insert(0,'Error \n click on restart')
    else:
        y=np.zeros(20)
        x=np.arange(1,21,1)
        for i in range(len(a1)):
            m=np.ones(20)
            m=np.power(x,a2[i])
            m=np.multiply(m,a1[i])
            y=np.add(y,m)
        plt.plot(x,y)
        plt.show()
        
    

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
