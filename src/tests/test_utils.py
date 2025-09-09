import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from subsetsumpy.utils import BaseSubsetMethods

basic_set = [1, 5, 2, 3, 6, -2]
binary_subset = [1, 0, 0, 0, 1, 1]


@pytest.fixture()
def base_subset_methods():
    """Creates a fresh instance of BaseSubsetMethods"""
    return BaseSubsetMethods()


@pytest.mark.parametrize("num, expected", [(1, 0), (0, 1)])
def test_invert_binary_number(base_subset_methods, num, expected):
    assert base_subset_methods.invert_binary_number(num) == expected


def test_invert_binary_number_exception(base_subset_methods):

    with pytest.raises(TypeError):
        base_subset_methods.invert_binary_number(binary_number="1")

    with pytest.raises(ValueError):
        base_subset_methods.invert_binary_number(binary_number=2)


def test_convert_to_decimal_format(base_subset_methods):
    binary_subset_test = base_subset_methods.convert_to_decimal_format(
        basic_set, binary_subset
    )
    assert binary_subset_test == [1, 6, -2]


def test_convert_to_decimal_format_exception(base_subset_methods):
    with pytest.raises(TypeError):
        base_subset_methods.convert_to_decimal_format({1, 2, 3}, binary_subset)

    with pytest.raises(TypeError):
        base_subset_methods.convert_to_decimal_format(basic_set, {1, 2, 3})


def test_evaluate_subset(base_subset_methods):
    score = base_subset_methods.evaluate_subset(basic_set, binary_subset, 5)
    assert score == 0


def test_evaluate_subset_exception(base_subset_methods):
    with pytest.raises(TypeError):
        base_subset_methods.evaluate_subset({1, 2, 3, 4, 5, 6}, binary_subset, 5)
    with pytest.raises(TypeError):
        base_subset_methods.evaluate_subset(basic_set, {1, 0, 0, 1, 1, 1}, 5)
    with pytest.raises(TypeError):
        base_subset_methods.evaluate_subset(basic_set, binary_subset, "5")
