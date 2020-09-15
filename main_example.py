'''
Mike Beradino
9-02-2020
Tkinter examples
'''
from tkinter import *

master = Tk()
master.title("Calc")
master.geometry("300x150")  # Width x Height
master.configure(background='gray20')


def print_box_val(numb):
    input_box_string_saved = String_input_value.get()
    input_box_string = str(numb) + input_box_string_saved
    String_input_value.set(input_box_string)

def preform_math():
    input_box_string_saved = String_input_value.get()
    print (eval(input_box_string_saved))
    String_input_value.set(eval(input_box_string_saved))

numb = 1
for i in range (1,4):
    for j in range (0,3):
        strnumb = str(numb)
        button_name = "button" + strnumb
        button_name = Button(master, text= numb, command=lambda numb=numb: print_box_val(numb), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=i, column = j)
        numb = numb +1

#buttons
Button(master, text='caculate', command=preform_math, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=7, column = 1)
add = "+"
Button(master, text='+', command=lambda add=add: print_box_val(add), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=1, column = 4)
subtract = "-"
Button(master, text='-', command=lambda subtract=subtract: print_box_val(subtract), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=2, column = 4)
divide = "/"
Button(master, text='/', command=lambda add=add: print_box_val(divide), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=3, column = 4)
mutiply = "*"
Button(master, text='*', command=lambda add=add: print_box_val(mutiply), bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=4, column = 4)
#
#Button(master, text='print_test', command=test, bg="gray20", fg="lime green", highlightbackground="gray20", activebackground="deep sky blue").grid(row=7, column =0)

'''
# check box
var1 = IntVar()
Checkbutton(master, text='mm --> in', bg="gray20", fg="lime green", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='in --> mm', bg="gray20", fg="lime green", variable=var2).grid(row=1, sticky=W)
'''

#Lables with entry boxes
#Label(master, text='units to convert',bg="gray20", fg="white", highlightbackground="gray20",).grid(row=3)
#Label(master, text='Last Name').grid(row=4)

String_input_value = StringVar(master, value='')
Total_box = Entry(master,textvariable=String_input_value)
Total_box.grid(row=0, columnspan=4, sticky=W + E)





master.mainloop()
