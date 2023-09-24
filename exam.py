import json
import os


def read_questions():
    with open("questions.json", "r") as file:
        return json.load(file)


def ask_question(qus):
    print("Lenght of list of answers : ", len(qus['answer']))
    answer_lenght = len(qus["answer"])
    if answer_lenght == 1:
        for i, option in enumerate(qus["options"]):
            print(str(i + 1) + ") " + option)
        user_answer = input(qus["question"])
        return user_answer
    else:
        for i, option in enumerate(qus["options"]):
            print(str(i + 1) + ") " + option)
        print(f" *  Notice: Choose {answer_lenght} answers separated by ','  like: 2,3")
        user_answer = input(qus["question"])
        return user_answer


def check_answer(qus, ans):
    if len(qus['answer']) == 1:
        if qus["options"][int(ans) - 1] == qus["answer"]:
            print("correct")
            return 1
        else:
            print("Incorrect")
            return 0
    else:
        answers = ans.split(",")
        print(answers)
        for a in answers:
            if qus["options"][int(a)-1] in qus['answer']:
                print(qus["options"][int(a)-1])
            else:
                print('wrong')


def explain(qus):
    ...

def quiz(questions):
    for q in questions:
        os.system('clear')
        answer = ask_question(q)
        check_answer(q, answer)
        input("Press Enter to continue ...")


if __name__ == "__main__":
    questions = read_questions()
    quiz(questions)
