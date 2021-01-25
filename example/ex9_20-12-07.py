from pybit.bits import Bits
from pybit.multiplication import Multiplication

# Question 1
print("========Q1========")
X1 = Bits.from_bin('101111')
Y1 = Bits.from_bin('110010')
ans = Multiplication.booth_secondary(X1, Y1)
# (a)
print("(a): ", ans[0].hex)
# (b)
print("(b): ", ans[1].hex)
# (c)
print("(c): ", ans[2].hex)
# (d)
print("(d): ", ans[3].hex)

# Question2
print("========Q2========")
X2 = Bits.from_bin('101111')
Y2 = Bits.from_bin('110010')
ans2 = Multiplication.booth_tertiary(X2, Y2)
Z = Y2 ^ Bits.from_bin('101000')
ans3 = Multiplication.booth_tertiary(X2, Z)

# (a)
print("(a): ", ans2[0].hex)
# (b)
print("(b): ", ans2[1].hex)
# (c)
print("(c): ", ans3[0].hex)
# (d)
print("(d): ", ans3[1].hex)

# Question3
print("========Q3========")


# Question4
print("========Q4========")

