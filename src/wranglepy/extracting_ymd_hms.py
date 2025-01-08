import pandas as pd

def extracting_ymd(df, column):
    """
    Returns a copy of the input DataFrame with three new columns: year, month, and day,
    extracted from the specified datetime column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the datetime column.
    column (str): The name of the datetime column to extract from.

    Returns:
    pd.DataFrame: A copy of the input DataFrame with added columns:
                  '<column>_year', '<column>_month', '<column>_day'.

    Example:
    >>> df = pd.DataFrame({'timestamp': ['2024-01-07 12:30:45', '2023-12-25 08:15:30']})
    >>> df['timestamp'] = pd.to_datetime(df['timestamp'])
    >>> extracting_ymd(df, 'timestamp')
            timestamp  timestamp_year  timestamp_month  timestamp_day
    0 2024-01-07 12:30:45             2024                1             7
    1 2023-12-25 08:15:30             2023               12            25
    """

def extracting_hms(df, column):
    """
    Returns a copy of the input DataFrame with three new columns: hour, minute, and second,
    extracted from the specified datetime column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the datetime column.
    column (str): The name of the datetime column to extract from.

    Returns:
    pd.DataFrame: A copy of the input DataFrame with added columns:
                  '<column>_hour', '<column>_minute', '<column>_second'.

    Example:
    >>> df = pd.DataFrame({'timestamp': ['2024-01-07 12:30:45', '2023-12-25 08:15:30']})
    >>> df['timestamp'] = pd.to_datetime(df['timestamp'])
    >>> extracting_hms(df, 'timestamp')
            timestamp  timestamp_hour  timestamp_minute  timestamp_second
    0 2024-01-07 12:30:45             12                30               45
    1 2023-12-25 08:15:30              8                15               30
    """