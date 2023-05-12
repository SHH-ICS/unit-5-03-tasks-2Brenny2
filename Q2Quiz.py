# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
import json


with open("Questions.json", "r") as f:
    Questions = json.loads(f.read())

Score = 0

index = 0
for ques in Questions:
    index += 1
    question = json.loads(ques)
    print(f"Question {index}: {question['question']}")
    i = 0
    for ans in question["answers"]:
        i += 1
        print(f"{i}) {ans}")
    answer = 0
    while answer <= 0 or answer > 4:
        try: answer = int(input("Answer: "))
        except: pass
    if answer == question["answer"]:
        print("Correct")
        Score += 1
    else:
        print("Incorrect")

print(f"\n\nScore: {Score}/4")
