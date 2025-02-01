from wrangle_in_py.remove_duplicates import remove_duplicates
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

def test_remove_duplicates_single_column():
    """Test that duplicates are removed based on a single column, keeping the first occurrence.
    Rows where the value in column 'A' is duplicated should retain the first occurrence only."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'])
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_all_columns():
    """Test that duplicates are removed based on all columns, keeping the first occurrence.
    Only fully identical rows should be removed."""
    data = {'A': [1, 2, 2], 'B': [5, 6, 6]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df)
    expected = pd.DataFrame({'A': [1, 2], 'B': [5, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_keep_last():
    """Test that the last occurrence of duplicates is retained when keep='last'.
    The last occurrence of duplicate values in column 'A' should be kept."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 7, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'], keep='last')
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 7, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_keep_last_all_columns():
    """Test that the last occurrence of duplicates across all columns is retained.
    Only fully identical rows should be considered duplicates."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, keep='last')
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_drop_all():
    """Test that all duplicates are removed when keep=False.
    Any row with duplicate values in column 'A' should be completely removed."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'], keep=False)
    expected = pd.DataFrame({'A': [1, 4], 'B': [5, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_no_duplicates_print(capsys):
    """Test that a DataFrame with no duplicates remains unchanged and prints correct message.
    No rows should be removed, and the function should print '0 rows have been dropped.'"""
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = remove_duplicates(df)
    expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    # Capture print output
    captured = capsys.readouterr()
    assert "0 rows have been dropped." in captured.out

def test_remove_duplicates_empty_dataframe(capsys):
    """Test that an empty DataFrame remains unchanged and prints correct message."""
    df = pd.DataFrame(columns=['A', 'B'])
    result = remove_duplicates(df)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), df)

    # Verify print output
    captured = capsys.readouterr()
    assert "0 rows have been dropped." in captured.out

def test_all_identical_rows_print(capsys):
    """Test DataFrame where all rows are identical.
    Expectation: Only one unique row should remain, and the function should print the number of rows dropped."""
    df = pd.DataFrame({'A': [1, 1, 1], 'B': [2, 2, 2]})
    result = remove_duplicates(df)
    expected = pd.DataFrame({'A': [1], 'B': [2]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    # Capture print output
    captured = capsys.readouterr()
    assert "2 rows have been dropped." in captured.out

def test_remove_duplicates_invalid_input_type():
    """Test handling of invalid input type.
    Expectation: Function should raise a ValueError if input is not a pandas DataFrame."""
    try:
        remove_duplicates([1, 2, 3])
    except ValueError as e:
        assert str(e) == "Input must be a pandas DataFrame"

def test_remove_duplicates_invalid_column():
    """Test handling of invalid column name.
    Expectation: Function should raise a ValueError if subset_columns contain a non-existent column."""
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    try:
        remove_duplicates(df, subset_columns=['C'])
    except ValueError as e:
        assert str(e) == "Some columns in subset_columns are not present in the DataFrame"

def test_invalid_keep_parameter():
    """Test handling of invalid keep parameter.
    Expectation: Function should raise a ValueError if keep is not 'first', 'last', or False."""
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(ValueError, match="Invalid value for 'keep'. Must be 'first', 'last', or False."):
        remove_duplicates(df, keep='invalid_option')

def test_remove_duplicates_no_subset():
    """Test removing duplicates with subset_columns=None.
    Expectation: Should behave as if all columns were specified, removing duplicate rows entirely."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=None)
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_print_dropped_rows(capsys):
    """This test verifies that the function correctly removes duplicate rows 
    based on the specified subset of columns and prints the number of dropped rows."""
    df = pd.DataFrame({'A': [1, 1, 2, 3], 'B': [4, 4, 5, 6]})
    result = remove_duplicates(df, subset_columns=['A'], keep='first')
    expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    # Capture print output
    captured = capsys.readouterr()
    assert "1 rows have been dropped." in captured.out

def test_duplicates_in_non_subset_columns():
    """Test handling of duplicates in columns that are not part of subset_columns.
    Expectation: Only the specified subset_columns should be considered when removing duplicates."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 7, 6]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'])
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_multiple_columns():
    """Test removing duplicates based on multiple columns.
    Expectation: Rows are considered duplicates only if they match in all specified columns."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8], 'C': [9, 10, 10, 11]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A', 'B'])
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 8], 'C': [9, 10, 11]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_mixed_columns():
    """Test removing duplicates when columns have mixed data types.
    Expectation: The function should correctly handle different data types when identifying duplicates."""
    data = {'A': ['apple', 'banana', 'apple'], 'B': [1, 2, 1]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'])
    expected = pd.DataFrame({'A': ['apple', 'banana'], 'B': [1, 2]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_large_dataframe():
    """Test removing duplicates from a large DataFrame.
    Expectation: The function should efficiently handle large data sets and remove duplicates correctly."""
    data = {'A': list(range(1000)) * 2, 'B': list(range(2000))}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'])
    expected = pd.DataFrame({'A': list(range(1000)), 'B': list(range(1000))})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

