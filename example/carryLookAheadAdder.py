from pybit.bits import Bits
from pybit.multiplication import Multiplication

X = Bits.from_bin('10111101')
Y = Bits.from_bin('10101111')
P, G, CO, S = Multiplication.CLA(X, Y, CI0=0, size=8)

print("P: ", P.hex)
print("G: ", G.hex)
print("S: ", S.hex)
print("CO: ", CO.hex)
