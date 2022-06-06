# SILENT AUCTIONING PROGRAM.
#DAY 10 incode PROJECT 
# AUTHOR LAWRENCE
# VERSION NO: 001
# LICENCE FREE TO USE.
#HAVE FUN
#since the python interpreter is a calculator
# that method seems long and atleast complicated.
# for further review in the meantime.

###algol read intput append to list work with the list.

from tkinter import *

expression = " "

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = " "
        
    except:
        equation.set(" 504 Error ")
        expression = " "
        equation.set(" ")
        
        
def clear():
    global expression
    expression= " "
    equation.set(" ")
    
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.title("Simple Calculator")
    # gui.geometry("270x150")
    equation = StringVar()
    
    expression_field = Entry(gui,textvariable=equation)
    expression_field.grid(columnspan=5,ipadx=60,ipady=25)
    
    # #button loop function
    # for i in range(3):
    #     for j in range(3):
    #         button =  Button(gui,text=f' {j} ',fg='white',bg='black',
    #                     command=lambda: press(j),height=1,width=7)
    #         button.grid(row=i+1,column=j)
    
    button1 = Button(gui,text=' 1 ',fg='white',bg='black',
                     command=lambda: press(1),height=1,width=7)
    button1.grid(row=2,column=1)
    
    minus = Button(gui,text=' - ',fg='white',bg='black',
                     command=lambda: press('-'),height=1,width=7)
    minus.grid(row=2,column=4)
    
    plus = Button(gui,text=' + ',fg='white',bg='black',
                     command=lambda: press('+'),height=1,width=7)
    plus.grid(row=3,column=4)

    divide = Button(gui,text=' / ',fg='white',bg='black',
                     command=lambda: press('/'),height=1,width=7)
    divide.grid(row=4,column=4) 

    multiply = Button(gui,text=' X ',fg='white',bg='black',
                     command=lambda: press('*'),height=2,width=7)
    multiply.grid(row=5,column=3) 
 
 
    
    button2 = Button(gui,text=' 2 ',fg='white',bg='black',
                     command=lambda: press(2),height=1,width=7)
    button2.grid(row=2,column=2)  
    
    button3 = Button(gui,text=' 3 ',fg='white',bg='black',
                     command=lambda: press(3),height=1,width=7)
    button3.grid(row=2,column=3) 
    
    
    button4 = Button(gui,text=' 4 ',fg='white',bg='black',
                     command=lambda: press(4),height=1,width=7)
    button4.grid(row=3,column=1) 
    
    button5 = Button(gui,text=' 5 ',fg='white',bg='black',
                     command=lambda: press(5),height=1,width=7)
    button5.grid(row=3,column=2) 
    
    button6 = Button(gui,text=' 6 ',fg='white',bg='black',
                     command=lambda: press(6),height=1,width=7)
    button6.grid(row=3,column=3) 
    
    
    button7 = Button(gui,text=' 7 ',fg='white',bg='black',
                     command=lambda: press(7),height=1,width=7)
    button7.grid(row=4,column=1)
     
    button8 = Button(gui,text=' 8 ',fg='white',bg='black',
                     command=lambda: press(8),height=1,width=7)
    button8.grid(row=4,column=2)  
    
    button9 = Button(gui,text=' 9 ',fg='white',bg='black',
                     command=lambda: press(9),height=1,width=7)
    button9.grid(row=4,column=3)
    
    clear1 = Button(gui,text=' Clear ',fg='white',bg='black',
                     command=lambda: clear(),height=2,width=7)
    clear1.grid(row=5,column=1)   
    
    button0 = Button(gui,text=' 0 ',fg='white',bg='black',
                     command=lambda: press(0),height=2,width=7)
    button0.grid(row=5,column=2)
    
    equal = Button(gui,text=' = ',fg='white',bg='black',
                     command=lambda: equal_press(),height=2,width=7)
    equal.grid(row=5,column=4)
    gui.mainloop()