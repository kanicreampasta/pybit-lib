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

class TestExtension:
    def setup_method(self, method):
        self.bits1 = Bits([0, 1, 0, 1])
        self.bits2 = Bits([1, 1, 0, 1])
        self.bits1_ref = Bits([0, 1, 0, 1])
        self.bits2_ref = Bits([1, 1, 0, 1])
    
    def _check_modify(self):
        assert self.bits1 == self.bits1_ref
        assert self.bits2 == self.bits2_ref

    def test_bits_zero_extension(self):
        assert self.bits1.zero_extend(size=8) == Bits([0, 0, 0, 0, 0, 1, 0, 1])
        assert self.bits2.zero_extend(size=8) == Bits([0, 0, 0, 0, 1, 1, 0, 1])
        self._check_modify()

    def test_bits_sign_extension(self):
        assert self.bits1.sign_extend(size=8) == Bits([0, 0, 0, 0, 0, 1, 0, 1])
        assert self.bits2.sign_extend(size=8) == Bits([1, 1, 1, 1, 1, 1, 0, 1])
        self._check_modify()

    def test_bits_zero_extension_same(self):
        assert self.bits1.zero_extend(size=4) == Bits([0, 1, 0, 1])
        assert self.bits2.zero_extend(size=4) == Bits([1, 1, 0, 1])
        self._check_modify()
    
    def test_bits_sign_extension_same(self):
        assert self.bits1.sign_extend(size=4) == Bits([0, 1, 0, 1])
        assert self.bits2.sign_extend(size=4) == Bits([1, 1, 0, 1])
        self._check_modify()
    
    def test_bits_zero_extension_shrink(self):
        assert self.bits1.zero_extend(size=3) == Bits([1, 0, 1])
        assert self.bits2.zero_extend(size=3) == Bits([1, 0, 1])
        self._check_modify()
    
    def test_bits_sign_extension_shrink(self):
        assert self.bits1.sign_extend(size=3) == Bits([1, 0, 1])
        assert self.bits2.sign_extend(size=3) == Bits([1, 0, 1])
        self._check_modify()


class TestToBits:

    def test_from_dec_positive(self):
        assert Bits.from_dec(0) == Bits([0])
        assert Bits.from_dec(0,1) == Bits([0])
        assert Bits.from_dec(1,1) == Bits([1])
        assert Bits.from_dec(10) == Bits([1, 0, 1, 0])
        assert Bits.from_dec(10, 1) == Bits([0])
        assert Bits.from_dec(10, 2) == Bits([1, 0])
        assert Bits.from_dec(10, 3) == Bits([0, 1, 0])
        assert Bits.from_dec(10, 10) == Bits([0, 0, 0, 0, 0, 0, 1, 0, 1, 0])
        assert Bits.from_dec(100) == Bits([1, 1, 0, 0, 1, 0, 0])

    def test_from_dec_negative(self):
        assert Bits.from_dec(-1) == Bits([1])
        assert Bits.from_dec(-1, 1) == Bits([1])
        assert Bits.from_dec(-1, 5) == Bits([1, 1, 1, 1, 1])
        assert Bits.from_dec(-10) == Bits([1, 0, 1, 1, 0])
        assert Bits.from_dec(-10, 5) == Bits([1, 0, 1, 1, 0])
        assert Bits.from_dec(-10, 10) == Bits([1, 1, 1, 1, 1, 1, 0, 1, 1, 0])
        assert Bits.from_dec(-100, 8) == Bits([1, 0, 0, 1, 1, 1, 0, 0])
        assert Bits.from_dec(-255) == Bits([1, 0, 0, 0, 0, 0, 0, 0, 1])

    def test_from_hex(self):
        assert Bits.from_hex(0x0) == Bits([0, 0, 0, 0])
        assert Bits.from_hex(0x0, 1) == Bits([0])
        assert Bits.from_hex(0x0, 2) == Bits([0, 0])
        assert Bits.from_hex(0xa) == Bits([1, 0, 1, 0])
        assert Bits.from_hex(0x48) == Bits([0, 1, 0, 0, 1, 0, 0, 0])
        assert Bits.from_hex(0x100) == Bits([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        assert Bits.from_hex(0xffff) == Bits([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        assert Bits.from_hex(0x0a, 6) == Bits([0, 0, 1, 0, 1, 0])
        assert Bits.from_hex(0xa, 8) == Bits([0, 0, 0, 0, 1, 0, 1, 0])
        assert Bits.from_hex(0x0a, 8) == Bits([0, 0, 0, 0, 1, 0, 1, 0])


class TestAdd:
    def test_no_carry(self):
        assert Bits([0, 0, 0]) + Bits([0, 0, 0]) == Bits([0, 0, 0])
        assert Bits([0, 1, 0, 1]) + Bits([1, 0, 1, 0]) == Bits([1, 1, 1, 1])
        assert Bits([1, 0, 1, 0]) + Bits([0, 1, 0, 1]) == Bits([1, 1, 1, 1])

    def test_no_carry_extend(self):
        assert Bits([0]) + Bits([0, 0, 0]) == Bits([0, 0, 0])
        assert Bits([0, 0, 0]) + Bits([0]) == Bits([0, 0, 0])
        assert Bits([0, 0, 0]) + Bits([1, 1]) == Bits([0, 1, 1])
        assert Bits([1, 0, 0]) + Bits([0, 0, 0, 0]) == Bits([0, 1, 0, 0])

    def test_has_carry(self):
        assert Bits([0, 0, 0, 1]) + Bits([0, 0, 0, 1]) == Bits([0, 0, 1, 0])
        assert Bits([0, 0, 1, 1]) + Bits([0, 0, 0, 1]) == Bits([0, 1, 0, 0])

    def test_has_carry_overflow(self):
        assert Bits([1]) + Bits([1]) == Bits([1, 0])
        assert Bits([1, 1, 1, 1]) + Bits([0, 0, 0, 1]) == Bits([1, 0, 0, 0, 0])
        assert Bits([0, 0, 0, 1]) + Bits([1, 1, 1, 1]) == Bits([1, 0, 0, 0, 0])
        assert Bits([1, 0, 1, 1]) + Bits([1, 1, 0, 1]) == Bits([1, 1, 0, 0, 0])

    def test_has_carry_extend(self):
        assert Bits([1, 0, 1, 1]) + Bits([1]) == Bits([1, 1, 0, 0])
        assert Bits([1]) + Bits([1, 0, 1, 1]) == Bits([1, 1, 0, 0])
        assert Bits([1, 0, 1]) + Bits([1, 0, 0, 1]) == Bits([1, 1, 1, 0])

    def test_has_carry_extend_overflow(self):
        assert Bits([1, 1, 1, 1]) + Bits([1]) == Bits([1, 0, 0, 0, 0])
        assert Bits([1]) + Bits([1, 1, 1, 1]) == Bits([1, 0, 0, 0, 0])

    def test_multiple_addition(self):
        assert Bits([0, 0]) + Bits([0, 0, 0]) + Bits([0, 0, 0, 0]) == Bits([0, 0, 0, 0])
        assert Bits([0, 0]) + Bits([0, 0, 0]) + Bits([0, 0]) == Bits([0, 0, 0])
        assert Bits([1, 0]) + Bits([1, 0, 0]) + Bits([0, 1, 1]) == Bits([1, 0, 0, 1])
        assert Bits([1, 1, 1, 1]) + Bits([1, 1, 1, 1]) + Bits([1, 1, 1, 1]) == Bits([1, 0, 1, 1, 0, 1])
