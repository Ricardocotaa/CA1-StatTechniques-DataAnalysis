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
