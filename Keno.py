import random

from tabulate import tabulate
from colorama import Fore, Back, Style
import numpy as np
w = 10 # board width
h = 8 # board height
p = 20 # numbers picked
c = 10 # numbers chosen
keno = [[],[],[],[],[],[],[],[]]
kenonum = [[],[],[],[],[],[],[],[]]

for i in range(h):
    x = i * 10
    for j in range(w):
        keno[i].append(x + j + 1)
        kenonum[i].append(x + j + 1)

# Checks to see if random number has already been picked.
def checknum(num,list):
    result = False
    for x in list:
        if num == x:
            result = True
    return result
print(tabulate(keno))

def win(picks, hits):
    payoutTable = [[0,0,0,0,0,0,0,0,0,3],
                   [2,0,0,0,0,0,0,0,0,0],
                   [0,8,2,1,0,0,0,0,0,0],
                   [0,0,16,5,2,1,1,0,0,0],
                   [0,0,0,24,17,4,2,2,1,0],
                   [0,0,0,0,200,40,10,5,5,2],
                   [0,0,0,0,0,1000,100,50,10,5],
                   [0,0,0,0,0,0,2500,500,100,50],
                   [0,0,0,0,0,0,0,10000,2500,500],
                   [0,0,0,0,0,0,0,0,25000,5000],
                   [0,0,0,0,0,0,0,0,0,100000]]
    return payoutTable[hits][picks-1]

# Choose numbers at random for picks
numbers = []
for x in range(p):
    boolean = True
    while boolean == True:
        temp = random.randrange(1,80)
        if not checknum(temp, numbers):
            numbers.append(temp)
            break
print(numbers)

# Choose numbers at random for picks
chosennumbers = []

for x in range(c):
    boolean = True
    while boolean == True:
        temp = random.randrange(1,80)
        if not checknum(temp, chosennumbers):
            chosennumbers.append(temp)
            break

print(chosennumbers)

# Paint chosen numbers red on Keno board
for x in chosennumbers:
    if x <= 10:
        i = 0
    elif 10 < x <= 20:
        i = 1
    elif 20 < x <= 30:
        i = 2
    elif 30 < x <= 40:
        i = 3
    elif 40 < x <= 50:
        i = 4
    elif 50 < x <= 60:
        i = 5
    elif 60 < x <= 70:
        i = 6
    else:
        i = 7
    for y in range(w):
        if x == kenonum[i][y]:
            keno[i][y] = Fore.BLUE + str(x) + Fore.RESET

count = 0
# Paint chosen numbers red on Keno board
for x in numbers:
    if x <= 10:
        i = 0
    elif 10 < x <= 20:
        i = 1
    elif 20 < x <= 30:
        i = 2
    elif 30 < x <= 40:
        i = 3
    elif 40 < x <= 50:
        i = 4
    elif 50 < x <= 60:
        i = 5
    elif 60 < x <= 70:
        i = 6
    else:
        i = 7
    for y in range(w):
        if x == kenonum[i][y]:
            keno[i][y] = Back.RED + str(x) + Back.RESET
            for z in chosennumbers:
                if x == z:
                    count = count + 1
                    keno[i][y] = Back.RED + Fore.BLUE + str(x) + Back.RESET + Fore.RESET
            break


print(tabulate(keno))
print(count)
print("You won " + str(win(len(chosennumbers), count)) + "!")



