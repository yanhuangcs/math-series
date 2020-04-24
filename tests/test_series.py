from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


""" unit tests for fibonacci function."""


def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fib_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fib_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fib_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_fib_20():
    actual = fibonacci(20)
    expected = 6765
    assert actual == expected


""" unit tests for lucas function."""


def test_luc_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_luc_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_luc_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_luc_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_luc_20():
    actual = lucas(20)
    expected = 15127
    assert actual == expected


""" unit tests for sum_series function with default parameters same as fibonacci series."""


def test_sumseries_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sumseries_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sumseries_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sumseries_three():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_sumseries_four():
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_sumseries_five():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_sumseries_20():
    actual = sum_series(20)
    expected = 6765
    assert actual == expected


"""unit test for sum_series with input parameters same as lucas series"""


def test_sumseries_zero_luc():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sumseries_luc():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected


def test_sumseries_luc():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected


def test_sumseries_luc():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected


def test_sumseries_luc():
    actual = sum_series(4, 2, 1)
    expected = 7
    assert actual == expected


def test_sumseries_20_luc():
    actual = sum_series(20, 2, 1)
    expected = 15127
    assert actual == expected