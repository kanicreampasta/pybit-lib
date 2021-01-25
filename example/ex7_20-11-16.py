from pybit.bits import Bits
from pybit.multiplication import Multiplication

# Question 1
print("========Q1========")
P1 = Bits.from_bin('11110100')
Q1 = Bits.from_bin('00001011')

# (a)
print("s0: ", (P1.zero_extend(size=32)).hex)
# (b)
print("s1: ", (Q1.zero_extend(size=32)).hex)
# (c)
print("s0: ", (P1.sign_extend(size=32)).hex)
# (d)
print("s1: ", (Q1.sign_extend(size=32)).hex)

# Question2
print("========Q2========")
P2 = Bits.from_bin('01111010')
Q2 = Bits.from_bin('10111011')
ans = Multiplication.RCA(P2, Q2, CI0=0, size=8)

# (a)
print("(a): ", P2.int)
# (b)
print("(b): ", Q2.int)
# (c)
print("(c): ", ans[0].hex)
# (d)
print("(d): ", ans[1].hex)

# Question3
print("========Q3========")
X3 = Bits.from_bin('01011010')
Y3 = Bits.from_bin('10111000')
ans2 = Multiplication.CLA(X3, Y3, CI0=0, size=8)

# (a)
print("(a): ", ans2[0].hex)
# (b)
print("(b): ", ans2[1].hex)
# (c)
print("(c): ", ans2[3].hex)
# (d)
print("(d): ", ans2[2].hex)

# Question4
print("========Q4========")

