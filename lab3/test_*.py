import pytest
from lab3 import (
    sum_recursive,
    sum_nested_iterative,
    seq_recursive,
    seq_iterative,
)

# --- SUM TESTS ---

@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], 6),
    ([1, [2, 3]], 6),
    ([1, [2, [3, 4, [5]]]], 15),
    ([], 0),
])
def test_sum_recursive(data, expected):
    assert sum_recursive(data) == expected

@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], 6),
    ([1, [2, 3]], 6),
    ([1, [2, [3, 4, [5]]]], 15),
    ([], 0),
])
def test_sum_iterative(data, expected):
    assert sum_nested_iterative(data) == expected

def test_sum_both_equal():
    data = [1, [2, [3, 4, [5]]]]
    assert sum_recursive(data) == sum_nested_iterative(data)

# --- SEQUENCE TESTS ---

def test_seq_base_case():
    assert seq_recursive(1) == (1, 1)
    assert seq_iterative(1) == (1, 1)

@pytest.mark.parametrize("k", [2, 3, 5, 10])
def test_seq_recursive_vs_iterative(k):
    a1, b1 = seq_recursive(k)
    a2, b2 = seq_iterative(k)

    assert a1 == pytest.approx(a2, rel=1e-9)
    assert b1 == pytest.approx(b2, rel=1e-9)

def test_seq_known_value():
    a, b = seq_iterative(5)

    assert a == pytest.approx(1.0)
    assert b == pytest.approx(1.0)