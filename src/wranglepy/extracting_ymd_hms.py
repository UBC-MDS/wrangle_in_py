import pandas as pd

def extracting_ymd(df, column):
    """
    Splits a datetime column into three new columns: year, month, and day.

    This function modifies the input DataFrame inplace, adding columns named
    '<column>_year', '<column>_month', and '<column>_day' based on the given datetime column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the datetime column.
    column (str): The name of the datetime column.

    Returns:
    None: Modifies the DataFrame inplace.

    Example:
    >>> df = pd.DataFrame({'timestamp': ['2024-01-07 12:30:45', '2023-12-25 08:15:30']})
    >>> df['timestamp'] = pd.to_datetime(df['timestamp'])
    >>> extracting_ymd(df, 'timestamp')
    >>> df
            timestamp  timestamp_year  timestamp_month  timestamp_day
    0 2024-01-07 12:30:45             2024                1             7
    1 2023-12-25 08:15:30             2023               12            25
    """
    df[f'{column}_year'] = df[column].dt.year
    df[f'{column}_month'] = df[column].dt.month
    df[f'{column}_day'] = df[column].dt.day


def extracting_hms(df, column):
    """
    Splits a datetime column into three new columns: hour, minute, and second.

    This function modifies the input DataFrame inplace, adding columns named
    '<column>_hour', '<column>_minute', and '<column>_second' based on the given datetime column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the datetime column.
    column (str): The name of the datetime column.

    Returns:
    None: Modifies the DataFrame inplace.

    Example:
    >>> df = pd.DataFrame({'timestamp': ['2024-01-07 12:30:45', '2023-12-25 08:15:30']})
    >>> df['timestamp'] = pd.to_datetime(df['timestamp'])
    >>> extracting_hms(df, 'timestamp')
    >>> df
            timestamp  timestamp_hour  timestamp_minute  timestamp_second
    0 2024-01-07 12:30:45             12                30               45
    1 2023-12-25 08:15:30              8                15               30
    """
    df[f'{column}_hour'] = df[column].dt.hour
    df[f'{column}_minute'] = df[column].dt.minute
    df[f'{column}_second'] = df[column].dt.second