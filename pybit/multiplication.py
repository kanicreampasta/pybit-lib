from pybit.bits import Bits


class Multiplication:
    @staticmethod
    def _check_len(A: Bits, B: Bits, size: int):
        sizes = [len(A), len(B)]
        if sizes[0] != sizes[1]:
            raise TypeError('A and B must be same length')
        if sizes[0] != size:
            raise TypeError('Only supports {0} bits now'.format(size))

    @staticmethod
    def _extend(A: Bits, B: Bits):
        # 符号拡張
        A = A.sign_extend(size=12)
        # Bのlsbに0を入れる
        B = B.sign_extend(size=12) << ('l', 1)
        return A, B

    @staticmethod
    def _ini(q: int, size: int):
        return (Bits.from_dec(0, size) for _ in range(q))

    @staticmethod
    def booth_secondary(A: Bits, B: Bits):
        PPType = {
            '000': ('', 0), '100': ('-', 2),
            '001': ('+', 1), '101': ('-', 1),
            '010': ('+', 1), '110': ('-', 1),
            '011': ('+', 2), '111': ('', 0)
        }

        Multiplication._check_len(A, B, size=6)
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

        Multiplication._check_len(A, B, size=6)
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
    def CLA(A: Bits, B: Bits, CI0: int, size: int):
        """
        lsb: list(size-1)
        msb: list(0)
        return:(list) [P, G, CO, S](Bits)
        """
        Multiplication._check_len(A, B, size=size)
        G, P, CI, CO, S = Multiplication._ini(q=5, size=size)
        CI[size - 1] = CI0

        for i in range(size):
            idx = size - (i + 1)
            G[idx] = A[idx] & B[idx]
            P[idx] = A[idx] ^ B[idx]
            CO[idx] = G[idx] + (P[idx] & CI[idx])
            if i != size - 1:
                CI[idx - 1] = CO[idx]
            else:
                continue
            S[idx] = P[idx] ^ CI[idx]

        return [P, G, CO, S]

    @staticmethod
    def CSA(X: Bits, Y: Bits, Z: Bits, size: int):
        Multiplication._check_len(X, Y, size=size)
        Multiplication._check_len(Y, Z, size=size)
        S, C = Multiplication._ini(q=2, size=size)

        for i in range(size):
            idx = size - (i + 1)
            S[idx] = X[idx] ^ Y[idx] ^ Z[idx]
            C[idx] = ((X[idx] & Y[idx]) + (Y[idx] & Z[idx]) + (Z[idx] & X[idx])) % 2
        C = C << ('l', 1)
        return [S, C]

    @staticmethod
    def RCA(A: Bits, B: Bits, CI0: int, size: int):
        Multiplication._check_len(A, B, size=size)
        S, CI, CO = Multiplication._ini(q=3, size=size)
        CI[size-1] = CI0

        for i in range(size):
            idx = size - (i + 1)
            S[idx] = A[idx] ^ B[idx] ^ CI[idx]
            CO[idx] = ((A[idx] & B[idx]) + (B[idx] & CI[idx]) + (CI[idx] & A[idx])) % 2
            if i != size - 1:
                CI[idx - 1] = CO[idx]

        return [S, CO]

    @staticmethod
    def partial_product():
        pass

    @staticmethod
    def wallace_tree():
        pass
