"""
Prog:   mathsTriviaGame.py
Name:   Tom Poletti
Date:   2018/05/09
Desc:   Maths Trivia Game
"""

qs = ['43+109=', '4*29=', '1836/12=', '259-74=', '3**5=']
ans = ['152', '116', '153', '185', '243']

print(qs[1])

for i,item in enumerate(qs):
    inp=input(item)
    if inp == (ans[i]):
        print('Correct!')
    else:
        print('Incorrect!')
