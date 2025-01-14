from wrangle_in_py.extracting_ymd_hms import extracting_hms
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal


# Test cases for extracting_hms
def test_valid_datetime_column():
    """Test function with a valid datetime column containing multiple rows."""
    df = pd.DataFrame({'timestamp': ['2024-01-07 12:30:45', '2023-12-25 08:15:30']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07 12:30:45', '2023-12-25 08:15:30']),
        'timestamp_hour': pd.Series([12, 8], dtype="Int64"),
        'timestamp_minute': pd.Series([30, 15], dtype="Int64"),
        'timestamp_second': pd.Series([45, 30], dtype="Int64")
    })
    result = extracting_hms(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_empty_dataframe():
    """Test function with an empty DataFrame."""
    df = pd.DataFrame({'timestamp': pd.Series([], dtype="datetime64[ns]")})
    expected = pd.DataFrame({
        'timestamp': pd.Series([], dtype="datetime64[ns]"),
        'timestamp_hour': pd.Series(dtype="Int64"),
        'timestamp_minute': pd.Series(dtype="Int64"),
        'timestamp_second': pd.Series(dtype="Int64")
    })
    result = extracting_hms(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_single_row_dataframe():
    """Test function with a DataFrame containing a single row."""
    df = pd.DataFrame({'timestamp': ['2024-02-15 10:15:45']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-02-15 10:15:45']),
        'timestamp_hour': pd.Series([10], dtype="Int64"),
        'timestamp_minute': pd.Series([15], dtype="Int64"),
        'timestamp_second': pd.Series([45], dtype="Int64")
    })
    result = extracting_hms(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_missing_values():
    """Test function with missing (NaT) values in the datetime column."""
    df = pd.DataFrame({'timestamp': ['2024-01-07 10:15:30', None, '2023-12-25 08:45:20']})
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07 10:15:30', None, '2023-12-25 08:45:20']),
        'timestamp_hour': pd.Series([10, pd.NA, 8], dtype="Int64"),
        'timestamp_minute': pd.Series([15, pd.NA, 45], dtype="Int64"),
        'timestamp_second': pd.Series([30, pd.NA, 20], dtype="Int64")
    })
    result = extracting_hms(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_non_datetime_column():
    """Test function with a non-datetime column. Expect a TypeError."""
    df = pd.DataFrame({'timestamp': ['not_a_date', 'still_not_a_date']})
    with pytest.raises(TypeError, match="Column 'timestamp' must be of datetime type."):
        extracting_hms(df, 'timestamp')


def test_missing_column():
    """Test function with a missing column. Expect a KeyError."""
    df = pd.DataFrame({'wrong_column': ['2024-01-01 08:00:00', '2023-12-31 18:45:30']})
    with pytest.raises(KeyError, match="Column 'timestamp' does not exist in the DataFrame."):
        extracting_hms(df, 'timestamp')


def test_timezone_aware_datetime():
    """Test function with timezone-aware datetime values."""
    df = pd.DataFrame({'timestamp': ['2024-01-07T12:30:45+00:00', '2023-12-25T08:15:30+00:00']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07T12:30:45+00:00', '2023-12-25T08:15:30+00:00']),
        'timestamp_hour': pd.Series([12, 8], dtype="Int64"),
        'timestamp_minute': pd.Series([30, 15], dtype="Int64"),
        'timestamp_second': pd.Series([45, 30], dtype="Int64")
    })
    result = extracting_hms(df, 'timestamp')
    assert_frame_equal(result, expected)


def test_unrelated_columns():
    """Test function with additional unrelated columns in the DataFrame."""
    df = pd.DataFrame({'timestamp': ['2024-01-07 12:30:45'], 'event': ['meeting']})
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    expected = pd.DataFrame({
        'timestamp': pd.to_datetime(['2024-01-07 12:30:45']),
        'event': ['meeting'],
        'timestamp_hour': pd.Series([12], dtype="Int64"),
        'timestamp_minute': pd.Series([30], dtype="Int64"),
        'timestamp_second': pd.Series([45], dtype="Int64")
    })
    result = extracting_hms(df, 'timestamp')
    assert_frame_equal(result, expected)



def test_special_character_column_name():
    """Test function with a column name containing special characters."""
    df = pd.DataFrame({'time@stamp': ['2024-01-07 12:30:45']})
    df['time@stamp'] = pd.to_datetime(df['time@stamp'])
    expected = pd.DataFrame({
        'time@stamp': pd.to_datetime(['2024-01-07 12:30:45']),
        'time@stamp_hour': pd.Series([12], dtype="Int64"),
        'time@stamp_minute': pd.Series([30], dtype="Int64"),
        'time@stamp_second': pd.Series([45], dtype="Int64")
    })
    result = extracting_hms(df, 'time@stamp')
    assert_frame_equal(result, expected)


def test_large_dataframe():
    """Test function with a very large DataFrame."""
    df = pd.DataFrame({'timestamp': pd.date_range(start='2024-01-01', periods=1000000, freq='S')})
    result = extracting_hms(df, 'timestamp')
    assert result.shape == (1000000, 4)  # Ensure the new columns are added
    assert result['timestamp_hour'].iloc[0] == 0
    assert result['timestamp_minute'].iloc[-1] == 46  # Last row's minute
    assert result['timestamp_second'].iloc[-1] == 39  # Last row's second