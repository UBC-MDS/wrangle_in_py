def column_standardizer(dataframe):
    """
    Returns a copy of the inputted dataframe with standardized column names.
    Column names will be converted to lowercase and
    non-alphanumerics (including spaces and puncutation) will be replaced with underscores.

    If the standardization results in duplicate column names, a warning will be raised.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The input pandas DataFrame whose column names need standardization.
    
    Warnings
    --------
    UserWarning:
        If any of the standardized column names are the same.

    Returns
    -------
    pd.DataFrame
        A new DataFrame with standardized column names.

    Examples
    --------
    >>> import pandas as pd
    >>> data = {'Jack Fruit 88': [1, 2], 'Pineapples!': [3, 4], 'Dragon (Fruit)': [25, 30]}
    >>> df = pd.DataFrame(data)
    >>> column_standardizer(df)
       jack_fruit_88  pineapples  dragon_fruit
    0           1          3         25
    1           2          4         30
    """