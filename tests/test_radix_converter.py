import pytest
from pybit.bits import Bits, BitsError
from pybit.radix_convert import RadixConvert


def test_dec_to_bin():
    assert RadixConvert.dec_to_bin(0) == Bits([0])
    assert RadixConvert.dec_to_bin(10) == Bits([1, 0, 1, 0])
    assert RadixConvert.dec_to_bin(10, 0) == Bits([1, 0, 1, 0])
    assert RadixConvert.dec_to_bin(10, 1) == Bits([0])
    assert RadixConvert.dec_to_bin(10, 2) == Bits([1, 0])
    assert RadixConvert.dec_to_bin(10, 3) == Bits([0, 1, 0])
    assert RadixConvert.dec_to_bin(10, 10) == Bits([0, 0, 0, 0, 0, 0, 1, 0, 1, 0])
    assert RadixConvert.dec_to_bin(100) == Bits([1, 1, 0, 0, 1, 0, 0])
    assert RadixConvert.dec_to_bin(-10, 5) == Bits([1, 0, 1, 1, 0])
    assert RadixConvert.dec_to_bin(-100, 8) == Bits([1, 0, 0, 1, 1, 1, 0, 0])


def test_dec_to_hex():
    assert RadixConvert.dec_to_hex(0) == '0x0'
    assert RadixConvert.dec_to_hex(10) == '0xa'
    assert RadixConvert.dec_to_hex(100) == '0x64'
    assert RadixConvert.dec_to_hex(100, 4) == '0x0064'
    assert RadixConvert.dec_to_hex(2000) == '0x7d0'
    assert RadixConvert.dec_to_hex(-100, 2) == '0x9c'
    assert RadixConvert.dec_to_hex(-100, 4) == '0xff9c'
    assert RadixConvert.dec_to_hex(-100, 8) == '0xffffff9c'
