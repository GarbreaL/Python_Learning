import random


def getAnswers(answerNumber):
    if answerNumber == '1':
        return 'It is OK'
    elif answerNumber == "2":
        return "It is decidedly too"
    elif answerNumber == "9":
        return "Very doubtful"
    else:
        return " answerNumber is a Integer"


r = random.randint(1, 9)
result = getAnswers(r)
print(result)
print(getAnswers(str(random.randint(1, 2))))
