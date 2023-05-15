from tkinter import*
root = Tk()
root.geometry('800x400') 
root.title("General knowledge quiz")

global score
score = 0

def q1():
    #make all the variables global so they can be carried across functions
    global question_1, opt_1, opt_2, opt_3, opt_4, next_1,score

    #make the question label
    question_1 = Label(root, text = 'From base to peak which is the tallest?', font = ('Arial', 40))
    question_1.pack()
    
    #create options for question 1
    opt_1 = Radiobutton(root, text = 'Burj Khalifa', value =1, font = ('Arial', 30))
    opt_2 = Radiobutton(root, text = 'Mauna Kea', value =2, font = ('Arial', 30))
    opt_3 = Radiobutton(root, text = 'Mt. Everest', value =3, font = ('Arial', 30))
    opt_4 = Radiobutton(root, text = 'K2', value =4, font = ('Arial', 30))
    
    #position the radio buttons
    opt_1.pack(padx=10, pady=10)
    opt_2.pack(padx=10, pady=10)
    opt_3.pack(padx=10, pady=10)
    opt_4.pack(padx=10, pady=10)

    #make the button to submit and move onto next question
    next_1 = Button(root, text = 'Next', command = q2)
    next_1.pack()
    
    #check to see if the user has selected the correct option
    if opt_2.get() == 2:
        score += 1
    

def q2():

    #remove previous question
    question_1.pack_forget()
    opt_1.pack_forget()
    opt_2.pack_forget()
    opt_3.pack_forget()
    opt_4.pack_forget()
    next_1.pack_forget()

    #make variables global so they can be accessed across functions
    global question_2, opt_5, opt_6, opt_7, opt_8, next_2, score
    
    #make the question label
    question_2 = Label(root, text = 'Who wrote to kill a Mockingbird?', font = ('Arial', 30))
    question_2.pack()

    #make the options for the quiz
    opt_5 = Radiobutton(root, text = 'Harper Lee', value = 5, font = ('Arial', 30))
    opt_6 = Radiobutton(root, text = 'J.K Rowling', value = 6, font = ('Arial', 30))
    opt_7 = Radiobutton(root, text = 'Charles Dickens', value = 7, font = ('Arial', 30))
    opt_8 = Radiobutton(root, text = 'Rick Riordan', value = 8, font = ('Arial', 30))

    #format the options
    opt_5.pack(padx=10, pady=10)
    opt_6.pack(padx=10, pady=10)
    opt_7.pack(padx=10, pady=10)
    opt_8.pack(padx=10, pady=10)

    #create the button label
    next_2 = Button(root, text = 'Next', command = q3)
    next_2.pack()

    #check to see if the user selected the correct option
    if opt_5.get()== 5:
        score += 1

    
def q3():
    #forget the previous question
    question_2.pack_forget()
    opt_5.pack_forget()
    opt_6.pack_forget()
    opt_7.pack_forget()
    opt_8.pack_forget()
    next_2.pack_forget()

    #make all variables global so they can be reached in other functions
    global question_3,opt_9, opt_10, opt_11, opt_12, next_3, score

    #make the question label
    question_3 = Label(root, text = 'What is the smallest country in the world by land area?', font = ('Arial', 30))
    question_3.pack()

    #create the options for the question
    opt_9 = Radiobutton(root, text = 'Monaco', value = 9, font = ('Arial', 30))
    opt_10 = Radiobutton(root, text = 'Vatican City', value = 10, font = ('Arial', 30))
    opt_11 = Radiobutton(root, text = 'San Marino', value = 11, font = ('Arial', 30))
    opt_12 = Radiobutton(root, text = 'Liechtenstein', value = 12, font = ('Arial', 30))
    
    #format the options
    opt_9.pack(padx=10, pady=10)
    opt_10.pack(padx=10, pady=10)
    opt_11.pack(padx=10, pady=10)
    opt_12.pack(padx=10, pady=10)

    #make the next button to continue the quiz
    next_3 = Button(root, text = 'Next', command=q4)
    next_3.pack()

    #check to see if the correct answer is selected
    if opt_10.get()==10:
        score += 1
    
