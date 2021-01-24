from pybit.bits import Bits
from pybit.multiplication import Multiplication

# Question 1 (CLA)
X1 = Bits.from_bin('10111101')
Y1 = Bits.from_bin('10101111')
P, G, CO, S = Multiplication.CLA(X1, Y1, CI0=0, size=8)

# (a)
print("P: ", P.hex)
# (b)
print("G: ", G.hex)
# (c)
print("S: ", S.hex)
# (d)
print("CO: ", CO.hex)

# Question2
X2 = Bits.from_bin('010111')
Y2 = Bits.from_bin('001011')
ans = Multiplication.booth_secondary(X2, Y2)

# (a)
print("(a): ", ans[0].hex)
# (b)
print("(b): ", ans[1].hex)
# (c)
print("(c): ", ans[2].hex)
# (d)
print("(d): ", ans[3].hex)
