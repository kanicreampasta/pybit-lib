import pytest
from pybit.radix_convert import RadixConvert


def test_dec_to_bin():
    assert RadixConvert.dec_to_bin(0) == '0b0'
    assert RadixConvert.dec_to_bin(10) == '0b1010'
    assert RadixConvert.dec_to_bin(10,10) == '0b0000001010'
    assert RadixConvert.dec_to_bin(100) == '0b1100100'
    assert RadixConvert.dec_to_bin(-10,5) == '0b10110'
    assert RadixConvert.dec_to_bin(-100,8) == '0b10011100'


def test_dec_to_hex():
    assert RadixConvert.dec_to_hex(0) == '0x0'
    assert RadixConvert.dec_to_hex(10) == '0xa'
    assert RadixConvert.dec_to_hex(100) == '0x64'
