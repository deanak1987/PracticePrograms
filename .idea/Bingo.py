import random

from tabulate import tabulate
from colorama import Fore, Back, Style


bingo = [[],[],[],[],[]]
bingoinv = [[],[],[],[],[]]

# Checks to see if random number has already been picked.
def checknum(num,list):
    result = False
    for x in list:
        if num == x:
            result = True
    return result

# Checks to see if there is a bingo
def bingoCheck(bingo1s):
    Bingoo = False
    # Checks for horizontal bingo
    for x in range(5):
        count = 0
        for y in range(5):
            if bingo1s[x][y] == 1:
                count = count + 1
        if count == 5:
            Bingoo = True
    # Checks for verical bingo
    for x in range(5):
        count = 0
        for y in range(5):
            if bingo1s[y][x] == 1:
                count = count + 1
        if count == 5:
            Bingoo = True

    # Checks for up-diagonal bingo
    count = 0
    for x in range(5):
        if bingo1s[x][x] == 1:
            count = count + 1
        if count == 5:
            Bingoo = True

    # Checks for down-diagonal bingo
    count = 0
    for x in range(5):
        if bingo1s[x][4-x] == 1:
            count = count + 1
        if count == 5:
            Bingoo = True

    # Checks for blackout bingo
    count = 0
    for x in range(5):
        for y in range(5):
            if bingo1s[x][y] == 1:
                count = count + 1
        if count == 25:
            Bingoo = True
            print("BLACKOUT")

    if Bingoo == True:
        print("BINGO!")

# Create bingo board
for x in range(5):
    for y in range(5):
        while True:
            temp = random.randrange((x+1)*15-14,(x+1)*15)
            if not checknum(temp, bingo[x]):
                bingo[x].append(temp)
                break

# Free spot
bingo[2][2] = 'F'

# Rotate bingo board
for x in range(5):
    for y in range(5):
        bingoinv[x].append(bingo[y][x])
table = [['B', 'I', 'N', 'G', 'O'],bingoinv[0],bingoinv[1],bingoinv[2],bingoinv[3],bingoinv[4]]


bingoinv[2][2] = Fore.RED + str(bingoinv[2][2]) +Fore.RESET

print(tabulate(table))

# Choose numbers at random
numbers = []
for x in range(70):
    boolean = True
    while boolean == True:
        temp = random.randrange(1,75)
        if not checknum(temp, numbers):
            numbers.append(temp)
            break
print(numbers)
bingofill = [[0]*5,[0]*5,[0,0,1,0,0],[0]*5,[0]*5]

# Check to see if numbers are on the card and aint them red if they are
for x in numbers:
    if x < 16:
        i = 0
    elif 15< x < 31:
        i = 1
    elif 30< x < 46:
        i = 2
    elif 45< x < 61:
        i = 3
    else:
        i = 4
    for y in range(5):
        if x == bingoinv[y][i]:
            bingoinv[y][i] = Fore.RED + str(bingoinv[y][i]) + Fore.RESET
            bingofill[y][i] = 1

print(tabulate(table))
bingoCheck(bingofill)

