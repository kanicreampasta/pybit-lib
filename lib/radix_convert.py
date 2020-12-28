class RadixConvert:

    @staticmethod
    def dec_to_bin(value: int) -> str:
        """
        Convert decimal number to binary.
        TODO: allow negative decimal
        :param value: (int) Decimal number.
        :return: (str) Binary number
        """
        return bin(value)

    @staticmethod
    def dec_to_hex(value: int) -> str:
        """
        Convert decimal number to hexadecimal number.
        TODO: allow negative decimal
        :param value: (int) Decimal number.
        :return: (str) Hexadecimal number
        """
        return hex(value)
