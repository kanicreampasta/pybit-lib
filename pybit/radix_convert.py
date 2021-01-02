import collections
from pybit.bits import Bits, BitsOperationError
import struct


class RadixConvert:

    @staticmethod
    def dec_to_bin(value: int, size: int = 0) -> Bits:
        """
        Convert decimal number to binary.
        :param value: (int) Decimal number.
        :param size: (int) [Optional] Number of BINARY digits.
        :return: (Bits) Binary number
        """
        if value >= 0:
            binary = [int(x) for x in list('{0:#0{1}b}'.format(value, size + 2))[2:]]
        else:
            # Calc 2s compliment and mask bits for designated digits
            binary = [int(x) for x in bin(((-value ^ (2 ** 32 - 1)) + 0b1) & 2 ** size - 1)[2:]]
        if size != 0:
            binary = collections.deque(binary, size)

        return Bits(binary)

    @staticmethod
    def hex_to_bin(value: int, size: int = 0) -> Bits:
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

    @staticmethod
    def float_to_bin(value: float) -> Bits:
        """
        Convert 32-bits float to Bits.
        :param value: (float) float to convert.
        :return: (Bits) A Bits instance representing the given value.
        """
        return RadixConvert.hex_to_bin(struct.unpack('>I', struct.pack('>f', value))[0], size=32)

    @staticmethod
    def dec_to_hex(value: int, digits: int = 0) -> str:
        """
        Convert decimal number to hexadecimal number.
        TODO: allow negative decimal
        :param value: (int) Decimal number.
        :param digits: (int) Number of HEX digits.
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
