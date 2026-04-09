# *EXPECTED VALUE FIRST GAME*

# The player pays €5 and picks 3 letters (all lower case English letters) and 2 digits (numbers 0-9 inclusive). They win as follows:
# What is correct	Prize
# 3 letters, both numbers	€100
# Two letters, both numbers	€50
# One letter, both numbers	€25
# No letter, both numbers	€10

import pandas as pd
import random
import matplotlib.pyplot as plt

#Probabilities 

# 3 letters correct + both numbers
Plllnn = 1/26*1/26*1/26*1/10*1/10

# 2 letters correct + both numbers
Pllnn = 1/26*1/26*25/26*1/10*1/10 + 1/26*25/26*1/26*1/10*1/10 + 25/26*1/26*1/26*1/10*1/10

# 1 letter correct + both numbers
Plnn = 1/26*25/26*25/26*1/10*1/10 + 25/26*1/26*25/26*1/10*1/10 + 25/26*25/26*1/26*1/10*1/10 

# 0 letters correct + both numbers
Pnn = 25/26*25/26*25/26*1/10*1/10
#Expected value for gamer

Ex_v = Plllnn*100 + Pllnn*50 + Plnn*25 + Pnn*10

print(Ex_v)
0.1177600136549841

#Expected value for club

Ex_club = 5 - Ex_v
print(Ex_club)
4.882239986345016

# Interpretation:
# The player wins on average about €0.11 per game,
# while the club earns approximately €4.88 per game.

# *EXPECTED VALUE SECOND GAME*

# The player pays €5 and picks 3 letters (all lower case AND upper case English letters, repetition allowed). If they guess all correctly, they win €500,000

# Probability of winning

Plll= 1/52*1/52*1/52
#Expected value for gamer
#Jackpot = 500000

Ex_v2 = Plll*500000
print(Ex_v2)
3.55598543468366

#Expected value for club

Ex_club = 5 - Ex_v2
print(Ex_club)
1.44401456531634

# Interpretation:
# The player wins on average about €3.55 per game,
# while the club earns approximately €1.44 per game.

# *GAME 1 SIMULATION*
def game1():
    win_data = [
        [100, 1/26*1/26*1/26*1/10*1/10],
        [50, 1/26*1/26*25/26*1/10*1/10 + 1/26*25/26*1/26*1/10*1/10 + 25/26*1/26*1/26*1/10*1/10],
        [25, 1/26*25/26*25/26*1/10*1/10 + 25/26*1/26*25/26*1/10*1/10 + 25/26*25/26*1/26*1/10*1/10],
        [10, 25/26*25/26*25/26*1/10*1/10]
    ]
    random_num = random.random()
    cumulative_propability = 0
    
    for wins in win_data:
        cumulative_propability += wins[1]
        if cumulative_propability >= random_num:
            return wins[0]
    return 0

def simulate_game1(n=100000):
    total = 0
    for i in range (n):
        total += game1()

    EV_gamer = total / n
    EV_club = 5 - EV_gamer

    return EV_gamer, EV_club

gamer, club = simulate_game1()

print(gamer)
print(club)
0.11805
4.88195

# Interpretation:
# The player wins about €0.11 on average per game,
# but since they pay €5 to play, this results in a loss of about €4.88.
# The club therefore earns approximately €4.88 per game.

# *GAME 2 SIMULATION*

def game2():
    win_data = [
        [500000, 1/52*1/52*1/52]
    ]

    random_num = random.random()
    cumulative_probability = 0
    
    for wins in win_data:
        cumulative_probability += wins[1]
        if cumulative_probability >= random_num:
            return wins[0]

    return 0
def simulate_game2(n=500000):
    total = 0
    for i in range(n):
        total += game2()

    EV_gamer = total / n
    EV_club = 5 - EV_gamer

    return EV_gamer, EV_club

gamer, club = simulate_game2()

print(gamer)
print(club)
2.0
3.0

# Interpretation:
# The results vary because the probability of winning is very low,
# while the prize is extremely large, making the simulation unstable.

# Running the simulation multiple times to observe variability

for i in range (10):
    print(simulate_game2())

(6.0, -1.0)
(6.0, -1.0)
(4.0, 1.0)
(3.0, 2.0)
(3.0, 2.0)
(0.0, 5.0)
(5.0, 0.0)
(4.0, 1.0)
(5.0, 0.0)
(5.0, 0.0)

# Interpretation:
# The initial simulation produced varying results, which seemed unusual.
# To investigate this, the simulation was run multiple times.
# The results showed significant variation between runs.

# *MEASUARES OF CENTRAL TENDENCY GAME 1*

import numpy as np
from scipy import stats

def simulate_game1_(n=100000):
    results = []
    for i in range (n):
        results.append(5-game1())
    return results 

data1= simulate_game1_()

mean1 = np.mean(data1)
median1 = np.median(data1)
mode1 = stats.mode(data1)

print(mean1)
print(median1)
print(mode1)

4.87685
5.0
ModeResult(mode=np.int64(5), count=np.int64(98955))

# Interpretation:
# The mean profit for the club is approximately €4.88 per game.
# The median and mode are both €5, indicating that in most cases
# the club earns €5, as players usually win nothing.

# *MEASUARES OF CENTRAL TENDENCY GAME 2*

def simulate_game2_(n=100000):
    results = []
    for i in range (n):
        results.append(5-game2())
    return results 

data2= simulate_game2_()

mean2 = np.mean(data2)
median2 = np.median(data2)
mode2 = stats.mode(data2)

print(mean2)
print(median2)
print(mode2)

0.0
5.0
ModeResult(mode=np.int64(5), count=np.int64(99999))

# Interpretation:
# The median and mode are both €5, indicating that in most cases
# the club earns €5, as players usually win nothing.

# However, the mean is significantly lower due to the rare €500,000 payout,
# which greatly reduces the average profit.

# *MEASUARES OF DISPERSION GAME 1*

def simulate_game1_(n=100000):
    results = []
    for i in range (n):
        results.append(5-game1())
    return results 

data1 = simulate_game1_()

range1 = np.max(data1) - np.min(data1)
variance1 = np.var(data1)
std_dev1 = np.std(data1)

print(range1)
print(variance1)
print(std_dev1)

# Interpretation:
# Game 1 has low variance and standard deviation,
# indicating consistent and predictable results.

