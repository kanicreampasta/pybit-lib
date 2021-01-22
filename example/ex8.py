from pybit.bits import Bits
from pybit.multiplication import Multiplication
# Question 1
X = Bits.from_bin('10111101')
Y = Bits.from_bin('10101111')

P, G, CO, S = Multiplication.CLA(X, Y, CI0=0, size=8)
# (a)
print("P: ", P[0:])
# (b)
print(G[0:])
# (c)
print(S[0:])
# (d)
print(CO[0:])