def q4():
    #forget the previous question
    question_3.pack_forget()
    opt_9.pack_forget()
    opt_10.pack_forget()
    opt_11.pack_forget()
    opt_12.pack_forget()
    next_3.pack_forget()

    #make variables global so they can be reached across functions
    global question_4, opt_13, opt_14, opt_15, opt_16, next_4, score
    
    #make the question label
    question_4 = Label(root, text = 'Who discovered Penicillin?', font = ('Arial', 30))
    question_4.pack()

    #make the options for each question
    opt_13 = Radiobutton(root, text = 'Louis Pasteur', value = 13, font = ('Arial', 30))
    opt_14 = Radiobutton(root, text = 'Robert Koch', value = 14, font = ('Arial', 30))
    opt_15 = Radiobutton(root, text = 'Alexander fleming', value = 15, font = ('Arial', 30))
    opt_16 = Radiobutton(root, text = 'Meliton Soriano', value = 16, font = ('Arial', 30))

    #format the options
    opt_13.pack(padx=10, pady=10)
    opt_14.pack(padx=10, pady=10)
    opt_15.pack(padx=10, pady=10)
    opt_16.pack(padx=10, pady=10)

    #make the button to move onto next question
    next_4 = Button(root, text = 'Next', command=q5)
    next_4.pack()

    #check to see if the correct answer is selected
    if opt_15.get()==15:
        score += 1
        
def q5():
    #forget the previous question
    question_4.pack_forget()
    opt_13.pack_forget()
    opt_14.pack_forget()
    opt_15.pack_forget()
    opt_16.pack_forget()
    next_4.pack_forget()

    #make all the variables global so they can be carried across functions
    global question_5, opt_17, opt_18, opt_19, opt_20, next_5, score

    #create the question label
    question_5 = Label(root, text = 'Who painted the Mona Lisa?', font = ('Arial', 30))
    question_5.pack()

    #create the question options
    opt_17 = Radiobutton(root, text = 'Pablo Picasso', value = 17, font = ('Arial', 30))
    opt_18 = Radiobutton(root, text = 'Vincent Van Gogh', value = 18, font = ('Arial', 30))
    opt_19 = Radiobutton(root, text = 'Leonardo davinci', value = 19, font = ('Arial', 30))
    opt_20 = Radiobutton(root, text = 'Michaelangelo', value = 20, font = ('Arial', 30))

    #format the question
    opt_17.pack(padx=10, pady=10)
    opt_18.pack(padx=10, pady=10)
    opt_19.pack(padx=10, pady=10)
    opt_20.pack(padx=10, pady=10)

    #create the button to move onto next question
    next_5 = Button(root, text = 'Next', command=q6)
    next_5.pack()

    #check to see if the correct answer is selected
    if opt_19.get()==19:
        score += 1
        
def q6():
    #forget the previous question
    question_5.pack_forget()
    opt_17.pack_forget()
    opt_18.pack_forget()
    opt_19.pack_forget()
    opt_20.pack_forget()
    next_5.pack_forget()

    #make all the variables global so they can be carried across functions
    global question_6, opt_21, opt_22, opt_23, opt_24, next_6, score

    #create question label
    question_6 = Label(root, text = 'What is the largest human organ?', font = ('Arial', 30))
    question_6.pack()

    #create options for the queston
    opt_21 = Radiobutton(root, text = 'Heart', value = 21, font = ('Arial', 30))
    opt_22 = Radiobutton(root, text = 'Brain', value = 22, font = ('Arial', 30))
    opt_23 = Radiobutton(root, text = 'Liver', value = 23, font = ('Arial', 30))
    opt_24 = Radiobutton(root, text = 'Skin', value = 24, font = ('Arial', 30))

    #format options
    opt_21.pack(padx=10, pady=10)
    opt_22.pack(padx=10, pady=10)
    opt_23.pack(padx=10, pady=10)
    opt_24.pack(padx=10, pady=10)

    #create button to move onto next question
    next_6 = Button(root, text = 'Next', command= q7)
    next_6.pack()

    #check to see if the correct answer is selected
    if opt_24.get()==24:
        score += 1
        
def q7():
    #forget the previous question
    question_6.pack_forget()
    opt_21.pack_forget()
    opt_22.pack_forget()
    opt_23.pack_forget()
    opt_24.pack_forget()
    next_6.pack_forget()
    
    #make all the variables global so they can be carried across functions
    global question_7, opt_25, opt_26, opt_27, opt_28, next_7, score
    
    #make the question label
    question_7 = Label(root, text = 'A tetradecahedron has how many faces?', font = ('Arial', 30))
    question_7.pack()

    #create the options for the question
    opt_25 = Radiobutton(root, text = '13', value = 25, font = ('Arial', 30))
    opt_26 = Radiobutton(root, text = '14', value = 26, font = ('Arial', 30))
    opt_27 = Radiobutton(root, text = '23', value = 27, font = ('Arial', 30))
    opt_28 = Radiobutton(root, text = '24', value = 28, font = ('Arial', 30))

    #format the options
    opt_25.pack(padx=10, pady=10)
    opt_26.pack(padx=10, pady=10)
    opt_27.pack(padx=10, pady=10)
    opt_28.pack(padx=10, pady=10)

    #create button to move onto next question
    next_7 = Button(root, text = 'Next', command=q8)
    next_7.pack()
    
    #check to see if the correct answer is selected
    if opt_26.get()==26:
        score += 1
    
