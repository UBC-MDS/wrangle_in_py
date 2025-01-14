import pandas as pd

def remove_duplicates(dataframe, subset_columns=None, keep='first'):
    """
    Remove duplicate rows from a DataFrame based on specified columns.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame to process.
    subset_columns (list or None): List of column names to consider for identifying duplicates.
                                   If None, consider all columns.
    keep (str): Determines which duplicates to keep:
                - 'first': Keep the first occurrence (default).
                - 'last': Keep the last occurrence.
                - False: Drop all duplicates.

    Returns:
    pd.DataFrame: A DataFrame with duplicates removed.

    Example:
    >>> data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
    >>> df = pd.DataFrame(data)
    >>> remove_duplicates(df, subset_columns=['A'])
       A  B
    0  1  5
    1  2  6
    3  4  8
    """
    # Validate input
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    if subset_columns is not None:
        if not all(col in dataframe.columns for col in subset_columns):
            raise ValueError("Some columns in subset_columns are not present in the DataFrame")
    
    if keep not in ['first', 'last', False]: 
         raise ValueError("Invalid value for 'keep'. Must be 'first', 'last', or False.")

    # Drop duplicates using pandas
    return dataframe.drop_duplicates(subset=subset_columns, keep=keep)
