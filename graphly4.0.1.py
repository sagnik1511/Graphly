"""
Created on Thu Jun  3 18:50:28 2021

@author: Kylo Ren
"""

# Graphy 4.0.1

"""Updated Version of Graphly , now adding values will be easier.
Tried to put altogether in a single file.
Try the GUI and send feedbacks.
"""



# Libraries -------------------------------------------------------------------------------



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import tkinter






# Functions ---------------------------------------------------------------------------------


def negpow(arr, k):
  xx = arr.tolist()
  ar = []
  for i in xx:
    ar.append( pow( i, k ) )
  return np.array( ar )


def Exit():
    if tkinter.messagebox.askquestion( 'Exit ', 'Do you really want to exit ?' ) == 'yes':
        root.destroy()


def coef_apply_fn():
    try :
        x1 = int( coef_lower_entry.get() )
        x2 = int( coef_upper_entry.get() )
        coef_lower_entry.delete( 0, tkinter.END )
        coef_upper_entry.delete( 0, tkinter.END )
        assert x1<=x2
        coef_scaler.config( from_ = x1, to = x2 )
    except :
        coef_lower_entry.delete( 0, tkinter.END )
        coef_upper_entry.delete( 0, tkinter.END )
        tkinter.messagebox.showwarning( "Add Coefficients", "Add valid numbers!" )
    
def power_apply_fn():
    try :
        x1 = int( power_lower_entry.get() )
        x2 = int( power_upper_entry.get() )
        power_lower_entry.delete( 0, tkinter.END )
        power_upper_entry.delete( 0, tkinter.END )
        assert x1<=x2
        power_scaler.config( from_ = x1, to = x2 )
    except :
        power_lower_entry.delete( 0, tkinter.END )
        power_upper_entry.delete( 0, tkinter.END )
        tkinter.messagebox.showwarning( "Add Powers", "Add valid numbers!" )


def add_value_fn():
    x1 = int( coef_scaler.get() )
    x2 = int( power_scaler.get() )
    coef_entry.insert( tkinter.END, str(x1) + ',' )
    power_entry.insert( tkinter.END, str(x2) + ',' )


def delete_value_fn():
    try:
        power_array = list( power_entry.get()[:-1].split(',') )
        coef_array = list( coef_entry.get()[:-1].split(',') )
        #print(len(power_array))
        power_entry.delete( 0, tkinter.END )
        coef_entry.delete( 0, tkinter.END )
        assert power_array[0] != ''
        for i in range( len( power_array ) - 1 ):
            power_entry.insert( tkinter.END, power_array[i] + ',')
        for i in range( len( coef_array ) - 1 ):
            coef_entry.insert( tkinter.END, coef_array[i]+',')
    except:
        tkinter.messagebox.showwarning( "Delete Variables", "No values to delete!" )
          
        
def restart_fn():
    power_entry.delete( 0, tkinter.END )
    coef_entry.delete( 0, tkinter.END )
    coef_scaler.config( from_ = -1000, to = 1000 )
    power_scaler.config( from_ = -10, to = 10 )
    fig=Figure(figsize=( 5, 5 ), dpi = 48 )  
    plot=fig.add_subplot( 111 )
    canvas=FigureCanvasTkAgg( fig, master = root )
    canvas.draw()
    canvas.get_tk_widget().place( x = 420, y = 129 )
    


def plot_fn():
    try:
        y=np.zeros( 80 )
        x=np.arange( 1, 21, 0.25 )
        power_array = list(map(int , power_entry.get()[:-1].split(',') ))
        coef_array = list(map(int ,  coef_entry.get()[:-1].split(',') ))
        for i in range(len( power_array ) ):
            ones = np.arange( 1, 21, 0.25 )
            if power_array[i] >= 0 :
                ones = pow( ones, power_array[i]  )
            else:
                ones = negpow( ones, power_array[i] )
            ones = ones * coef_array[i] 
            y = np.add( y, ones )
        
        fig=Figure(figsize=( 5 , 5 ), dpi = 48 )  
        plot=fig.add_subplot( 111 )
        plot.plot( x, y )
        canvas=FigureCanvasTkAgg( fig, master = root )
        canvas.draw()
        canvas.get_tk_widget().place( x = 420, y = 129 )
    except:
        tkinter.messagebox.showwarning( 'Graphly', 'Add valid values!' )
    
    
    
     
    
    
#Header --------------------------------------------------------------------------------


root = tkinter.Tk()
root.title( 'Graphly4.0.1' )
root.geometry( "700x470" )
root.config(bg = 'lightskyblue')





# EntryBoxes ---------------------------------------------------------------------------


