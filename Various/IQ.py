#THIS IS AN IQ TEST
#Hope the best of results
#IQ results may not be acurate

import random

def resIQ(IQ):
    IQ = IQ - 5
    print('ouch')
    return IQ
def addIQ(IQ):
    IQ = IQ + 5
    print('Just win IQ!!!')
    return IQ
def qa():
    print("This programs selects a random question...")
    
    iqDef = 90
    
    isHere = []
    #Questions obtained via Chatgpt-4 turbo
    qtn = ["What is the capital of Japan?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for gold?",
    "Which planet is known as the Red Planet?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the largest ocean on Earth?",
    "How many continents are there on Earth?",
    "Who developed the theory of relativity?",
    "What is the hardest natural substance on Earth?",
    "Which country is famous for inventing pizza?"]

    ans = ["tokyo",
    "leonardodavinci",
    "au",
    "mars",
    "williamshakespeare",
    "thepacificocean",
    "seven",
    "alberteinstein",
    "diamond",
    "italy"]
    #Other possible correct answers
    ans2 = ["tokyo",
    "davinci",
    "au",
    "planetmars",
    "shakespeare",
    "pacificocean",
    "7",
    "einstein",
    "diamonds",
    "italia"]
    i = random.randint(0, 9) 
    isHere.append(i)
    for x in range(4):
        print(qtn[i])
        usout = input("Answer: ")
        if usout.lower().replace(" ", "") == ans[i] or usout.lower().replace(" ", "") == ans2[i]:
            iqDef = addIQ(iqDef)
        else:
           iqDef = resIQ(iqDef)
        while i in isHere:
            i = random.randint(0, 9) 
        isHere.append(i)
    print(f"This is your result {iqDef} points!!!")
qa()
