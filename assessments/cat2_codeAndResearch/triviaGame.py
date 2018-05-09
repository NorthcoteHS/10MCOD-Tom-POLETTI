"""
Prog:   mathsTriviaGame.py
Name:   Tom Poletti
Date:   2018/05/09
Desc:   Maths Trivia Game
"""

qs = ['43 plus 109 equals ', '4 times 29 equals ', '1836 divided by 12 equals ', '259 minus 74 equals ', '3 to the power of 5 equals ']
ans = ['152', '116', '153', '185', '243']

count=int(0)

for i,item in enumerate(qs):
    inp=input(item)
    if inp == (ans[i]):
        print('Correct!')
        count=(count+1)
    else:
        print('Incorrect!')

mess1 = ['Unlucky, ', 'Not bad, ', 'Perfect, ']
mess2 = ('you scored')
if count == 0, 1:
    print(mess1[0]+mess2, count)
elif count == 2, 3, 4:
    print(mess1[1]+mess2, count)
else count == 5:
    print(mess1[2]+mess2, count)
