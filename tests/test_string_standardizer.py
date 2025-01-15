import pytest
from wrangle_in_py.column_standardizer import string_standardizer

# expected cases
def test_expected_cases():
    """
    `string_standardizer` should convert the inputted string to lowercase and
    non-alphanumerics (including spaces and punctuation) should be replaced
    with underscores
    """
    assert string_standardizer('Jack Fruit 88') == 'jack_fruit_88'
    assert string_standardizer('PINEAPPLES') == 'pineapples'
    assert string_standardizer('Dragon (Fruit)') == 'dragon__fruit_'
    assert string_standardizer('Mango@Steen!') == 'mango_steen_'

# edge cases
def test_edge_case_no_standardization_needed():
    """
    `string_standardizer` should return an identical string to the input
    if the input is in all lowercase and doesn't contain any non-alpahnumerics
    besides underscores.
    """
    assert string_standardizer('durian') == 'durian'
    assert string_standardizer('_longan_') == '_longan_'

def test_edge_case_empty_string():
    """
    `string_standardizer` should return an empty string if the input
    is an empty string
    """
    assert string_standardizer('') == ''

# error cases
def test_error_wrong_type():
    """
    `string_standardizer` should raise a TypeError if the input is
    not a string.
    """
    with pytest.raises(TypeError):
        string_standardizer(12345)
        string_standardizer(None)
        string_standardizer(['list', 'of', 'strings'])