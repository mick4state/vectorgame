### SETTING UP ###
from tkinter import *
from math import *
from random import *
# Create master window
master = Tk()
master.configure(bg='gray90')
master.geometry('1300x800')
master.bind('<Escape>',quit)
# Defining random variables
quiz = BooleanVar()
quiz.set(False)
next = BooleanVar()
next.set(False)
done = BooleanVar()
q_type_list = []
mastery_list = []
score_list = []
scorecard_list = []
error_list = []
max_score = IntVar()
max_score.set(5)
q_images = Frame()
q_statement = Frame()
q_answer = Frame()
score_frame = Frame()
question_frame = Frame()
submit = Button()
next = Button()
feedback_frame = Frame()
feedback_label = Label()
answer1 = DoubleVar()
resp1 = DoubleVar()
answer2 = DoubleVar()
resp2 = DoubleVar()
# Place permanent header
header = Frame(master, height=50, bg='white')
header.pack_propagate(False)
header.pack(side=TOP, fill=X)
header_label = Label(header, text='Welcome to Brendon\'s Amazing Vector Game!!!', font='trebuchet 20 bold italic', fg='white', bg='dark green', highlightthickness=5, highlightbackground='gray20')
header_label.pack(expand=YES, fill=BOTH)

### QUIZ INITIALIZATION FUNCTION ###
def make_quiz():
# Destroy problem type selection frame
    q_type_frame.destroy()
# Creating permanent frames for question/score/navigation and permanent subframes
    global score_frame
    score_frame = Frame(master, width=180, height=730, bg='white')
    score_frame.pack_propagate(False)
    score_frame.place(x=10, y=60)
    global nav_frame
    nav_frame = Frame(master, width=180, height=730, bg='white')
    nav_frame.pack_propagate(False)
    nav_frame.place(x=1110, y=60)
    global feedback_frame
    feedback_frame = Frame(nav_frame, width=180, height=50, bg='gray75')
    feedback_frame.pack_propagate(False)
    feedback_frame.pack(side='top')
    global question_frame
    question_frame = Frame(master, width=900, height=730, bg='white')
    question_frame.pack_propagate(False)
    question_frame.place(x=200, y=60)
    global q_images
    q_images = Frame(question_frame, width=900, height=340, bg='gray75')
    q_images.pack_propagate(False)
    q_images.place(x=0, y=0)
    global q_statement
    q_statement = Frame(question_frame, width=900, height=140, bg='gray75')
    q_statement.pack_propagate(False)
    q_statement.place(x=0, y=350)
    global q_answer
    q_answer = Frame(question_frame, width=900, height=230, bg='gray75')
    q_answer.pack_propagate(False)
    q_answer.place(x=0, y=500)
# Document chosen problem types and run quiz
    if vadd.get() == 1:
        q_type_list.append('vadd')
        mastery_list.append(False)
        score_list.append(0)
    if vsub.get() == 1:
        q_type_list.append('vsub')
        mastery_list.append(False)
        score_list.append(0)
    for type in q_type_list:
        score_label = Label(score_frame, text='\n'+type_dict[type], font='verdana 16')
        score_label.pack(side='top')
        global score_canvas
        score_canvas = Canvas(score_frame, width=180, height=75, bg='red')
        score_canvas.pack(side='top')        
        scorecard_list.append(score_canvas)
        for i in range(0,max_score.get()):
            blank_score_box = score_canvas.create_rectangle(i*180/max_score.get(),0,(i+1)*180/max_score.get(),80, fill='gray50', outline='black')
    run_quiz()

### NEXT FUNCTION ###
def next_question():
    for widget in feedback_frame.winfo_children():
        widget.destroy()
    next.destroy()
    if all(mastery_list):
        score_frame.destroy()
        question_frame.destroy()
        nav_frame.destroy()
        victory_frame = Frame(master, bg='white', highlightthickness=5, highlightbackground='gray20')
        victory_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        victory_label = Label(victory_frame, text='You have mastered all problem types!', font='trebuchet 24 bold', padx=10, pady=10)
        victory_label.grid(row=1)
        quit_button = Button(victory_frame, text='Quit Program', command=quit, padx=10, pady=10)
        quit_button.grid(row=2)
    else:
        run_quiz()

### SUBMIT FUNCTION ### Grades answer, assigns score, kills submit button, makes next question button
def submit_answer():
    submit.destroy()
    global feedback_frame
    for item in error_list:
        item.destroy()
    try:
        float(resp_1.get())
        float(resp_2.get())
    except:
        print('You didn\'t enter an integer you twat.')
        fb_text = 'ERROR'
        fb_color = 'yellow'
        error_label = Label(nav_frame, text='You must enter a number for your submission to be graded', font='verdana 18', fg='black', bg='yellow', highlightthickness=5, highlightbackground='gray20', wraplength=180, justify=LEFT, height=5)
        error_label.pack(side='bottom', fill=X)
        error_list.append(error_label)
        error_submit = Button(nav_frame, text='Submit Answer', command=submit_answer)
        error_submit.pack(side=TOP)
        error_list.append(error_submit)
        resp_1.delete(first=0, last=100)
        resp_2.delete(first=0, last=100)
        feedback_label = Label(feedback_frame, text=fb_text, font='trebuchet 20 bold', fg='black', bg=fb_color, highlightthickness=5, highlightbackground='gray20')
        feedback_label.pack(expand=YES, fill=BOTH)
        error_list.append(feedback_label)
        return        
    resp1.set(resp_1.get())
    resp2.set(resp_2.get())
