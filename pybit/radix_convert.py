from pybit.bits import Bits, BitsOperationError


class RadixConvert:

    @staticmethod
    def dec_to_bin(value: int, size: int = 0) -> Bits:
        """
        Convert decimal number to binary.
        :param value: (int) Decimal number.
        :param size: (int) [Optional] Number of digits.
        :return: (Bits) Binary number
        """
        if value >= 0:
            binary = Bits([int(x) for x in list('{0:#0{1}b}'.format(value, size + 2))[2:]])
        else:
            # Calc 2s compliment and mask bits for designated digits
            binary = Bits([int(x) for x in bin(((-value ^ (2 ** 32 - 1)) + 0b1) & 2 ** size - 1)[2:]])
        return binary

    @staticmethod
    def dec_to_hex(value: int, digits: int = 0) -> str:
        """
        Convert decimal number to hexadecimal number.
        TODO: allow negative decimal
        :param value: (int) Decimal number.
        :param digits: (int) Number of digits.
        :return: (str) Hexadecimal number
        """
        hexadecimal = ''
        if value >= 0:
            hexadecimal = '{0:#0{1}x}'.format(value, digits + 2)
        else:
            digits *= 4
            # Calc 2s compliment and mask bits for designated digits
            hexadecimal = hex(((-value ^ (2 ** 32 - 1)) + 0b1) & 2 ** digits - 1)
        return hexadecimal
