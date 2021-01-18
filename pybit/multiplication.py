from pybit.bits import Bits


class Multiplication:
    @staticmethod
    def _check_len(A: Bits, B: Bits):
        size = [len(A), len(B)]
        if size[0] != size[1]:
            raise TypeError('A and B must be same length')
        if size[0] != 6:
            raise TypeError('Only supports 6 bits now')

    @staticmethod
    def _extend(A: Bits, B: Bits):
        # 符号拡張
        A = A.sign_extend(size=12)
        # Bのlsbに0を入れる
        B = B.sign_extend(size=12) << ('l', 1)
        return A, B

    @staticmethod
    def booth_secondary(A: Bits, B: Bits):
        PPType = {
            '000': ('', 0), '100': ('-', 2),
            '001': ('+', 1), '101': ('-', 1),
            '010': ('+', 1), '110': ('-', 1),
            '011': ('+', 2), '111': ('', 0)
        }

        Multiplication._check_len(A, B)
        A, B = Multiplication._extend(A, B)
        pp = []

        for i in range(3):
            bit3 = ''.join(map(str, B[12 - 3 - 2 * i:12 - 2 * i]))

            if PPType[bit3][0] == '-':
                _A = A.__invert__() + Bits([1])
            else:
                _A = A

            if PPType[bit3][1] == 0:
                pp.append(Bits.from_dec(0, 12))
            elif PPType[bit3][1] == 1:
                pp.append(_A << ('l', 2 * i))
            elif PPType[bit3][1] == 2:
                pp.append(_A << ('l', 1) << ('l', 2 * i))
            else:
                raise TypeError("unintended bit3")

        # 部分積をたしあわせて溢れた分をカット
        ans = (pp[0] + pp[1] + pp[2]).sign_extend(size=12)
        pp.append(ans)

        return pp

    @staticmethod
    def booth_tertiary(A: Bits, B: Bits):
        PPType = {
            '0000': ('', 0), '1000': ('-', 4),
            '0001': ('+', 1), '1001': ('-', 3),
            '0010': ('+', 1), '1010': ('-', 3),
            '0011': ('+', 2), '1011': ('-', 2),
            '0100': ('+', 2), '1100': ('-', 2),
            '0101': ('+', 3), '1101': ('-', 1),
            '0110': ('+', 3), '1110': ('-', 1),
            '0111': ('+', 4), '1111': ('', 0),
        }

        Multiplication._check_len(A, B)
        A, B = Multiplication._extend(A, B)
        pp = []

        for i in range(2):
            bit4 = ''.join(map(str, B[12 - 4 - 3 * i:12 - 3 * i]))
            print(bit4)

            if PPType[bit4][0] == '-':
                _A = A.__invert__() + Bits([1])
            else:
                _A = A

            if PPType[bit4][1] == 0:
                pp.append(Bits.from_dec(0, 12))
            elif PPType[bit4][1] == 1:
                pp.append(_A << ('l', 3 * i))
            elif PPType[bit4][1] == 2:
                pp.append(_A << ('l', 1) << ('l', 3 * i))
            elif PPType[bit4][1] == 3:
                _p = ((_A << ('l', 1)) + _A).sign_extend(size=12)
                pp.append(_p << ('l', 3 * i))
            elif PPType[bit4][1] == 4:
                pp.append(_A << ('l', 2) << ('l', 3 * i))
            else:
                raise TypeError("unintended bit4")

        # 部分積をたしあわせて溢れた分をカット
        ans = (pp[0] + pp[1]).sign_extend(size=12)
        pp.append(ans)

        return pp

    @staticmethod
    def partial_product():
        pass

    @staticmethod
    def wallace_tree():
        pass
