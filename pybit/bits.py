from typing import Optional, List, Tuple


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
    def __init__(self, bits: Optional[List[int]]=None, *, size: Optional[int]=None) -> None:
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
    
    def zero_extend(self, *, size: int) -> 'Bits':
        bits_data = [0 for i in range(size)]
        current_size = len(self)
        for i in range(min(size, current_size)):
            bits_data[size-1-i] = self.bits[current_size-1-i]
        return Bits(bits_data)
    
    def sign_extend(self, *, size: int) -> 'Bits':
        msb = self.bits[0]
        bits_data = [msb for i in range(size)]
        current_size = len(self)
        for i in range(min(size, current_size)):
            bits_data[size-1-i] = self.bits[current_size-1-i]
        return Bits(bits_data)
