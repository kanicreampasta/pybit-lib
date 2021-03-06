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


def test_CLA():
    A1 = Bits([1, 0, 1, 1, 1, 1, 0, 1])
    B1 = Bits([1, 0, 1, 0, 1, 1, 1, 1])
    assert Multiplication.CLA(A1, B1, 0, size=8) == [
        Bits([0, 0, 0, 1, 0, 0, 1, 0]),
        Bits([1, 0, 1, 0, 1, 1, 0, 1]),
        Bits([1, 0, 1, 1, 1, 1, 1, 1]),
        Bits([0, 1, 1, 0, 1, 1, 0, 0])
    ]

    A2 = Bits([0, 1, 0, 1, 1, 0, 1, 0])
    B2 = Bits([1, 0, 1, 1, 1, 0, 0, 0])
    assert Multiplication.CLA(A2, B2, 0, size=8) == [
        Bits([1, 1, 1, 0, 0, 0, 1, 0]),
        Bits([0, 0, 0, 1, 1, 0, 0, 0]),
        Bits([1, 1, 1, 1, 1, 0, 0, 0]),
        Bits([0, 0, 0, 1, 0, 0, 1, 0])
    ]

    A3 = Bits([0, 1, 1, 1, 1, 0, 1, 0])
    B3 = Bits([1, 0, 1, 1, 1, 0, 1, 1])
    assert Multiplication.CLA(A3, B3, 0, size=8) == [
        Bits([1, 1, 0, 0, 0, 0, 0, 1]),
        Bits([0, 0, 1, 1, 1, 0, 1, 0]),
        Bits([1, 1, 1, 1, 1, 0, 1, 0]),
        Bits([0, 0, 1, 1, 0, 1, 0, 1])
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


def test_RCA():
    A1 = Bits([1, 1, 0, 1, 0, 0, 1, 0])
    B1 = Bits([1, 1, 1, 0, 0, 1, 0, 1])
    assert Multiplication.RCA(A1, B1, 1, size=8) == [
        Bits([1, 0, 1, 1, 1, 0, 0, 0]),
        Bits([1, 1, 0, 0, 0, 1, 1, 1])
    ]
    A2 = Bits([1, 0, 1, 1, 1, 0, 0, 0])
    B2 = Bits([1, 1, 1, 0, 1, 1, 0, 0])
    assert Multiplication.RCA(A2, B2, 0, size=8) == [
        Bits([1, 0, 1, 0, 0, 1, 0, 0]),
        Bits([1, 1, 1, 1, 1, 0, 0, 0])
    ]


def test_partial_product():
    A1 = Bits([0, 1, 1, 0, 1, 1])
    B1 = Bits([0, 1, 1, 1, 0, 1])
    assert Multiplication.partial_product(A1, B1, size=6) == [
        Bits([0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]),
        Bits([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        Bits([0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0]),
        Bits([0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]),
        Bits([0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]),
        Bits([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ]
    A2 = Bits([1, 0, 1, 1, 1, 1])
    B2 = Bits([0, 1, 1, 0, 1, 0])
    assert Multiplication.partial_product(A2, B2, size=6) == [
        Bits([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        Bits([1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]),
        Bits([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        Bits([1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0]),
        Bits([1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0]),
        Bits([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ]


def test_wallace_tree():
    A1 = Bits([0, 1, 1, 0, 1, 1])
    B1 = Bits([0, 1, 1, 1, 0, 1])
    assert Multiplication.wallace_tree(A1, B1, size=6) == Bits([0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1])
    A2 = Bits([1, 0, 1, 1, 1, 1])
    B2 = Bits([0, 1, 1, 0, 1, 0])
    assert Multiplication.wallace_tree(A2, B2, size=6) == Bits([1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0])
