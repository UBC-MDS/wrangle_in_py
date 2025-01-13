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
        'timestamp_year': [2024, 2023],
        'timestamp_month': [1, 12],
        'timestamp_day': [7, 25]
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_empty_dataframe():
    """Test function with an empty DataFrame."""
    df = pd.DataFrame({'timestamp': []})
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime([]),
        'timestamp_year': [],
        'timestamp_month': [],
        'timestamp_day': []
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_single_row_dataframe():
    """Test function with a DataFrame containing a single row."""
    df = pd.DataFrame({'timestamp': ['2024-02-15 10:00:00']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-02-15 10:00:00']),
        'timestamp_year': [2024],
        'timestamp_month': [2],
        'timestamp_day': [15]
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_missing_values():
    """Test function with missing (NaT) values in the datetime column."""
    df = pd.DataFrame({'timestamp': ['2024-01-07', None, '2023-12-25']})
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07', None, '2023-12-25']),
        'timestamp_year': [2024, None, 2023],
        'timestamp_month': [1, None, 12],
        'timestamp_day': [7, None, 25]
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_non_datetime_column():
    """Test function with a non-datetime column. Expect a TypeError."""
    df = pd.DataFrame({'timestamp': ['not_a_date', 'still_not_a_date']})
    with pytest.raises(TypeError, match="must be of datetime type"):
        extracting_ymd(df, 'timestamp')


def test_missing_column():
    """Test function with a missing column. Expect a KeyError."""
    df = pd.DataFrame({'wrong_column': ['2024-01-01', '2023-12-31']})
    with pytest.raises(KeyError, match="does not exist in the DataFrame"):
        extracting_ymd(df, 'timestamp')


def test_timezone_aware_datetime():
    """Test function with timezone-aware datetime values."""
    df = pd.DataFrame({'timestamp': ['2024-01-07T12:30:45+00:00', '2023-12-25T08:15:30+00:00']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07T12:30:45+00:00', '2023-12-25T08:15:30+00:00']),
        'timestamp_year': [2024, 2023],
        'timestamp_month': [1, 12],
        'timestamp_day': [7, 25]
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
        'timestamp_year': [2024],
        'timestamp_month': [1],
        'timestamp_day': [7]
    })
    result = extracting_ymd(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_special_character_column_name():
    """Test function with a column name containing special characters."""
    df = pd.DataFrame({'date/time': ['2024-01-07']})
    df['date/time'] = pd.to_datetime(df['date/time'])
    expected = pd.DataFrame({
        'date/time': pd.to_datetime(['2024-01-07']),
        'date/time_year': [2024],
        'date/time_month': [1],
        'date/time_day': [7]
    })
    result = extracting_ymd(df, 'date/time')
    assert_frame_equal(result, expected)


def test_large_dataframe():
    """Test function with a very large DataFrame."""
    df = pd.DataFrame({'timestamp': pd.date_range(start='2024-01-01', periods=1000000, freq='H')})
    result = extracting_ymd(df, 'timestamp')
    assert result.shape == (1000000, 4)  # Ensure the new columns are added
    assert result['timestamp_year'].iloc[0] == 2024
    assert result['timestamp_month'].iloc[-1] == 6  # Last row's month in the range