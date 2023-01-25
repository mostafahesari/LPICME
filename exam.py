import json

def read_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def start_quiz():
    questions = read_questions()
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(str(i + 1) + ") " + option)
        user_answer = input("Enter the number of your answer: ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. ")
            print("Answer is: ", question["answer"])
        print(question["explanation"])
    print("Your final score is " + str(score) + " out of " + str(len(questions)) + ".")

start_quiz()

