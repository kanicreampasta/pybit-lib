import pytest
from lib.radix_convert import RadixConvert


def test_dec_to_bin():
    assert RadixConvert.dec_to_bin(0) == '0b0'
    assert RadixConvert.dec_to_bin(10) == '0b1010'
    assert RadixConvert.dec_to_bin(100) == '0b1100100'
