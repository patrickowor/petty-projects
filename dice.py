import random
from tkinter import *

# define the window 
window = Tk()
window.title('dice')
window.minsize(50,50)
#window.background('red')


# dice variables and functions 
def dice():
    dice1 = str(random.randint(1, 6))
    dice2 = str(random.randint(1, 6))
    button. config(text='roll again ', bg='green', )
    dices = dice1, dice2
    diced = dices
    label.config(text = diced)
    

# exit function 
def end():
    exit()
    
#font variables   
fontss = ('times', 90, 'bold') 
buts = ('times', 30, 'bold') 

# widgets 
button = Button(window, text = 'roll dice', fg='white',bg='red', command= dice )
button.config(font = buts)
button.pack()

label = Label(window, text='roll', bg='black', fg='white')
label.config(font = fontss)
label.pack()


Button(window, text= 'end', fg = 'white',  bg = 'red', command = end).pack()

#loop inisiate
window.mainloop()