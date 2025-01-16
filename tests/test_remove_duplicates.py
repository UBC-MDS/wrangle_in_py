from wrangle_in_py.remove_duplicates import remove_duplicates
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

def test_remove_duplicates_single_column():
    """Test removing duplicates based on a single column."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'])
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_all_columns():
    """Test removing duplicates based on all columns."""
    data = {'A': [1, 2, 2], 'B': [5, 6, 6]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df)
    expected = pd.DataFrame({'A': [1, 2], 'B': [5, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_keep_last():
    """Test keeping the last occurrence of duplicates."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 7, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'], keep='last')
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 7, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_keep_last_all_columns():
    """Test keeping the last occurrence of duplicates across all columns."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, keep='last')
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_remove_duplicates_drop_all():
    """Test dropping all duplicates."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'], keep=False)
    expected = pd.DataFrame({'A': [1, 4], 'B': [5, 8]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_no_duplicates_print(capsys):
    """Test DataFrame with no duplicates."""
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = remove_duplicates(df)
    expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    # Capture print output
    captured = capsys.readouterr()
    assert "0 rows have been dropped." in captured.out

def test_remove_duplicates_empty_dataframe(capsys):
    """Test handling of an empty DataFrame."""
    df = pd.DataFrame(columns=['A', 'B'])
    result = remove_duplicates(df)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), df)

    # Verify print output
    captured = capsys.readouterr()
    assert "0 rows have been dropped." in captured.out

def test_all_identical_rows_print(capsys):
    """Test DataFrame where all rows are identical."""
    df = pd.DataFrame({'A': [1, 1, 1], 'B': [2, 2, 2]})
    result = remove_duplicates(df)
    expected = pd.DataFrame({'A': [1], 'B': [2]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    # Capture print output
    captured = capsys.readouterr()
    assert "2 rows have been dropped." in captured.out

def test_remove_duplicates_invalid_input_type():
    """Test handling of invalid input type."""
    try:
        remove_duplicates([1, 2, 3])
    except ValueError as e:
        assert str(e) == "Input must be a pandas DataFrame"

def test_remove_duplicates_invalid_column():
    """Test handling of invalid column name."""
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    try:
        remove_duplicates(df, subset_columns=['C'])
    except ValueError as e:
        assert str(e) == "Some columns in subset_columns are not present in the DataFrame"

def test_remove_duplicates_print_dropped_rows(capsys):
    """Test ."""
    df = pd.DataFrame({'A': [1, 1, 2, 3], 'B': [4, 4, 5, 6]})
    result = remove_duplicates(df, subset_columns=['A'], keep='first')
    expected = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    
    # Capture print output
    captured = capsys.readouterr()
    assert "1 rows have been dropped." in captured.out

def test_duplicates_in_non_subset_columns():
    """Test duplicates in columns not included in subset_columns are ignored."""
    data = {'A': [1, 2, 2, 4], 'B': [5, 6, 7, 6]}
    df = pd.DataFrame(data)
    result = remove_duplicates(df, subset_columns=['A'])
    expected = pd.DataFrame({'A': [1, 2, 4], 'B': [5, 6, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)



