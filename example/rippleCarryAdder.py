from pybit.bits import Bits
from pybit.multiplication import Multiplication

X = Bits.from_bin('01111010')
Y = Bits.from_bin('10111011')
ans = Multiplication.RCA(X, Y, CI0=0, size=8)

print("S: ", ans[0].hex)
print("CO: ", ans[1].hex)
