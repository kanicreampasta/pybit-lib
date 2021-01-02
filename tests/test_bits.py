import pytest
from pybit.bits import Bits, BitsOperationError


def test_zero_construct():
    empty = Bits(size=32)
    assert empty == Bits([0 for x in range(32)])
    assert len(empty) == 32

def test_bits_construct_eq():
    one1 = Bits([0, 0, 0, 1], size=4)
    one2 = Bits([0, 0, 0, 1], size=8)
    assert len(one1) == 4
    assert len(one2) == 4
    assert one1 == one2

def test_bits_eq_zero():
    zero1 = Bits(size=4)
    zero2 = Bits(size=4)
    zero3 = Bits(size=8)
    assert zero1 == zero2
    with pytest.raises(BitsOperationError):
        zero2 != zero3
    with pytest.raises(BitsOperationError):
        zero3 != zero1

def test_bits_eq_one():
    one1 = Bits([1, 1, 1, 1])
    one2 = Bits([1, 1, 1, 1])
    one3 = Bits([1, 1, 1, 1, 1, 1])
    assert one1 == one2
    with pytest.raises(BitsOperationError):
        one2 != one3
    with pytest.raises(BitsOperationError):
        one3 != one1

def test_bits_eq_mix():
    mix1 = Bits([1, 0, 1, 0])
    mix2 = Bits([1, 0, 1, 0])
    mix3 = Bits([1, 0, 1, 1])
    assert mix1 == mix2
    assert mix2 != mix3
    assert mix3 != mix1

def test_bits_list_reference():
    lst = [1, 0, 1, 0]
    mix1 = Bits(lst)
    mix2 = Bits(lst)
    assert mix1 == mix2
    lst[3] = 1
    assert mix1 == mix2
    assert mix1 == Bits([1, 0, 1, 1])

def test_bits_and_simple():
    bits1 = Bits([1, 0, 1, 0])
    bits2 = Bits([1, 0, 0, 1])
    assert (bits1 & bits2) == Bits([1, 0, 0, 0])

def test_bits_or_simple():
    bits1 = Bits([1, 0, 1, 0])
    bits2 = Bits([1, 0, 0, 1])
    assert (bits1 | bits2) == Bits([1, 0, 1, 1])

def test_bits_xor_simple():
    bits1 = Bits([1, 0, 1, 0])
    bits2 = Bits([1, 0, 0, 1])
    assert (bits1 ^ bits2) == Bits([0, 0, 1, 1])

def test_bits_inv_simple():
    bits = Bits([1, 0, 1, 0])
    assert ~bits == Bits([0, 1, 0, 1])

def test_bits_and_different_len():
    bits1 = Bits([1, 0, 1, 0])
    bits2 = Bits([1, 0, 0, 1, 0])
    with pytest.raises(BitsOperationError):
        bits1 & bits2

def test_bits_and_different_len():
    bits1 = Bits([1, 0, 1, 0])
    bits2 = Bits([1, 0, 0, 1, 0])
    with pytest.raises(BitsOperationError):
        bits1 | bits2

def test_bits_and_different_len():
    bits1 = Bits([1, 0, 1, 0])
    bits2 = Bits([1, 0, 0, 1, 0])
    with pytest.raises(BitsOperationError):
        bits1 ^ bits2

def test_bits_right_logical_shift():
    bits = Bits([1, 1, 0, 1])
    assert bits >> ('l', 0) == Bits([1, 1, 0, 1])
    assert bits >> ('l', 1) == Bits([0, 1, 1, 0])
    assert bits >> ('l', 2) == Bits([0, 0, 1, 1])
    assert bits >> ('l', 3) == Bits([0, 0, 0, 1])
    assert bits >> ('l', 4) == Bits([0, 0, 0, 0])
    assert bits >> ('l', 5) == Bits([0, 0, 0, 0])

def test_bits_left_logical_shift():
    bits = Bits([1, 1, 0, 1])
    assert bits << ('l', 0) == Bits([1, 1, 0, 1])
    assert bits << ('l', 1) == Bits([1, 0, 1, 0])
    assert bits << ('l', 2) == Bits([0, 1, 0, 0])
    assert bits << ('l', 3) == Bits([1, 0, 0, 0])
    assert bits << ('l', 4) == Bits([0, 0, 0, 0])
    assert bits << ('l', 5) == Bits([0, 0, 0, 0])

def test_bits_right_arithmetic_shift():
    bits = Bits([1, 1, 0, 1])
    bits2 = Bits([1, 0, 1, 1, 0, 0])
    assert bits >> ('a', 0) == Bits([1, 1, 0, 1])
    assert bits >> ('a', 1) == Bits([1, 1, 1, 0])
    assert bits >> ('a', 2) == Bits([1, 1, 1, 1])
    assert bits >> ('a', 3) == Bits([1, 1, 1, 1])
    assert bits >> ('a', 4) == Bits([1, 1, 1, 1])
    assert bits2 >> ('a', 1) == Bits([1, 1, 0, 1, 1, 0])
    assert bits2 >> ('a', 2) == Bits([1, 1, 1, 0, 1, 1])
    assert bits2 >> ('a', 3) == Bits([1, 1, 1, 1, 0, 1])

def test_bits_left_arithmetic_shift():
    bits = Bits([1, 1, 0, 1])
    bits2 = Bits([1, 0, 1, 1, 0, 0])
    assert bits << ('a', 0) == Bits([1, 1, 0, 1])
    assert bits << ('a', 1) == Bits([1, 0, 1, 0])
    assert bits << ('a', 2) == Bits([1, 1, 0, 0])
    assert bits << ('a', 3) == Bits([1, 0, 0, 0])
    assert bits << ('a', 4) == Bits([1, 0, 0, 0])
    assert bits << ('a', 5) == Bits([1, 0, 0, 0])
    assert bits2 << ('a', 1) == Bits([1, 1, 1, 0, 0, 0])
    assert bits2 << ('a', 2) == Bits([1, 1, 0, 0, 0, 0])
    assert bits2 << ('a', 3) == Bits([1, 0, 0, 0, 0, 0])
    assert Bits([1, 1, 1, 0, 1, 1, 0, 0]) << ('a', 2) == Bits([1, 0, 1, 1, 0, 0, 0, 0])
