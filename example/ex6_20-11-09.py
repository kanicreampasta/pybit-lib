from pybit.bits import Bits
from pybit.multiplication import Multiplication

# Question 1
print("========Q1========")
print("(a): ", Bits.from_float(-0.5).hex)
print("(b): ", Bits.from_float(1.5).hex)
print("(c): ", Bits.from_float(10.5).hex)
print("(d): ", Bits.from_float(5).hex)

# Question2
print("========Q2========")

# (a)
print("(a): ", Bits.from_float12(-0.5).hex)
# (b)
print("(b): ", Bits.from_float12(1.5).hex)
# (c)
print("(c): ", Bits.from_float12(10.5).hex)
# (d)
print("(d): ", Bits.from_float12(5.0).hex)

# Question3
print("========Q3========")
P = Bits.from_bin('11010010')
Q = Bits.from_bin('00011010')
ans2 = Multiplication.RCA(P, Q, CI0=0, size=8)

# (a)
print("(a): ", P.int)
# (b)
print("(b): ", Q.int)
# (c)
print("(c): ", ans2[0].hex)
# (d)
print("(d): ", ans2[1].hex)

# Question4
print("========Q4========")
QB = ~ Q
ans3 = Multiplication.RCA(P, QB, CI0=1, size=8)
ans4 = Multiplication.RCA(ans2[0], ans3[0], CI0=0, size=8)
# (a)
print("(a): ", QB.int)
# (b)
print("(b): ", ans3[0].hex)
# (c)
print("(c): ", ans3[1].hex)
# (d)
print("(d): ", ans4[0].hex)