# Checking submission against correct answer
#    if type(resp1.get()) != float:
#        print('Response 1 error')
    if resp1.get() == answer1.get() and resp2.get() == answer2.get():
        score_list[type_count.get()] += 1
        fb_text = 'Correct'
        fb_color = 'green'
        scorecard_list[type_count.get()].create_rectangle((score_list[type_count.get()]-1)*180/max_score.get(),0,(score_list[type_count.get()])*180/max_score.get(),80, fill='green')
    else:
        score_list[type_count.get()] = 0
        fb_text = 'Wrong'
        fb_color = 'red'
        for i in range(0,max_score.get()):
            scorecard_list[type_count.get()].create_rectangle(i*180/max_score.get(),0,(i+1)*180/max_score.get(),80, fill='gray50', outline='black')
    ### Update score canvas somehow
    print('Scores '+str(score_list))
    if score_list[type_count.get()] == max_score.get():
        mastery_list[type_count.get()] = True
        print('You have passed '+type_dict[q_type_list[type_count.get()]]+'!!! Congratulations!')
# Generate feedback banner
    feedback_label = Label(feedback_frame, text=fb_text, font='trebuchet 20 bold', fg='black', bg=fb_color, highlightthickness=5, highlightbackground='gray20')
    feedback_label.pack(expand=YES, fill=BOTH)
    global next
    if all(mastery_list):
        next_text = 'Finish Quiz'
    else:
        next_text = 'Next Question'
    next = Button(nav_frame, text=next_text, command=next_question)
    next.pack(side=TOP)

#    print(mastery_list)

### GENERATE PROBLEM FUNCTION ###
def generate(str):
# Destroy previous content of question subframes and create submit button
    for widget in q_images.winfo_children():
        widget.destroy()
    for widget in q_statement.winfo_children():
        widget.destroy()
    for widget in q_answer.winfo_children():
        widget.destroy()
    answer1.set(None)
    answer2.set(None)
    global submit
    global resp_1
    global resp_2
    submit = Button(nav_frame, text='Submit Answer', command=submit_answer)
    submit.pack(side=TOP)
# Instructions specific to problem type
    if str == 'vadd':
#        print('Create a Vector Addition Problem')
        Label(q_images, text='Vector Addition Images', fg='red', bg='black').pack()
        state_text = 'This is a fucking vector addition problem. The correct answer is 2 3.'
        answer1.set(2)
        answer2.set(3)
        text1 = Label(q_answer, text='Enter your answer.', wraplength=800, font=('verdana', 20), justify=LEFT)
        text1.pack(side=TOP, expand=YES, fill=BOTH)
        resp_1 = Entry(q_answer, width=3)
        resp_1.pack(side=TOP)
        resp_2 = Entry(q_answer, width=3)
        resp_2.pack(side=TOP)
    if str == 'vsub':
#        print('Create a Vector Subtraction Problem')
        Label(q_images, text='Vector Subtraction Images', fg='purple', bg='yellow', font='times').pack()
        state_text = 'You don\'t even fucking know, dude. Now it\'s time for a vector subtraction problem. You whore. The correct answer is 3 4'
        answer1.set(3)
        answer2.set(4)
        text1 = Label(q_answer, text='No seriously, enter your answer.', wraplength=800, font=('verdana', 20), justify=LEFT)
        text1.pack(side=TOP, expand=YES, fill=BOTH)
        resp_1 = Entry(q_answer, width=3)
        resp_1.pack(side=TOP)
        resp_2 = Entry(q_answer, width=3)
        resp_2.pack(side=TOP)
# Things general to all problems
    statement = Label(q_statement, text=state_text, wraplength=900, font=('verdana',20), justify=LEFT)
    statement.pack(expand=YES, fill=BOTH)

### CHOOSING PROBLEM TYPES ###
# Create problem type selection window
q_type_frame = Frame(master, bg='white', highlightthickness=5, highlightbackground='gray20')
q_type_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
q_type_label = Label(q_type_frame, text='Choose your problem types', font='trebuchet 16 underline', padx=10).grid(row=0)
# Defining variables, names, and checkbuttons for each type
vadd = IntVar()
vsub = IntVar()
type_dict = {'vadd':'Vector Addition', 'vsub':'Vector Subtraction'}
Checkbutton(q_type_frame, text=type_dict['vadd'], variable=vadd).grid(row=1, sticky=W)
Checkbutton(q_type_frame, text=type_dict['vsub'], variable=vsub).grid(row=2, sticky=W)
Button(q_type_frame, text='Start Quiz', command=make_quiz).grid(row=3)

### CYCLE THROUGH PROBLEM TYPES ###
type_count = IntVar()
type_count.set(-1)
def run_quiz():
    type_count.set(type_count.get() + 1)
    if type_count.get() == len(q_type_list):
        type_count.set(0)
    if mastery_list[type_count.get()] == True:
        run_quiz()
    else:
        generate(q_type_list[type_count.get()])

master.mainloop()
