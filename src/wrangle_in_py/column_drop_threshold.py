def column_drop_threshold(df, threshold, variance=None):
    """
    Returns a copy of the dataframe inputted with columns removed if they did not meet the threshold specified, 
    and with columns removed if they had variance lower than specified.
    
    Parameters
    ----------
    df : pd.DataFrame
        The input pandas dataframe whose missingness threshold needs to be checked for specified columns
    
    threshold : float
        The threshold for the proportion of missing values to allow in each column of the dataframe
        Columns with a larger proportion of missing observations than the threshold will be removed from the dataframe

    variance : float
        Default is None
        The lowest variance to allow in any one column of the dataframe
        Columns with a lower variance than specified will be removed from the dataframe
    
    Returns
    ----------
    pd.DataFrame
        A new dataframe where each column meets or exceeds the specified allowable missingness threshold. 
        Any columns previously not meeting the threshold have been removed.
    
    Examples
    ----------
    >>> data = {'apple': [1, 2, NaN], 'banana': [3, 4, 5], 'kiwi': [NaN, 30, NaN], 'peach': [2, 2, 2]}
    >>> df = pd.DataFrame(data)
    >>> column_drop_threshold(df, 0.35, 0.1)
        apple banana
    0   1     3
    1   2     4
    2   NaN   5
    """