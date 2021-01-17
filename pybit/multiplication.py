from pybit.bits import Bits


class Multiplication:

    @staticmethod
    def booth_primary():
        pass

    @staticmethod
    def booth_secondary(A: Bits, B: Bits, t: str = 'bin'):
        PPType = {
            '000': "0",
            '001': "+1",
            '010': "+1",
            '011': "+2",
            '100': "-2",
            '101': "-1",
            '110': "-1",
            '111': "0"
        }
        size = [len(A), len(B)]
        if size[0] != size[1]:
            raise TypeError('A and B must be same length')
        if size[0] != 6:
            raise TypeError('Only supports 6 bits now')

        # 符号拡張
        A = A.sign_extend(size=size[0] * 2)
        B = B.sign_extend(size=size[1] * 2)
        B = B << ('l', 1)

        pp = []

        for i in range(3):
            bit3 = ''.join(map(str, B[12 - 3 - 2 * i:12 - 2 * i]))

            if PPType[bit3] == "0":
                pp.append(Bits.from_dec(0, 12))
            elif PPType[bit3] == "+1":
                pp.append(A << ('l', 2 * i))
            elif PPType[bit3] == "+2":
                pp.append(A << ('l', 1) << ('l', 2 * i))
            elif PPType[bit3] == "-1":
                invA = A.__invert__()
                pp.append(invA << ('l', 2 * i))
            elif PPType[bit3] == "-2":
                invA = A.__invert__()
                pp.append(invA << ('l', 1) << ('l', 2 * i))
            else:
                raise TypeError("unintended bit3")
        for i in pp:
            print(i[0:])
        ans = Bits([0])

        return pp.append(ans)

    @staticmethod
    def booth_tertiary():
        pass

    @staticmethod
    def partial_product():
        pass

    @staticmethod
    def wallace_tree():
        pass


# print(Multiplication.booth_secondary(Bits.from_dec(10, 6), Bits.from_dec(-1, 6)))
Multiplication.booth_secondary(Bits.from_dec(0b010111, 6), Bits.from_dec(0b001011, 6))
