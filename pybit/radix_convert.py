class RadixConvert:

    @staticmethod
    def dec_to_bin(value: int, digits: int = 0) -> str:
        """
        Convert decimal number to binary.
        TODO: allow negative decimal
        :param value: (int) Decimal number.
        :param digits: (int) Number of digits.
        :return: (str) Binary number
        """
        binary = ''
        if value >= 0:
            binary = '{0:#0{1}b}'.format(value, digits + 2)
        else:
            binary = '{:#0{}b}'.format(value, digits)
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
