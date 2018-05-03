"""
Prog:   countdown.py
Name:   Tom Poletti
Date:   2018/05/03
Desc:   Counts down for blast off
"""

import time

countdown = 1

for countdown in range(10,0,-1):
    print(countdown)
    time.sleep(1)

print('BLAST OFF!')
