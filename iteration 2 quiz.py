
#create check answer function
def check_answer(question, answer, incorrect, correct, prompt):
    global score
    valid_answers = ["a","b","c","d"]
    if answer in valid_answers:
        correct_answers.append(correct)#add the actual answer to the correct_answers list
        if answer == correct:
            print("CORRECT!")
            score += 1
            guesses.append(answer) #add the user response into the guesses list
        else:
            print("INCORRECT!")
            guesses.append(answer) #add the user response into the guesses list 
    else:
        print("ANSWER WITH EITHER a,b,c, or d") #error handling for invalid cases
        prompt()
                               
#create the questions functions for the main routine
def prompt_1():
    print("-------------------------------")
    question_1 = print("From base to peak which is the tallest? ")
    print("a) Burj Khalifa ")
    print("b) Mauna Kea")
    print("c) Mt. Everest")
    print("d) K2 ")
    answer_1 = input("ANSWER: ")
    check_answer(question_1, answer_1, ("a","c","d"),"b", prompt_1)
   
    
def prompt_2():
    print("-------------------------------")

    question_2 = print("Who wrote 'To Kill a Mockingbird'? ")
    print("a) Harper lee ")
    print("b) J.K Rowling ")
    print("c) Charles Dickens")
    print("d) F. Scott Fitzgerald")
    answer_2 = input("ANSWER: ")
    check_answer(question_2, answer_2, ("b" ,"c","d"), "a", prompt_2)
   

def prompt_3():
    print("-------------------------------")

    question_3 = print("What is the smallest country in the world by land area? ")
    print("a) Monaco ")
    print("b) Vatican City")
    print("c) San Marino ")
    print("d) Liechtenstein")
    answer_3 = input("ANSWER: ")
    check_answer(question_3, answer_3, ("a","c","d"), "b", prompt_3)
    

def prompt_4():
    print("-------------------------------")

    question_4 = print("Who discovered Penicillin? ")
    print("a) Louis Pasteur")
    print("b) Robert Koch")
    print("c) Alexander Fleming") 
    print("d) Meliton Soriano")
    answer_4 = input("ANSWER: ")
    check_answer(question_4, answer_4, ("a","b","d"), "c", prompt_4)
    
    
def prompt_5():
    print("-------------------------------")

    question_5 = print("Who painted the Mona Lisa? ")
    print("a) Pablo Picasso")
    print("b) Vincent Van Gogh")
    print("c) Leonardo Davinci")
    print("d) Michaelangelo ")
    answer_5 = input("ANSWER: ")
    check_answer(question_5, answer_5, ("a","b","d"), "c", prompt_5)
    
    
def prompt_6():
    print("-------------------------------")

    question_6 = print("What is the largest human organ? ")
    print("a) Heart")
    print("b) Brain ")
    print("c) Liver ")
    print("d) skin ")
    answer_6 = input("ANSWER: ")
    check_answer(question_6, answer_6, ("a", "b", "c"), "d", prompt_6)
    

def prompt_7():
    print("-------------------------------")

    question_7 = print("A tetredecahedron has how many faces? ")
    print("a) 13 ")
    print("b) 14 ")
    print("c) 23 ")
    print("d) 24 ")
    answer_7 = input("ANSWER: ")
    check_answer(question_7, answer_7, ("a","c","d"), "b", prompt_7)
    

def prompt_8():
    print("-------------------------------")

    question_8 = print("Which one of these animals lays eggs? ")
    print("a) Platypus")
    print("b) Lion ")
    print("c) Porcupine ")
    print("d) Hedgehog ")
    answer_8 = input("ANSWER: ")
    check_answer(question_8, answer_8, ("b","c","d"), "a", prompt_8)
    

def prompt_9():
    print("-------------------------------")

    question_9 = print("What does NDL stand for? ")
    print("a) National democratic Leaders ")
    print("b) Nicely Done Loser ")
    print("c) Niko Defense league ")
    print("d) Non distinct linguistics ")
    answer_9 = input("ANSWER: ")
    check_answer(question_9, answer_9, ("a", "b", "d"), "c", prompt_9)
    

def prompt_10():
    print("-------------------------------")

    question_10 = print("What is the functional group of a carboxylic acid? ")
    print("a) C-H ")
    print("b) -OH ")
    print("c) -OOH ")
    print("d) C-NH3 ")
    answer_10 = input("ANSWER: ")
    check_answer(question_10, answer_10, ("a", "b", "d"), "c", prompt_10)
    
    
#run main routine
    
#randomise the order of the questions/prompts so when the user tries again they won't just guess the same order.
import random

#create the list for guesses.
guesses = []


#create list for the correct answers

correct_answers = []


#introduce the users to the quiz
name = input("What is your name? ")
print("Welcome, {}" .format(name))
print("This is a multiple choice quiz, answer with either a, b, c, or d")

print("-------------------------------")
global score #make score global so it can be added across functions
score = 0

play_again = False

while play_again == False:
    questions = [prompt_1,prompt_2,prompt_3,prompt_4,prompt_5,prompt_6,prompt_7,prompt_8,prompt_9,prompt_10]
    random_questions = questions[:]
    random.shuffle(random_questions)
    for questions in random_questions:
       questions() #finishes running the quiz moves onto printing the score, guesses, and if user wants to play again
    print(', '.join(correct_answers), ":correct answers:")
    print(', '.join(guesses), ":your guesses:")
    print("\n{}/10" .format(score))
    try_again = 0 # use this instead of 'while True:' so it is easier to break
    while try_again == 0: #error handling for value error
        try:
            retry = int(input("\nPress 1 if you want to play again or press 2 to exit: "))
            if retry == 1:
                play_again = False
                score = 0
                guesses.clear()
                correct_answers.clear()
                try_again += 1 #breaks the try and except loop 
            elif retry == 2:
                print("thank you for playing!")
                exit() #ends the whole main routine, (exit()) is a built in function
            else:
                ("the only valid inputs are 1 or 2")
        except ValueError:
            print("Enter either 1 or 2")
            
            
            

    











