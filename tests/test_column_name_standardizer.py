import pytest
import pandas as pd
import warnings
from wrangle_in_py.column_name_standardizer import column_name_standardizer, resulting_duplicates, string_standardizer

# expected cases
def test_expected_cases():
    """
    `column_name_standardizer` should convert column names to lowercase and
    non-alphanumerics (including spaces and punctuation) should be replaced
    with underscores. The resulting dataframe should be a pandas DataFrame and
    its shape should be the same as the shape of the input dataframe.
    """
    df = pd.DataFrame({
        'Jack Fruit 88': [1, 2],
        'PINE-APPLES': [3, 4]
    })
    standardized_df = column_name_standardizer(df)
    assert standardized_df.columns.tolist() == ['jack_fruit_88', 'pine_apples']
    assert isinstance(standardized_df, pd.DataFrame)
    assert standardized_df.shape == df.shape

# edge cases
def test_edge_case_no_standardization_needed():
    """
    `column_name_standardizer` should return a dataframe that is the same as the input
    dataframe if the input dataframe's column names are all in lowercase and doesn't 
    contain any non-alphanumerics besides underscores. The resulting dataframe should be a pandas DataFrame and
    its shape should be the same as the shape of the input dataframe.
    """
    df = pd.DataFrame({
        'durian_': [1, 2],
        '_mangosteen': [3, 4]
    })
    standardized_df = column_name_standardizer(df)
    assert standardized_df.columns.tolist() == ['durian_', '_mangosteen']
    assert isinstance(standardized_df, pd.DataFrame)
    assert standardized_df.shape == df.shape

def test_edge_case_empty_dataframe():
    """
    `column_name_standardizer` should return an empty dataframe if the input is
    an empty dataframe.
    """
    df = pd.DataFrame()
    standardized_df = column_name_standardizer(df)
    assert standardized_df.empty
    assert standardized_df.shape == (0, 0)

def test_edge_case_numeric_column_names():
    """
    `column_name_standardizer` should return a dataframe that is the same as the input
    dataframe if the input dataframe's column names are numeric strings. The resulting dataframe should be a pandas DataFrame and
    its shape should be the same as the shape of the input dataframe.
    """
    df = pd.DataFrame({
        '2025': [1, 2],
        '2024': [3, 4]
    })
    standardized_df = column_name_standardizer(df)
    assert standardized_df.columns.tolist() == ['2025', '2024']
    assert isinstance(standardized_df, pd.DataFrame)
    assert standardized_df.shape == df.shape


def test_warning_on_duplicates():
    """
    `column_name_standardizer` should raise a warning if after standardization,
    some column names are duplicates.
    """
    df = pd.DataFrame({
        'mango!': [1, 2],
        'Mango.': [3, 4]
    })
    with pytest.warns(UserWarning):
        column_name_standardizer(df)

# error cases
def test_error_wrong_type():
    """
    `column_name_standardizer` should raise a TypeError if the input is not a
    pandas DataFrame.
    """
    with pytest.raises(TypeError):
        column_name_standardizer("Not a dataframe")
    with pytest.raises(TypeError):
        column_name_standardizer([1, 2, 3])
