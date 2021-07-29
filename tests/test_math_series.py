from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_version():
    assert __version__ == '0.1.0'

# fibonacci tests

def test_fibonacci_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fibonacci_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fibonacci_ntn():
    for n in range (2,100):
        expected = fibonacci(n-1)+fibonacci(n-2)
        actual = fibonacci(n)
        assert actual == expected

# lucas tests

def test_lucas_zero():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_lucas_one():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_lucas_ntn():
    for m in range (2,100):
        expected = lucas(m-1)+lucas(m-2)
        actual = lucas(m)
        assert actual == expected

# sum_series tests

# def test_sum_series_zero():
#     expected = 0
#     actual = sum_series(0)
#     assert actual == expected

# def test_sum_series_zero_lucas(a=2,b=1):
#     expected = 2
#     actual = sum_series(0 , a ,b)
#     assert actual == expected

# def test_sum_series_one():
#     expected = 1
#     actual = sum_series(1)
#     assert actual == expected

# def test_sum_series_one_lucas(a=2,b=1):
#     expected = 1
#     actual = sum_series(1 , a ,b)
#     assert actual == expected

# def test_sum_series_nth():
#     for z in range(2,100):
#         expected = sum_series(z-1) + sum_series(z-2)
#         actual = sum_series(z)
#         assert actual == expected
