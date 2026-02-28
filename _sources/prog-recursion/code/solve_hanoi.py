from hanoi2 import HanoiTowers
from time import sleep

hanoi = HanoiTowers(n=3, names=["A", "B", "C"], speed=3)
# Variables A, B and C refer to the towers which can be manipulated through 
# overloaded operators < and >
[A, B, C] = hanoi.sticks_in_order()
sleep(1)

# moves to solve the game for n=3
A > C
A > B
C > B
A > C
B > A
B > C
A > C

print("Necessary moves : ", hanoi.get_total_moves())

# reset game to solve for N=4
sleep(1)
hanoi.reset(n=4)