def q8():
    #forget the previous question
    question_7.pack_forget()
    opt_25.pack_forget()
    opt_26.pack_forget()
    opt_27.pack_forget()
    opt_28.pack_forget()
    next_7.pack_forget()
    
    #make all the variables global so they can be carried across functions
    global question_8, opt_29, opt_30, opt_31, opt_32
    
    #make the question label
    question_8 = Label(root, text = 'Which one of these animals lays eggs', font = ('Arial', 30))
    question_8.pack()

    #make the options for the question
    opt_29= Radiobutton(root, text = 'Platypus', value = 29, font = ('Arial', 30))
    opt_30 = Radiobutton(root, text = 'Lion', value = 30, font = ('Arial', 30))
    opt_31 = Radiobutton(root, text = 'Porcupine', value = 31, font = ('Arial', 30))
    opt_32 = Radiobutton(root, text = 'Hedgehog', value = 32, font = ('Arial', 30))
    
    #format the options
    opt_29.pack(padx=10, pady=10)
    opt_30.pack(padx=10, pady=10)
    opt_31.pack(padx=10, pady=10)
    opt_32.pack(padx=10, pady=10)

    #make the 'next' button to move onto next question
    next_8 = Button(root, text = 'Next', command=q9)
    next_8.pack()

    #check to see if the correct answer is selected
    global score
    if opt_29.get()==29:
        score += 1
    
def q9():
    #forget the previous question
    question_8.pack_forget()
    opt_29.pack_forget()
    opt_30.pack_forget()
    opt_31.pack_forget()
    opt_32.pack_forget()
    next_8.pack_forget()

    #make all the variables global so they can be carried across functions
    global question_9, opt_33, opt_34, opt_35, opt_36, next_9, score
    
    #make the question label
    question_9 = Label(root, text = 'What does NDL stand for?', font = ('Arial', 35))
    question_9.pack()
    
    #make the options for the question
    opt_33 = Radiobutton(root, text = 'National Democratic Leaders', value = 33, font = ('Arial', 30))
    opt_34 = Radiobutton(root, text = 'Nice Dancing Linguini', value = 34, font = ('Arial', 30))
    opt_35 = Radiobutton(root, text = 'Niko Defense League', value = 35, font = ('Arial', 30))
    opt_36 = Radiobutton(root, text = 'Non Distinct Linguistics', value = 36, font = ('Arial', 30))
    
    #format the options for the quiz.
    opt_33.pack(padx=10, pady=10)
    opt_34.pack(padx=10, pady=10)
    opt_35.pack(padx=10, pady=10)
    opt_36.pack(padx=10, pady=10)

    #create the next button so next question appears
    next_9 = Button(root, text = 'Next', command=q10)
    next_9.pack()

    #check to see if the correct answer is selected
    if opt_35.get() == 35:
        score += 1
        
def q10():
    #forget the previous question
    question_9.pack_forget()
    opt_33.pack_forget()
    opt_34.pack_forget()
    opt_35.pack_forget()
    opt_36.pack_forget()
    next_9.pack_forget()

    #make all the variables global so they can be carried across functions
    global question_10, opt_37, opt_38, opt_39, opt_40, next_10, score
    #make the question label
    question_10 = Label(root, text = 'What is the functional group of a carboxylic acid?', font = ('Arial', 30))
    question_10.pack()

    #create the options for the question
    opt_37 = Radiobutton(root, text = 'C-H', value = 37, font = ('Arial', 30))
    opt_38 = Radiobutton(root, text = '-OH', value = 38, font = ('Arial', 30))
    opt_39 = Radiobutton(root, text = '-OOH', value = 39, font = ('Arial', 30))
    opt_40 = Radiobutton(root, text = 'C-NH3', value = 40, font = ('Arial', 30))

    #format the options
    opt_37.pack(padx=10, pady=10)
    opt_38.pack(padx=10, pady=10)
    opt_39.pack(padx=10, pady=10)
    opt_40.pack(padx=10, pady=10)

    #create button to finish quiz
    next_10 = Button(root, text = 'Finish', command = results)
    next_10.pack()

    #check to see if the correct answer is selected
    if opt_39.get()==39:
        score += 1
    
def results():
    #forget the previous question
    question_10.pack_forget()
    opt_37.pack_forget()
    opt_38.pack_forget()
    opt_39.pack_forget()
    opt_40.pack_forget()
    next_10.pack_forget()

    #print out the final score
    global score
    result = Label(root, text = score)
    result.pack()
    


#run code
q1()


root.mainloop()

