'''
this program is to create bar graphs based on
questions given to user
done in class week 1
Jan 29, 2026
'''

import random
questions = ['How much do you like pizza','How much do you like math','How much do you like coding']

# input from user
#input('Hi user based on the following question give your preference on scale 1-10')

choiceResult = []
for x in range(3):
    choiceResult.append((random.randint(1,10)))

graphStrings = []

for i in range(max(choiceResult)):
    print(i)
    if choiceResult[0] > 0:
        graphStrings.append(" | ")
    else:
        graphStrings.append("   ")
    if choiceResult[1] > 0:
        graphStrings[i] += ' | '
    else:
        graphStrings[i] += '   '
    if choiceResult[2] > 0:
        graphStrings[i] += ' | '
    else:
        graphStrings[i] += '   '
    choiceResult[0] -= 1
    choiceResult[1] -= 1
    choiceResult[2] -= 1

"""""
for x in choiceResult:
    #print(x)
    s1 = '-'*x
    graphStrings.append(s1)
"""""
for x in range(len(choiceResult)):
    print(graphStrings[len(graphStrings)-x-1])