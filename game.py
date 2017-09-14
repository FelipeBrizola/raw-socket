import json
from random import randint

def sortQuestionByLevel(level):
    questions = getQuestions()

    indexOfQuestion = randint(0, 1)
    questionsOfLevel = questions[level]
    return questionsOfLevel[indexOfQuestion]

def getQuestions():
    with open('questions.json') as json_data:
        return json.load(json_data)

def isCorrect(question, answerIndex):
    return question.correctAnswerIndex == answerIndex

# ta martelado
def finishMessage(question):
    return "voce ganhou " + question['reward']

if __name__ == "__main__":
    print sortQuestionByLevel(0)