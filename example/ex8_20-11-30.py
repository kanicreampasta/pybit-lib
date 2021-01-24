from pybit.bits import Bits
from pybit.multiplication import Multiplication

# Question 1 (CLA)
X1 = Bits.from_bin('10111101')
Y1 = Bits.from_bin('10101111')

P, G, CO, S = Multiplication.CLA(X1, Y1, CI0=0, size=8)
# (a)
print("P: ", P[0:])
# (b)
print("G: ", G[0:])
# (c)
print("S: ", S[0:])
# (d)
print("CO: ", CO[0:])

# Question2
X2= Bits.from_bin('010111')
X2= Bits.from_bin('001011')