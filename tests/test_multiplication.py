import pytest
from pybit.bits import Bits
from pybit.multiplication import Multiplication


def test_booth_primary():
    pass


def test_booth_secondary():
    A1 = Bits.from_dec(0b010111, 6)
    B1 = Bits.from_dec(0b001011, 6)
    assert Multiplication.booth_secondary(A1, B1) == [
        Bits([1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1]),
        Bits([1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0]),
        Bits([0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]),
        Bits([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1])
    ]
    A2 = Bits.from_dec(0b101111, 6)
    B2 = Bits.from_dec(0b011010, 6)
    assert Multiplication.booth_secondary(A2, B2) == [
        Bits([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]),
        Bits([0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]),
        Bits([1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]),
        Bits([1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0])
    ]



def test_booth_tertiary():
    pass


def test_partial_product():
    pass


def test_wallace_tree():
    pass
