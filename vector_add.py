from tkinter import *
from math import *
from random import *

# Master window
master = Tk() 
master.configure(bg='gray90')
master.geometry('1300x800')
master.bind('<Escape>',quit)

# Creating grids
grid1 = Canvas(master, bg='white', width=400, height=400)
grid1.place(x=225, y=50)
grid2 = Canvas(master, bg='white', width=400, height=400)
grid2.place(x=675, y=50)
for t in range(0,20):
    grid1.create_line(0,20*t,400,20*t, width=1, fill='gray50')
    grid1.create_line(20*t,0,20*t,400, width=1, fill='gray50')
    grid2.create_line(0,20*t,400,20*t, width=1, fill='gray50')
    grid2.create_line(20*t,0,20*t,400, width=1, fill='gray50')
grid1.create_line(0,200,400,200, width=3, fill='black')
grid1.create_line(200,0,200,400, width=3, fill='black')
grid2.create_line(0,200,400,200, width=3, fill='black')
grid2.create_line(200,0,200,400, width=3, fill='black')

# Creating arrows manually
x1 = randint(-9,9)
y1 = randint(-9,9)
x2 = randint(-9,9)
y2 = randint(-9,9)
arrow1 = grid1.create_line(200,200,200+20*x1,200-20*y1, width=6, arrow=LAST, fill='dark green', arrowshape=(16,20,6))
arrow2 = grid2.create_line(200,200,200+20*x2,200-20*y2, width=6, arrow=LAST, fill='blue', arrowshape=(16,20,6))

# Creating problem statement and answer field
statement = Frame(master, bg='white', height=200, width=800)
statement.pack_propagate(False)
statement.place(x=250 , y=500)
vadd_statement = 'Vector A (left) and Vector B (right) are shown. In the spaces provided below, provide the x and y components of the vector sum, A+B.'
vadd = Label(statement, text=vadd_statement, wraplength=800, font=('verdana', 20), justify=LEFT)
vadd.pack(side='top')
vadd_ans1 = Label(statement, text='The vector sum A+B = ', font=('verdana', 20))
vadd_ans1.pack(side='left')
xresp = Entry(statement, width=3)
xresp.pack(side='left')
vadd_ans2 = Label(statement, text='ihat + ', font=('verdana', 20))
vadd_ans2.pack(side='left')
yresp = Entry(statement, width=3)
yresp.pack(side='left')
vadd_ans3 = Label(statement, text='jhat.', font=('verdana', 20))
vadd_ans3.pack(side='left')

# Submitting and grading answer
score = IntVar()
score.set(0)
xcomp = IntVar()
ycomp = IntVar()
feedback = Frame(master, bg='white', height=59, width=175)
feedback.pack_propagate(False)
feedback.place(x=1100, y=50)
rightwrong = Label(feedback, text='', fg='white', bg='white', font=('verdana', 44))
rightwrong.pack()
def vadd_find():
    score.set(0)
    xcomp.set(xresp.get())
    ycomp.set(yresp.get())
    vadd_x = x1+x2
    vadd_y = y1+y2
    print('Correct: x='+str(vadd_x)+' y='+str(vadd_y))
    if xcomp.get() == vadd_x:
        if ycomp.get() == vadd_y:
            score.set(1)
    if score.get() == 0:
        fb = 'Wrong'
        fbcolor = 'black'
        bgcolor = 'red'
    if score.get() == 1:
        fb = 'Correct'
        fbcolor = 'black'
        bgcolor = 'green'
    rightwrong.configure(text=fb, fg=fbcolor, bg=bgcolor)
submit = Button(statement, text='Submit Answer', command=vadd_find)
submit.pack(side='right')

#print(statement.width)

# Main loop
master.mainloop() 
