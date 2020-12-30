class RadixConvert:

    @staticmethod
    def dec_to_bin(value: int, digits: int = 0) -> str:
        """
        Convert decimal number to binary.
        :param value: (int) Decimal number.
        :param digits: (int) Number of digits.
        :return: (str) Binary number
        """
        binary = ''
        if value >= 0:
            binary = '{0:#0{1}b}'.format(value, digits + 2)
        else:
            # Calc 2s compliment and mask bits for designated digits
            binary = bin(((-value ^ 0b111111111111) + 0b1) & 2**digits-1)
        return binary

    @staticmethod
    def dec_to_hex(value: int) -> str:
        """
        Convert decimal number to hexadecimal number.
        TODO: allow negative decimal
        :param value: (int) Decimal number.
        :return: (str) Hexadecimal number
        """
        return hex(value)
