def string_standardizer(messy_string):
    """
    Converts the inputted messy_string to lowercase and
    non-alphanumerics (including spaces and punctuation) will be replaced with underscores.

    Parameters
    ----------
    messy_string : str
        The input string to be standardized.

    Returns
    -------
    str
        A standardized version of the input string in lowercase 
        and non-alphanumeric characters replaced by underscores.

    Examples
    --------
    >>> string_standardizer('Jack Fruit 88')
    'jack_fruit_88'
    
    >>> string_standardizer('PINEAPPLES')
    'pineapples'

    >>> string_standardizer('Dragon (Fruit)')
    'dragon_fruit'
    """

def resulting_duplicates(original_strings, standardized_strings):
    """
    Identifies which strings became duplicates after standardization.

    Parameters
    ----------
    original_strings : list of str
        List of strings before standardization.
    standardized_strings : list of str
        List of strings after standardization.

    Returns
    -------
    dict
        A dictionary where the keys are the standardized strings with duplicate(s),
        and the values are lists of the original strings that map to them.
    
    Examples
    --------
    >>> strings_before = ['Jack Fruit 88', "Jack! Fruit! 88!", "PINEAPPLES"]
    >>> strings_after = ["jack_fruit_88", "jack_fruit_88", "pineapples"]
    >>> identify_duplicates(strings_before, strings_after)
    {'jack_fruit_88': ['Jack Fruit 88', 'Jack! Fruit! 88!']}
    """

def column_standardizer(dataframe):
    """
    Returns a copy of the inputted dataframe with standardized column names.
    Column names will be converted to lowercase and
    non-alphanumerics (including spaces and punctuation) will be replaced with underscores.

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
    >>> data = {'Jack Fruit 88': [1, 2], 'PINEAPPLES': [3, 4], 'Dragon (Fruit)': [25, 30]}
    >>> df = pd.DataFrame(data)
    >>> column_standardizer(df)
       jack_fruit_88  pineapples  dragon_fruit
    0           1          3         25
    1           2          4         30
    """