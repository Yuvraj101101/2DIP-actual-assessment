from tkinter import*

#configure the gui frame base
root = Tk()
root.geometry('800x400') 
root.title("General knowledge quiz")
root.config(bg= '#8fd2ff')

#make the scores list to carry all the previous scores before the application is quit
scores = []

#define score variable
global score
score = 0

#make reset score function for restart()
def reset_score():
    global score
    score = 0
def restart():
    reset_score() 
    



#check answer function
def call(par,value):
    if par == value:
        global score, label
        label = Label(root, text = 'CORRECT!!!', bg = '#8fd2ff',fg = '#05fc21', font=('Arial',24,'bold'))
        label.pack(padx = 10, pady = 10)
        score +=1
    else:
        label = Label(root, text = "INCORRECT!!!", bg = '#8fd2ff', fg = 'red', font=('Arial',24,'italic','bold'))
        score += 0
        label.pack(padx = 10, pady = 10)
    
    

def q1():
    #set score to 0 in the beginning
    restart()
    #make all the variables global so they can be carried across functions
    global correct,label

    
    correct = IntVar()

    #make the question label
    question_1 = Label(root, text = 'From base to peak which is the tallest?',width = 800 ,font = ('Arial', 40,'italic','underline','bold'),bg='#f5c43d')
    question_1.pack()
    
    
    #create options for question 1
    opt_1 = Radiobutton(root, text = 'Burj Khalifa',variable = correct, value = 1, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_2 = Radiobutton(root, text = 'Mauna Kea', variable = correct,value = 2, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_3 = Radiobutton(root, text = 'Mt. Everest',variable = correct, value = 3, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_4 = Radiobutton(root, text = 'K2',variable = correct, value = 4, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    
    #position the radio buttons
    opt_1.pack(padx=40, pady=10)
    opt_2.pack(padx=10, pady=10)
    opt_3.pack(padx=10, pady=10)
    opt_4.pack(padx=10, pady=10)

   

    #check to see if the user has selected the correct option
    submit_1 = Button(root,text='Submit',highlightbackground='#8fd2ff', command = lambda: [next_1.pack(),call(correct.get(),2),submit_1.pack_forget(),skip_1.pack_forget()])
    submit_1.pack()
    
    #make the button to submit and move onto next question
    #when pressed the elements in this function dissapear and the next question appears.
    next_1 = Button(root, text='Next',highlightbackground='#8fd2ff', command= lambda: [q2(),question_1.pack_forget(),opt_1.pack_forget(),opt_2.pack_forget(),opt_3.pack_forget(),opt_4.pack_forget(),next_1.pack_forget(),label.pack_forget(),skip_1.pack_forget()])

    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_1 = Button(root, text = 'skip' ,highlightbackground='#8fd2ff',command = lambda: [submit_1.pack_forget(),q2(),question_1.pack_forget(),opt_1.pack_forget(),opt_2.pack_forget(),opt_3.pack_forget(),opt_4.pack_forget(),next_1.pack_forget(),skip_1.pack_forget()])
    skip_1.pack()
    

def q2():

   
    
    
    #make the question label
    question_2 = Label(root, text = 'Who wrote to kill a Mockingbird?',width = 800, font = ('Arial', 50,'italic','underline','bold'),bg='#f5c43d')
    question_2.pack()

    #make the options for the quiz
    opt_5 = Radiobutton(root, text = 'Harper Lee',variable = correct, value = 5, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_6 = Radiobutton(root, text = 'J.K Rowling',variable = correct, value = 6, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_7 = Radiobutton(root, text = 'Charles Dickens',variable = correct, value = 7, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_8 = Radiobutton(root, text = 'Rick Riordan',variable = correct, value = 8, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')

    #format the options
    opt_5.pack(padx=10, pady=10)
    opt_6.pack(padx=10, pady=10)
    opt_7.pack(padx=10, pady=10)
    opt_8.pack(padx=10, pady=10)

    #check to see if the user selected the correct option   
    submit_2 = Button(root, highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_2.pack(),call(correct.get(),5),submit_2.pack_forget(),skip_2.pack_forget()])
    submit_2.pack()


    #create the button label
    next_2 = Button(root,highlightbackground='#8fd2ff', text = 'Next', command = lambda: [q3(),question_2.pack_forget(),opt_5.pack_forget(),opt_6.pack_forget(),opt_7.pack_forget(),opt_8.pack_forget(),next_2.pack_forget(),label.pack_forget()])
    
    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_2 = Button(root,highlightbackground='#8fd2ff', text = 'skip',command = lambda: [submit_2.pack_forget(),q3(),question_2.pack_forget(),opt_5.pack_forget(),opt_6.pack_forget(),opt_7.pack_forget(),opt_8.pack_forget(),next_2.pack_forget(),skip_2.pack_forget()])
    skip_2.pack()

    
    
def q3():

    #make all variables global so they can be reached in other functions
    global question_3,opt_9, opt_10, opt_11, opt_12, next_3, score, submit_3

    #make the question label
    question_3 = Label(root, text = 'What is the smallest country in the world by land area?',width = 800, font = ('Arial', 30,'italic','underline','bold'), bg='#f5c43d')
    question_3.pack()

    #create the options for the question
    opt_9 = Radiobutton(root,text = 'Monaco',variable = correct, value = 9, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_10 = Radiobutton(root,text = 'Vatican City',variable = correct, value = 10, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_11 = Radiobutton(root,text = 'San Marino',variable = correct, value = 11, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_12 = Radiobutton(root,text = 'Liechtenstein',variable = correct, value = 12, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    
    #format the options
    opt_9.pack(padx=10, pady=10)
    opt_10.pack(padx=10, pady=10)
    opt_11.pack(padx=10, pady=10)
    opt_12.pack(padx=10, pady=10)

    #check to see if the correct answer is selected   
    submit_3 = Button(root,highlightbackground='#8fd2ff', text='Submit', command = lambda: [next_3.pack(),call(correct.get(),10),submit_3.pack_forget(),skip_3.pack_forget()])
    submit_3.pack()

    #make the next button to continue the quiz
    next_3 = Button(root,highlightbackground='#8fd2ff', text = 'Next', command= lambda :[q4(),question_3.pack_forget(),opt_9.pack_forget(),opt_10.pack_forget(),opt_11.pack_forget(),opt_12.pack_forget(),next_3.pack_forget(),label.pack_forget()])
    
    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_3 = Button(root,highlightbackground='#8fd2ff', text = 'skip',command = lambda: [submit_3.pack_forget(),q4(),question_3.pack_forget(),opt_9.pack_forget(),opt_10.pack_forget(),opt_11.pack_forget(),opt_12.pack_forget(),next_3.pack_forget(),skip_3.pack_forget()])
    skip_3.pack()

    
    
def q4():

    #make variables global so they can be reached across functions
    global question_4, opt_13, opt_14, opt_15, opt_16, next_4, score, submit_4
    
    #make the question label
    question_4 = Label(root, text = 'Who discovered Penicillin?', width = 800, font = ('Arial', 50,'italic','underline','bold'),bg='#f5c43d')
    question_4.pack()

    #make the options for each question
    opt_13 = Radiobutton(root, text = 'Louis Pasteur',variable = correct, value = 13, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_14 = Radiobutton(root, text = 'Robert Koch',variable = correct, value = 14, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_15 = Radiobutton(root, text = 'Alexander fleming',variable = correct, value = 15, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_16 = Radiobutton(root, text = 'Meliton Soriano',variable = correct, value = 16, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')

    #format the options
    opt_13.pack(padx=10, pady=10)
    opt_14.pack(padx=10, pady=10)
    opt_15.pack(padx=10, pady=10)
    opt_16.pack(padx=10, pady=10)

    #check to see if the correct answer is selected    
    submit_4 = Button(root, highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_4.pack(),call(correct.get(),15),submit_4.pack_forget(),skip_4.pack_forget()])
    submit_4.pack()

    #make the button to move onto next question
    next_4 = Button(root, highlightbackground='#8fd2ff',text = 'Next', command=lambda:[q5(),question_4.pack_forget(),opt_13.pack_forget(),opt_14.pack_forget(),opt_15.pack_forget(),opt_16.pack_forget(),next_4.pack_forget(),label.pack_forget()])

    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_4 = Button(root, highlightbackground='#8fd2ff',text = 'skip',command = lambda: [submit_4.pack_forget(),q5(),question_4.pack_forget(),opt_13.pack_forget(),opt_14.pack_forget(),opt_15.pack_forget(),opt_16.pack_forget(),next_4.pack_forget(),skip_4.pack_forget()])
    skip_4.pack()

    
        
def q5():

    #make all the variables global so they can be carried across functions
    global question_5, opt_17, opt_18, opt_19, opt_20, next_5, score, submit_5

    #create the question label
    question_5 = Label(root, text = 'Who painted the Mona Lisa?',width = 800, font = ('Arial', 50,'italic','underline','bold'),bg='#f5c43d')
    question_5.pack()

    #create the question options
    opt_17 = Radiobutton(root, text = 'Pablo Picasso',variable = correct, value = 17, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_18 = Radiobutton(root,text = 'Vincent Van Gogh',variable = correct, value = 18, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_19 = Radiobutton(root,text = 'Leonardo Davinci',variable = correct, value = 19, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_20 = Radiobutton(root,text = 'Michaelangelo',variable = correct, value = 20, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')

    #format the question
    opt_17.pack(padx=10, pady=10)
    opt_18.pack(padx=10, pady=10)
    opt_19.pack(padx=10, pady=10)
    opt_20.pack(padx=10, pady=10)

    #check to see if the correct answer is selected  
    submit_5 = Button(root, highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_5.pack(),call(correct.get(),19),submit_5.pack_forget(), skip_5.pack_forget()])
    submit_5.pack()

    #create the button to move onto next question
    next_5 = Button(root, highlightbackground='#8fd2ff',text = 'Next', command= lambda:[q6(),question_5.pack_forget(),opt_17.pack_forget(),opt_18.pack_forget(), opt_19.pack_forget(),opt_20.pack_forget(),next_5.pack_forget(),label.pack_forget()])

    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_5 = Button(root, highlightbackground='#8fd2ff',text = 'skip',command = lambda: [submit_5.pack_forget(),q6(),question_5.pack_forget(),opt_17.pack_forget(),opt_18.pack_forget(),opt_19.pack_forget(),opt_20.pack_forget(),next_5.pack_forget(),skip_5.pack_forget()])
    skip_5.pack()


    
        
def q6():


    #create question label
    question_6 = Label(root, text = 'What is the largest human organ?',width = 800, font = ('Arial', 49,'italic','underline','bold'),bg='#f5c43d')
    question_6.pack()

    #create options for the queston
    opt_21 = Radiobutton(root, text = 'Heart',variable = correct, value = 21, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_22 = Radiobutton(root, text = 'Brain',variable = correct, value = 22, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_23 = Radiobutton(root, text = 'Liver',variable = correct, value = 23, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_24 = Radiobutton(root, text = 'Skin',variable = correct, value = 24, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')

    #format options
    opt_21.pack(padx=10, pady=10)
    opt_22.pack(padx=10, pady=10)
    opt_23.pack(padx=10, pady=10)
    opt_24.pack(padx=10, pady=10)

    #check to see if the correct answer is selected
    submit_6 = Button(root, highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_6.pack(),call(correct.get(),24),submit_6.pack_forget(),skip_6.pack_forget()])
    submit_6.pack()

    #create button to move onto next question
    next_6 = Button(root, highlightbackground='#8fd2ff',text = 'Next', command= lambda: [q7(),question_6.pack_forget(),opt_21.pack_forget(),opt_22.pack_forget(),opt_23.pack_forget(),opt_24.pack_forget(),next_6.pack_forget(),label.pack_forget()])

    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_6 = Button(root, highlightbackground='#8fd2ff',text = 'skip',command = lambda: [submit_6.pack_forget(),q7(),question_6.pack_forget(),opt_21.pack_forget(),opt_22.pack_forget(),opt_23.pack_forget(),opt_24.pack_forget(),next_6.pack_forget(),skip_6.pack_forget()])
    skip_6.pack()

        
def q7():
    
    
    #make the question label
    question_7 = Label(root, text = 'A tetradecahedron has how many faces?',width = 800, font = ('Arial', 40,'italic','underline','bold'),bg='#f5c43d')
    question_7.pack()

    #create the options for the question
    opt_25 = Radiobutton(root, text = '13',variable = correct, value = 25, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_26 = Radiobutton(root, text = '14',variable = correct, value = 26, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_27 = Radiobutton(root, text = '23',variable = correct, value = 27, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_28 = Radiobutton(root, text = '24',variable = correct, value = 28, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')

    #format the options
    opt_25.pack(padx=10, pady=10)
    opt_26.pack(padx=10, pady=10)
    opt_27.pack(padx=10, pady=10)
    opt_28.pack(padx=10, pady=10)

    #check to see if the correct answer is selected
    submit_7 = Button(root, highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_7.pack(),call(correct.get(),26),submit_7.pack_forget(),skip_7.pack_forget()])
    submit_7.pack()

    #create button to move onto next question
    next_7 = Button(root, highlightbackground='#8fd2ff',text = 'Next', command= lambda: [q8(),question_7.pack_forget(),opt_25.pack_forget(),opt_26.pack_forget(),opt_27.pack_forget(),opt_28.pack_forget(),next_7.pack_forget(),label.pack_forget()])

    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_7 = Button(root, highlightbackground='#8fd2ff',text = 'skip',command = lambda: [submit_7.pack_forget(),q8(),question_7.pack_forget(),opt_25.pack_forget(),opt_26.pack_forget(),opt_27.pack_forget(),opt_28.pack_forget(),next_7.pack_forget(),skip_7.pack_forget()])
    skip_7.pack()

        
    
def q8():
    
    #make the question label
    question_8 = Label(root, text = 'Which one of these animals lays eggs',width = 800, font = ('Arial', 43,'italic','underline','bold'),bg='#f5c43d')
    question_8.pack()

    #make the options for the question
    opt_29= Radiobutton(root, text = 'Platypus',variable = correct, value = 29, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_30 = Radiobutton(root, text = 'Lion',variable = correct, value = 30, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_31 = Radiobutton(root, text = 'Porcupine',variable = correct, value = 31, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_32 = Radiobutton(root, text = 'Hedgehog',variable = correct, value = 32, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    
    #format the options
    opt_29.pack(padx=10, pady=10)
    opt_30.pack(padx=10, pady=10)
    opt_31.pack(padx=10, pady=10)
    opt_32.pack(padx=10, pady=10)

    #check to see if the correct answer is selected
    submit_8 = Button(root, highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_8.pack(),call(correct.get(),29),submit_8.pack_forget(), skip_8.pack_forget()])
    submit_8.pack()

    #make the 'next' button to move onto next question
    next_8 = Button(root, highlightbackground='#8fd2ff',text = 'Next', command= lambda:[q9(),question_8.pack_forget(),opt_29.pack_forget(),opt_30.pack_forget(),opt_31.pack_forget(),opt_32.pack_forget(),next_8.pack_forget(),label.pack_forget()])

    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_8 = Button(root, highlightbackground='#8fd2ff',text = 'skip',command = lambda: [submit_8.pack_forget(),q9(),question_8.pack_forget(),opt_29.pack_forget(),opt_30.pack_forget(),opt_31.pack_forget(),opt_32.pack_forget(),next_8.pack_forget(),skip_8.pack_forget()])
    skip_8.pack()


def q9():

    
    #make the question label
    question_9 = Label(root, text = 'What does NDL stand for?', width = 800,font = ('Arial', 45,'italic','underline','bold'),bg='#f5c43d')
    question_9.pack()
    
    #make the options for the question
    opt_33 = Radiobutton(root, text = 'National Democratic Leaders',variable = correct, value = 33, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_34 = Radiobutton(root, text = 'Nice Dancing Linguini',variable = correct, value = 34, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_35 = Radiobutton(root, text = 'Niko Defense League',variable = correct, value = 35, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_36 = Radiobutton(root, text = 'Non Distinct Linguistics',variable = correct, value = 36, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    
    #format the options for the quiz.
    opt_33.pack(padx=10, pady=10)
    opt_34.pack(padx=10, pady=10)
    opt_35.pack(padx=10, pady=10)
    opt_36.pack(padx=10, pady=10)

    #check to see if the correct answer is selected
    submit_9 = Button(root,highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_9.pack(),call(correct.get(),35),submit_9.pack_forget(),skip_9.pack_forget()])
    submit_9.pack()

    #create the next button so next question appears
    next_9 = Button(root, highlightbackground='#8fd2ff',text = 'Next', command= lambda:[q10(),question_9.pack_forget(), opt_33.pack_forget(),opt_34.pack_forget(),opt_35.pack_forget(),opt_36.pack_forget(),next_9.pack_forget(),submit_9.pack_forget(),label.pack_forget()])
    
    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_9 = Button(root, highlightbackground='#8fd2ff',text = 'skip',command = lambda: [submit_9.pack_forget(),q10(),question_9.pack_forget(),opt_33.pack_forget(),opt_34.pack_forget(),opt_35.pack_forget(),opt_36.pack_forget(),next_9.pack_forget(),skip_9.pack_forget()])
    skip_9.pack()

           
def q10():
    
    #make the question label
    question_10 = Label(root, text = 'What is the functional group of a carboxylic acid?',width = 800, font = ('Arial', 32,'italic','underline','bold'),bg='#f5c43d')
    question_10.pack()

    #create the options for the question
    opt_37 = Radiobutton(root, text = 'C-H',variable = correct, value = 37, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_38 = Radiobutton(root, text = '-OH',variable = correct, value = 38, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_39 = Radiobutton(root, text = '-OOH',variable = correct, value = 39, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')
    opt_40 = Radiobutton(root, text = 'C-NH3',variable = correct, value = 40, font = ('Arial', 30,'bold'),bg = '#8fd2ff',fg = 'black')

    #format the options
    opt_37.pack(padx=10, pady=10)
    opt_38.pack(padx=10, pady=10)
    opt_39.pack(padx=10, pady=10)
    opt_40.pack(padx=10, pady=10)
    
    #check to see if the correct answer is selected
    submit_10 = Button(root, highlightbackground='#8fd2ff',text='Submit', command = lambda: [next_10.pack(),call(correct.get(),39),submit_10.pack_forget(),skip_10.pack_forget()])
    submit_10.pack()

    #create button to finish quiz
    next_10 = Button(root, highlightbackground='#8fd2ff',text = 'Finish', command = lambda: [results(),question_10.pack_forget(),opt_37.pack_forget(),opt_38.pack_forget(),opt_39.pack_forget(),opt_40.pack_forget(),next_10.pack_forget(),label.pack_forget()])  

    #make a button so the user can also skip the question instead if they don't want to answer.
    skip_10 = Button(root, highlightbackground='#8fd2ff',text = 'skip',command = lambda: [submit_10.pack_forget(),results(),question_10.pack_forget(),opt_37.pack_forget(),opt_38.pack_forget(),opt_39.pack_forget(),opt_40.pack_forget(),next_10.pack_forget(),skip_10.pack_forget()])
    skip_10.pack()

def results():
    global score
    #format the items in the scores list
    formatted_scores = ''.join(str(scores))

    #make the final score variable
    final_score = score
    
    #Make the finish label
    finish = Label(root,width=800,bg='#ff7f50', text = f'Your final score was: {score}', font= ('Arial',50, 'bold','underline'))
    finish.pack()
    
    #make the play_again button
    play_again = Button(root,highlightbackground='#8fd2ff', text = 'play again',command = lambda:[view_score.pack_forget(),previous_scores.pack_forget(),q1(),finish.pack_forget(),play_again.pack_forget(),scores.append(final_score)])
    play_again.pack()
    
    #make a view score button
    view_score = Button(root,highlightbackground='#8fd2ff', text = 'previous scores',command = lambda:[previous_scores.pack()])
    view_score.pack(pady=20)

    #make a view score label
    previous_scores = Label(root, text = formatted_scores, font=('Arial',30,'italic','bold'),bg='#8fd2ff')

      
#run the main code
q1()

root.mainloop()

