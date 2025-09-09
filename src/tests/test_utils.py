import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from subsetsumpy.utils import BaseSubsetMethods



@pytest.fixture()
def base_subset_methods():
    """Creates a fresh instance of BaseSubsetMethods"""
    return BaseSubsetMethods()

@pytest.mark.parametrize("num, expected",[
    (1,0),
    (0,1)
])
def test_invert_binary_number(base_subset_methods, num, expected):
    assert base_subset_methods.invert_binary_number(num) == expected



def test_invert_binary_number_exception(base_subset_methods):

    with pytest.raises(TypeError):
        base_subset_methods.invert_binary_number(binary_number="1")

    with pytest.raises(ValueError):
        base_subset_methods.invert_binary_number(binary_number=2)

