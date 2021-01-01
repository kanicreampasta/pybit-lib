from pybit.bits import Bits


class Multiplication:

    @staticmethod
    def booth_primary():
        pass

    @staticmethod
    def booth_secondary(A: Bits, B: Bits, t: str = 'bin'):
        size = [len(A), len(B)]
        if size[0] != size[1]:
            raise TypeError('A and B must be same length')
        if size[0] != 6:
            raise TypeError('Only supports 6 bits now')

        # 符号拡張
        A = Bits([A[0] for _ in range(6)] + [A[i] for i in range(6)])
        B = Bits([B[0] for _ in range(6)] + [B[i] for i in range(6)])



    @staticmethod
    def booth_tertiary():
        pass

    @staticmethod
    def partial_product():
        pass

    @staticmethod
    def wallace_tree():
        pass
