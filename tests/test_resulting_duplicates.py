import pytest
from wrangle_in_py.column_standardizer import resulting_duplicates

# expected cases
def test_no_duplicates():
    """
    `resulting_duplicates` should return an empty dictionary if there are
    no duplicates in the list of standardized strings.
    """
    original = ['!!Durian..', '_Jack_fruit!', 'pineAppLES']
    standardized = ['__durian__', '_jack_fruit_', 'pineapples']
    assert resulting_duplicates(original, standardized) == {}

def test_with_duplicates():
    """
    `resulting_duplicates` should return a dictionary where the keys are
    the standardized strings with duplicate(s), and the values are lists of
    the original strings that map to them.
    """
    original = ['Jack Fruit 88', 'Jack! Fruit! 88!', 'PINEAPPLES']
    standardized = ['jack_fruit_88', 'jack_fruit_88', 'pineapples']
    expected = {'jack_fruit_88': ['Jack Fruit 88', 'Jack! Fruit! 88!']}
    assert resulting_duplicates(original, standardized) == expected

# edge cases
def test_edge_case_empty_lists():
    """
    `resulting_duplicates` should return an empty dictionary if the inputs
    are empty lists.
    """
    assert resulting_duplicates([], []) == {}

def test_edge_case_only_duplicates():
    """
    `resulting_duplicates` should return a dictionary where the keys are
    the standardized strings with duplicate(s), and the values are lists of
    the original strings that map to them.
    In this case, all of the standardized strings are duplicates.
    """
    original = ['MangO', 'MANGO', 'mANGo']
    standardized = ['mango', 'mango', 'mango']
    expected = {'mango': ['MangO', 'MANGO', 'mANGo']}
    assert resulting_duplicates(original, standardized) == expected

# error cases
def test_error_different_lengths():
    """
    `resulting_duplicates` should raise a ValueError if the inputted
    lists of strings are not of the same length.
    """
    original_1 = ['MANGO', 'Dragon! Fruit!']
    standardized_1 = ['mango']

    original_2 = ['MANGO']
    standardized_2 = ['mango', 'dragon fruit']

    with pytest.raises(ValueError, match="Both inputs must be of the same length."):
        resulting_duplicates(original_1, standardized_1)
    with pytest.raises(ValueError, match="Both inputs must be of the same length."):
        resulting_duplicates(original_2, standardized_2)


def test_error_wrong_type():
    """
    `resulting_duplicates` should raise a TypeError if any of the inputs
    are not a list of strings.
    """
    with pytest.raises(TypeError):
        resulting_duplicates('not a list', ['jack fruit'])
        resulting_duplicates(['jack fruit'], 'not a list')
        resulting_duplicates('not a list', 'not a list')
        resulting_duplicates(2025, ['mango'])
        resulting_duplicates(['mango'], 2025)
        resulting_duplicates(False, True)
