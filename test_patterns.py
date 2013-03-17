import pytest
from patterns import patterns


def test_const():
    @patterns
    def const():
        if 1: 'int'
        if 'hi': 'str'
        if [1, 2]: 'list'
        if (1, 2): 'tuple'

    assert const(1) == 'int'
    assert const('hi') == 'str'
    assert const([1, 2]) == 'list'
    assert const((1, 2)) == 'tuple'
    with pytest.raises(Mismatch): const(2)
    with pytest.raises(Mismatch): const({})


def test_global_ref():
    @patterns
    def _global():
        if '': test_global_ref

    assert _global('') is test_global_ref


def test_local_ref():
    local_var = object()

    @patterns
    def _local():
        if '': local_var

    assert _local('') is local_var
    local_var = object()
    assert _local('') is local_var


def test_capture():
    @patterns
    def capture():
        if y: y - 1

    assert capture(41) == 40


def test_typing():
    @patterns
    def typing():
        if n is int: n + 1
        if s is (str, float): 'str_or_float'

    assert typing(42) == 43
    assert typing('42') == 'str_or_float'
    assert typing(3.14) == 'str_or_float'


def test_destruct_tuple():
    @patterns
    def destruct():
        if (x, 0): 0
        if (x, 1): x
        if (x, y): x + destruct((x, y - 1))
        if (_,): raise ValueError('Give me pair')

    assert destruct((2, 0)) == 0
    assert destruct((2, 1)) == 2
    assert destruct((2, 2)) == 4
    assert destruct((5, 5)) == 25
    with pytest.raises(ValueError): destruct(2)

def test_inserted_destruct_tuple():
    @patterns
    def destruct():
        if (1, (1,2)): 3
        if (x, (1,(y))): x + y
        if ((1,2,3), (1,2,3), x): x

    assert destruct((1, (1,2))) == 3
    assert destruct((11, (1,(11)))) == 22
    assert destruct(((1,2,3), (1,2,3),(1,2,(1,10)))) == (1,2,(1,10))
#
#
# def test_factorial():
#     @patterns
#     def factorial():
#         if 0: 1
#         if n is int: n * factorial(n-1)
#         if []: []
#         if [x] + xs: [factorial(x)] + factorial(xs)
#         if {'n': n, 'f': f}: f(factorial(n))
#
#     assert factorial(0) == 1
#     assert factorial(5) == 120
#     assert factorial([3,4,2]) == [6, 24, 2]
#     assert factorial({'n': [5, 1], 'f': sum}) == 121
