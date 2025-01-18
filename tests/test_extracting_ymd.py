from wrangle_in_py.extracting_ymd_hms import extracting_ymd
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

# Test cases
def test_valid_datetime_column():
    """Test function with a valid datetime column containing multiple rows."""
    df = pd.DataFrame({'timestamp': ['2024-01-07 12:30:45', '2023-12-25 08:15:30']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07 12:30:45', '2023-12-25 08:15:30']),
        'timestamp_year': pd.Series([2024, 2023], dtype="Int64"),
        'timestamp_month': pd.Series([1, 12], dtype="Int64"),
        'timestamp_day': pd.Series([7, 25], dtype="Int64")
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_empty_dataframe():
    """Test function with an empty DataFrame."""
    df = pd.DataFrame({'timestamp': pd.Series([], dtype="datetime64[ns]")})
    expected = pd.DataFrame({
        'timestamp': pd.Series([], dtype="datetime64[ns]"),
        'timestamp_year': pd.Series([], dtype="Int64"),
        'timestamp_month': pd.Series([], dtype="Int64"),
        'timestamp_day': pd.Series([], dtype="Int64")
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_single_row_dataframe():
    """Test function with a DataFrame containing a single row."""
    df = pd.DataFrame({'timestamp': ['2024-02-15 10:00:00']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-02-15 10:00:00']),
        'timestamp_year': pd.Series([2024], dtype="Int64"),
        'timestamp_month': pd.Series([2], dtype="Int64"),
        'timestamp_day': pd.Series([15], dtype="Int64")
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_missing_values():
    """Test function with missing (NaT) values in the datetime column."""
    df = pd.DataFrame({'timestamp': ['2024-01-07', None, '2023-12-25']})
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07', None, '2023-12-25']),
        'timestamp_year': pd.Series([2024, pd.NA, 2023], dtype="Int64"),
        'timestamp_month': pd.Series([1, pd.NA, 12], dtype="Int64"),
        'timestamp_day': pd.Series([7, pd.NA, 25], dtype="Int64")
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_non_datetime_column():
    """Test function with a non-datetime column. Expect a TypeError."""
    df = pd.DataFrame({'timestamp': ['not_a_date', 'still_not_a_date']})
    with pytest.raises(TypeError, match="Column 'timestamp' must be of datetime type."):
        extracting_ymd(df, 'timestamp')


def test_missing_column():
    """Test function with a missing column. Expect a KeyError."""
    df = pd.DataFrame({'wrong_column': ['2024-01-01', '2023-12-31']})
    with pytest.raises(KeyError, match="Column 'timestamp' does not exist in the DataFrame"):
        extracting_ymd(df, 'timestamp')


def test_timezone_aware_datetime():
    """Test function with timezone-aware datetime values."""
    df = pd.DataFrame({'timestamp': ['2024-01-07T12:30:45+00:00', '2023-12-25T08:15:30+00:00']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07T12:30:45+00:00', '2023-12-25T08:15:30+00:00']),
        'timestamp_year': pd.Series([2024, 2023], dtype="Int64"),
        'timestamp_month': pd.Series([1, 12], dtype="Int64"),
        'timestamp_day': pd.Series([7, 25], dtype="Int64")
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_unrelated_columns():
    """Test function with additional unrelated columns in the DataFrame."""
    df = pd.DataFrame({'timestamp': ['2024-01-07'], 'name': ['event']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07']),
        'name': ['event'],
        'timestamp_year': pd.Series([2024], dtype="Int64"),
        'timestamp_month': pd.Series([1], dtype="Int64"),
        'timestamp_day': pd.Series([7], dtype="Int64")
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_special_character_column_name():
    """Test function with a column name containing special characters."""
    df = pd.DataFrame({'date/time': ['2024-01-07']})
    df['date/time'] = pd.to_datetime(df['date/time'])
    expected = pd.DataFrame({
        'date/time': pd.to_datetime(['2024-01-07']),
        'date/time_year': pd.Series([2024], dtype="Int64"),
        'date/time_month': pd.Series([1], dtype="Int64"),
        'date/time_day': pd.Series([7], dtype="Int64")
    })
    result = extracting_ymd(df, 'date/time')
    assert_frame_equal(result, expected)


def test_large_dataframe():
    """Test function with a very large DataFrame."""
    df = pd.DataFrame({'timestamp': pd.date_range(start='2024-01-01', periods=1000000, freq='h')})
    result = extracting_ymd(df, 'timestamp')
    assert result.shape == (1000000, 4)  # Ensure the new columns are added
    assert result['timestamp_year'].iloc[0] == 2024
    assert result['timestamp_month'].iloc[-1] == 1  # Dynamically compute the last row's month