coef_entry = tkinter.Entry( root, width = 90 )
power_entry = tkinter.Entry( root, width = 90 )
coef_lower_entry = tkinter.Entry( root, width = 10 )
coef_upper_entry = tkinter.Entry( root, width = 10 )
power_lower_entry = tkinter.Entry( root, width = 10 )
power_upper_entry = tkinter.Entry( root, width = 10 )






# Labels --------------------------------------------------------------------------------


heading = tkinter.Label(root,text='❄︎❄︎❄︎GRAPHLY   ❄︎❄︎❄︎', bg = 'lightskyblue', font = ( "Courier", 20 ) )
coef_label = tkinter.Label( root, text = 'Coefficient Values' , bg = 'lightskyblue' )
power_label = tkinter.Label( root, text = 'Power Values' , bg = 'lightskyblue')
coef_heading = tkinter.Label( root, text = 'Set Coefficient Value', bg = 'lightskyblue' )
power_heading = tkinter.Label( root, text = 'Set Power Value', bg = 'lightskyblue' )
coef_from = tkinter.Label( root, text = 'Lower Value', bg = 'lightskyblue' )
coef_to = tkinter.Label( root, text = 'Upper Value', bg = 'lightskyblue' )
power_from = tkinter.Label( root, text = 'Lower Value', bg = 'lightskyblue' )
power_to = tkinter.Label( root, text = 'Upper Value', bg = 'lightskyblue' )
see_figure_label = tkinter.Label( root, text = 'See Figure Down Here' )






# Scales ---------------------------------------------------------------------------------


coef_scaler = tkinter.Scale( root, from_ = -1000, to = 1000,
                    orient = tkinter.HORIZONTAL, length = 200,
                    bg = 'royalblue', highlightbackground = 'royalblue',
                    activebackground = 'mediumblue', trough = 'deepskyblue')

power_scaler = tkinter.Scale( root, from_ = -10, to = 10 , 
                     orient = tkinter.HORIZONTAL, length = 200,
                     bg = 'royalblue', highlightbackground = 'royalblue',
                     activebackground = 'mediumblue', trough = 'deepskyblue')






# Buttons --------------------------------------------------------------------------------


coef_apply_button = tkinter.Button( root, text = ' Apply',
                           height = 1, width = 6,
                           command = coef_apply_fn,
                           bg = 'royalblue', bd = 4 )

power_apply_button = tkinter.Button( root, text = ' Apply',
                            height = 1, width = 6,
                            command = power_apply_fn,
                            bg = 'royalblue', bd = 4 )

add_value_button = tkinter.Button( root, text = 'Add \nValue',
                          height = 3, width = 9,
                          command = add_value_fn,
                          bg = 'royalblue', bd = 4 )

delete_value_button = tkinter.Button( root, text = 'Delete \nValue',
                             height = 3, width = 9,
                             command = delete_value_fn,
                             bg = 'royalblue', bd = 4 )

restart_button = tkinter.Button( root, text = 'Restart',
                        height = 3, width = 9,
                        command = restart_fn,
                        bg = 'royalblue', bd = 4 )

exit_button = tkinter.Button( root, text = 'Exit',
                     height = 3, width = 9,
                     command = Exit,
                     bg = 'royalblue', bd = 4 )

plot_button = tkinter.Button( root, text = 'PLOT',
                     height = 5, width = 40,
                     command =plot_fn,
                     bg = 'aqua', bd = 4 )






# Plaecholders ----------------------------------------------------------------------------


heading.place( x = 90, y = 20)

coef_label.place( x = 10, y = 70 )
power_label.place( x = 34, y = 100 )
coef_entry.place( x = 115, y = 70 )
power_entry.place( x = 115, y = 100 )



coef_heading.place( x = 180, y = 150 )
coef_from.place( x = 20, y = 170 )
coef_lower_entry.place( x = 100, y = 170 )
coef_to.place( x = 20, y = 190 )
coef_upper_entry.place( x = 100, y = 190 )
coef_scaler.place( x = 170, y = 170 )
coef_apply_button.place( x = 20, y = 210 )



power_heading.place( x = 190, y = 260 )
power_from.place( x = 20, y = 280)
power_lower_entry.place( x = 100, y = 280 )
power_to.place( x = 20, y = 300 )
power_upper_entry.place( x = 100, y = 300 )
power_scaler.place( x = 170, y = 280 )
power_apply_button.place( x = 20, y = 320 )


add_value_button.place( x = 20, y = 390 )
delete_value_button.place( x = 112, y = 390 )
exit_button.place( x = 204, y = 390 )
restart_button.place( x = 296, y = 390 )
plot_button.place( x = 400, y = 376 )






# Canvas -----------------------------------------------------------------------------------

fig=Figure(figsize = (5, 5), dpi = 48)  
plot=fig.add_subplot(111)
canvas=FigureCanvasTkAgg(fig, master = root)
canvas.draw()
canvas.get_tk_widget().place(x = 420, y = 129)
    
root.mainloop()

