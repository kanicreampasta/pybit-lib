from pybit.bits import Bits
from pybit.multiplication import Multiplication


X = Bits.from_bin('010111')
Y = Bits.from_bin('001011')
ans = Multiplication.booth_secondary(X, Y)

# Partial Product 1st line
print("PP1: ", ans[0].hex)
# Partial Product 2nd line
print("PP2: ", ans[1].hex)
# Partial Product 3rd line
print("PP3: ", ans[2].hex)
# Answer
print("Answer: ", ans[3].hex)

print("=====================")

X2 = Bits.from_bin('100010')
Y2 = Bits.from_bin('001110')
# When X2 is considered non 2's complementary number
ans2 = Multiplication.booth_secondary(X2, Y2, Apositive=True)

# Partial Product 1st line
print("PP1: ", ans2[0].hex)
# Partial Product 2nd line
print("PP2: ", ans2[1].hex)
# Partial Product 3rd line
print("PP3: ", ans2[2].hex)
# Answer
print("Answer: ", ans2[3].hex)

print("=====================")

X3 = Bits.from_bin('101111')
Y3 = Bits.from_bin('110010')
ans3 = Multiplication.booth_tertiary(X3, Y3)

# Partial Product 1st line
print("PP1: ", ans3[0].hex)
# Partial Product 2nd line
print("PP3: ", ans3[1].hex)
# Answer
print("Answer: ", ans3[2].hex)
