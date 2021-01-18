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
    A1 = Bits.from_dec(0b101111, 6)
    B1 = Bits.from_dec(0b011010, 6)
    assert Multiplication.booth_tertiary(A1, B1) == [
        Bits([1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]),
        Bits([1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0]),
        Bits([1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0])
    ]

    A2 = Bits.from_dec(0b101111, 6)
    B2 = Bits.from_dec(0b110010, 6)
    assert Multiplication.booth_tertiary(A2, B2) == [
        Bits([1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]),
        Bits([0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]),
        Bits([0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0])
    ]

def test_CSA():
    X1 = Bits([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Y1 = Bits([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0])
    Z1 = Bits([1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0])
    assert Multiplication.CSA(X1, Y1, Z1, size=12) == [
        Bits([1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]),
        Bits([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    ]
    X2 = Bits([0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
    Y2 = Bits([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    Z2 = Bits([1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0])
    assert Multiplication.CSA(X2, Y2, Z2, size=12) == [
        Bits([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]),
        Bits([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    ]
    X3 = Bits([1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0])
    Y3 = Bits([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    Z3 = Bits([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0])
    assert Multiplication.CSA(X3, Y3, Z3, size=12) == [
        Bits([0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0]),
        Bits([1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0])
    ]
    X4 = Bits([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    Y4 = Bits([0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0])
    Z4 = Bits([1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0])
    assert Multiplication.CSA(X4, Y4, Z4, size=12) == [
        Bits([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]),
        Bits([0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0])
    ]


def test_partial_product():
    pass


def test_wallace_tree():
    pass
