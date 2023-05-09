#introduce the users to the quiz
name = input("What is your name? ")
print("Welcome, {}" .format(name))
print("This is a multiple choice quiz, answer with either a, b, c, or d")

print("-------------------------------")
#make score global so it can be counted in the function and across questions
global score
score = 0

#create check answer function
def check_answer(question, answer, incorrect, correct):
    global score
    if answer == correct:
        print("correct")
        score += 1
    elif answer in incorrect:
        print("incorrect")
    else:
        print("ANSWER WITH EITHER a,b,c, or d")
       
        
        
#run the main routine
question_1 = print("From base to peak which is the tallest? ")
print("a) Burj Khalifa ")
print("b) Mauna Kea")
print("c) Mt. Everest")
print("d) K2 ")
answer_1 = input("ANSWER: ")
check_answer(question_1, answer_1, ("a","c","d"),"b")

print("-------------------------------")

question_2 = print("Who wrote 'To Kill a Mockingbird'? ")
print("a) Harper lee ")
print("b) J.K Rowling ")
print("c) Charles Dickens")
print("d) F. Scott Fitzgerald")
answer_2 = input("ANSWER: ")
check_answer(question_2, answer_2, ("b" ,"c","d"), "a")

print("-------------------------------")

question_3 = print("What is the smallest country in the world by land area? ")
print("a) Monaco ")
print("b) Vatican City")
print("c) San Marino ")
print("d) Liechtenstein")
answer_3 = input("ANSWER: ")
check_answer(question_3, answer_3, ("a","c","d"), "b")

print("-------------------------------")

question_4 = print("Who discovered Penicillin? ")
print("a) Louis Pasteur")
print("b) Robert Koch")
print("c) Alexander Fleming") 
print("d) Meliton Soriano")
answer_4 = input("ANSWER: ")
check_answer(question_4, answer_4, ("a","b","d"), "c")

print("-------------------------------")

question_5 = print("Who painted the Mona Lisa? ")
print("a) Pablo Picasso")
print("b) Vincent Van Gogh")
print("c) Leonardo Davinci")
print("d) Michaelangelo ")
answer_5 = input("ANSWER: ")
check_answer(question_5, answer_5, ("a","b","d"), "c")

print("-------------------------------")

question_6 = print("What is the largest human organ? ")
print("a) Heart")
print("b) Brain ")
print("c) Liver ")
print("d) skin ")
answer_6 = input("ANSWER: ")
check_answer(question_6, answer_6, ("a", "b", "c"), "d")

print("-------------------------------")

question_7 = print("A tetredecahedron has how many faces? ")
print("a) 13 ")
print("b) 14 ")
print("c) 23 ")
print("d) 24 ")
answer_7 = input("ANSWER: ")
check_answer(question_7, answer_7, ("a","c","d"), "b")

print("-------------------------------")

question_8 = print("Which one of these animals lays eggs? ")
print("a) Platypus")
print("b) Lion ")
print("c) Porcupine ")
print("d) Hedgehog ")
answer_8 = input("ANSWER: ")
check_answer(question_8, answer_8, ("b","c","d"), "a")

print("-------------------------------")

question_9 = print("What does NDL stand for? ")
print("a) National democratic Leaders ")
print("b) Nicely Done Loser ")
print("c) Niko Defense league ")
print("d) Non distinct linguistics ")
answer_9 = input("ANSWER: ")
check_answer(question_9, answer_9, ("a", "b", "d"), "c")

print("-------------------------------")

question_10 = print("What is the functional group of a carboxylic acid? ")
print("a) C-H ")
print("b) -OH ")
print("c) -OOH ")
print("d) C-NH3 ")
answer_10 = input("ANSWER: ")
check_answer(question_10, answer_10, ("a", "b", "d"), "c")

print("-------------------------------")

print("{}/10" .format(score)) #prints teh final score and code ends




