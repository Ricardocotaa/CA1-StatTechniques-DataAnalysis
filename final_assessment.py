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
