# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
import json

class Question:
    question:str
    answers:list
    answer:int

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

Questions = []

for i in range(4):
    question = ""
    answers = ["", "", "", ""]
    answer = 0
    while question == "":
        question = input(f"Question ({i+1}): ")
    for o in range(4):
        while answers[o] == "":
            answers[o] = input(f"Answer ({o+1}): ")
    while answer <= 0 or answer > 4:
        try: answer = int(input("Which answer is correct? "))
        except: pass
    ques = Question()
    ques.question = question
    ques.answers = answers
    ques.answer = answer
    Questions.append(ques.toJson())

with open("Questions.json", "w") as f:
    f.write(json.dumps(Questions))
