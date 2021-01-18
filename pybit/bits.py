from typing import Optional, List, Tuple
import collections


class BitsError(Exception):
    def __init__(self, msg: str) -> None:
        super(BitsError, self).__init__(msg)


class BitsConstructError(BitsError):
    def __init__(self, msg: str) -> None:
        super(BitsConstructError, self).__init__(msg)


class BitsOperationError(BitsError):
    def __init__(self, msg: str) -> None:
        super(BitsOperationError, self).__init__(msg)


class Bits:
    def __init__(self, bits: Optional[List[int]] = None, *, size: Optional[int] = None) -> None:
        if bits:
            self.bits = bits
        else:
            if size:
                self.bits = [0 for x in range(size)]
            else:
                raise BitsConstructError('size must be specified')

    def __getitem__(self, key: int) -> int:
        return self.bits[key]

    def __setitem__(self, key: int, val: int) -> int:
        self.bits[key] = val

    def __len__(self) -> int:
        return len(self.bits)

    def _check_len_eq(self, o: 'Bits') -> None:
        if len(self) != len(o):
            raise BitsOperationError('Bits length does not match')

    def __eq__(self, o) -> bool:
        if isinstance(o, Bits):
            self._check_len_eq(o)
            return all([a == b for a, b in zip(self.bits, o.bits)])
        return False

    def __ne__(self, o) -> bool:
        return not self.__eq__(o)

    def __and__(self, o: 'Bits') -> 'Bits':
        if isinstance(o, Bits):
            self._check_len_eq(o)
            return Bits([1 if a == 1 and b == 1 else 0 for a, b in zip(self.bits, o.bits)])
        raise TypeError('o must be Bits')

    def __or__(self, o: 'Bits') -> 'Bits':
        if isinstance(o, Bits):
            self._check_len_eq(o)
            return Bits([1 if a == 1 or b == 1 else 0 for a, b in zip(self.bits, o.bits)])
        raise TypeError('o must be Bits')

    def __xor__(self, o: 'Bits') -> 'Bits':
        if isinstance(o, Bits):
            self._check_len_eq(o)
            return Bits([1 if a != b else 0 for a, b in zip(self.bits, o.bits)])
        raise TypeError('o must be Bits')

    def __invert__(self) -> 'Bits':
        return Bits([1 - x for x in self.bits])

    def __rshift__(self, arg: Tuple[str, int]) -> 'Bits':
        t, n = arg
        size = len(self.bits)
        if t == 'l' or t == 'logic':
            return Bits([0 for _ in range(min(n, size))] + self.bits[:max(size - n, 0)])
        elif t == 'a' or t == 'arithmetic':
            msb = self.bits[0]
            return Bits([msb for _ in range(min(n, size))] + self.bits[:max(size - n, 0)])
        else:
            raise TypeError('shift type must be logical or arithmetic')

    def __lshift__(self, arg: Tuple[str, int]) -> 'Bits':
        t, n = arg
        size = len(self.bits)
        lst = self.bits + [0 for _ in range(n)]
        if t == 'l' or t == 'logic':
            return Bits(lst[n:])
        elif t == 'a' or t == 'arithmetic':
            msb = self.bits[0]
            return Bits([msb] + lst[n + 1:])
        else:
            raise TypeError('shift type must be logical or arithmetic')

    def __add__(self, o: 'Bits') -> 'Bits':
        if isinstance(o, Bits):
            # 1桁多めにとる
            mlen = max(len(self.bits), len(o.bits)) + 1

            A = self.zero_extend(size=mlen)
            B = o.zero_extend(size=mlen)

            while B != Bits.from_dec(0b0, size=mlen):
                tmp = (A & B) << ('l', 1)
                A = A ^ B
                B = tmp

            # オーバーフローしてたら拡張して返す
            return A if A[0] == 1 else A.sign_extend(size=mlen-1)
        raise TypeError('o must be Bits')

    def zero_extend(self, *, size: int) -> 'Bits':
        bits_data = [0 for i in range(size)]
        current_size = len(self)
        for i in range(min(size, current_size)):
            bits_data[size - 1 - i] = self.bits[current_size - 1 - i]
        return Bits(bits_data)

    def sign_extend(self, *, size: int) -> 'Bits':
        msb = self.bits[0]
        bits_data = [msb for i in range(size)]
        current_size = len(self)
        for i in range(min(size, current_size)):
            bits_data[size - 1 - i] = self.bits[current_size - 1 - i]
        return Bits(bits_data)

    @staticmethod
    def from_dec(value: int, size: int = None) -> 'Bits':
        """
        Convert decimal number to binary.
        :param value: (int) Decimal number.
        :param size: (int) [Optional] Number of BINARY digits.
        :return: (Bits) Binary number
        """
        if value >= 0:
            binary = [int(x) for x in list('{0:#0{1}b}'.format(value, 32 + 2))[2:]]
            if size is None:
                size = 1  # for 0
                for i, b in enumerate(binary):
                    if b == 1: size = 32 - i; break
        else:
            # Calc 2s compliment and mask bits for designated digits
            binary = [int(x) for x in bin(((-value ^ (2 ** 32 - 1)) + 0b1) & 2 ** 32 - 1)[2:]]
            if size is None:
                size = 1  # for -1
                for i, b in enumerate(binary):
                    if b == 0: size = 32 - i + 1; break

        return Bits(binary[32 - size:])

    @staticmethod
    def from_hex(value: int, size: int = 0) -> 'Bits':
        """
        Convert hexadecimal number to binary.
        :param value: (int) Decimal number.
        :param size: (int) [Optional] Number of BINARY digits.
        :return: (Bits) Binary number
        """
        if size == 0:
            size = len(list(hex(value))[2:]) * 4
        binary = [int(x) for x in list('{0:#0{1}b}'.format(value, size + 2))[2:]]

        return Bits(binary)
