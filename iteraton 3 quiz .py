
#import random library

import random

#make question variables
# put them in triple quotes so they will appear on multiple lines
Q1 = """From base to peak which is the tallest? 
a) Burj Khalifa
b) Mauna Kea
c) Mt.Everest
d) K2 """

Q2= """Who wrote 'To Kill a Mockingbird'?
a) Harper lee
b) J.K Rowling
c) Charles Dickens
d) F. Scott Fitzgerald"""

Q3= """What is the smallest country in the world by land area?
a) Monaco
b) Vatican City
c) San Marino
d) Liechtenstein"""

Q4= """Who discovered Penicillin?
a) Louis Pasteur
b) Robert Koch
c) Alexander Fleming
d) Meliton Soriano
"""

Q5= """Who painted the Mona Lisa?
a) Pablo Picasso
b) Vincent Van Gogh
c) Leonardo Davinci
d) Michaelangelo"""



Q6= """What is the largest human organ?
a) Heart
b) Brain
c) Liver
d) Skin"""



Q7= """A tetradecahedron has how many faces?
a) 13
b) 14
c) 23
d) 24"""


Q8= """Which one of these animals lays eggs?
a) Platypus
b) Lion
c) Porcupine
d) Hedgehog"""



Q9= """What does NDL stand for?
a) National Democratic Leaders
b) Nice Dancing Linguini
c) Niko Defense League
d) Non Distinct Linguistics"""



Q10= """What is the functional group of a carboxylic acid?
a) C-H
b) -OH
c) -OOH
d) C-NH3"""


#create a dictonary with all questions and asign the correct answer to all of them
questions = {Q1:"b" , Q2:"a", Q3:"b" , Q4:"c" , Q5:"c" , Q6:"d", Q7:"b", Q8:"a", Q9:"c", Q10:"c"}

#randomise quesitons


#create an empty guesses list
guesses = []

#create an empty correct answers list
correct_answers = []

#run main routine
#introduce user to the quiz
name = input("What is your name? ")
print("Welcome, {}" .format(name))
print("This is a multiple choice quiz, answer with either a, b, c, or d")

#make the score variable and set to 0
score = 0


#valid answers list
valid_answers = ["a","b", "c","d"]

#set play again to true:
play_again = True

#iter each question in the following way
while play_again == True:
    attempted = 10
    try_again = 0 
    random_questions = list(questions.items())
    random.shuffle(random_questions)
    shuffled_questions = dict(random_questions)
    for question in shuffled_questions:
        print("----------------------------------")
        print(question)
        
        
        #create skip question feature
        skip_question = input("type 'yes' to skip and any other key to continue: ").lower()
        
        if skip_question=="yes":
            attempted -= 1
            print("QUESTION SKIPPED!")
            continue
        
        answer = input("ANSWER : ").lower()
        
        #check if answer is valid
        while answer not in valid_answers:
            print("INVALID!!!!!!!")
            print("please answer with a,b,c,d ")
            answer = input("ANSWER: ").lower()
        #check valid answer       
        if answer in valid_answers:
            correct_answers.append(shuffled_questions[question]) #puts the actual answer into the correct_answers list
            if answer==shuffled_questions[question]:
                print("CORRECT!")
                score += 1
                guesses.append(answer)
            else:
                print("INCORRECT")
                guesses.append(answer)
        else:
            print("make sure to answer with a,b,c, or d")

  #execute final steps of the programme, answers, guesses, play again, and score          
    print("")        
    print(', '.join(correct_answers), ":correct answers:")
    print(', '.join(guesses), ":your guesses:")
    print(f"\n{score}/{attempted}" )

    while try_again == 0: #error handling for value error
         try:
             retry = int(input("\nPress 1 if you want to play again or press 2 to exit: "))
             if retry == 1:
                 play_again = True
                 score = 0
                 attempted = 0
                 guesses.clear()
                 correct_answers.clear()
                 try_again += 1 #breaks the try and except loop 
             elif retry == 2:
                 print("thank you for playing!")
                 play_again = False #ends the whole while loop
                 try_again += 1 # breaks the try and except while loop
                 
             else:
                print("the only valid inputs are 1 or 2")
         except ValueError:
            print("Enter either 1 or 2")
    
