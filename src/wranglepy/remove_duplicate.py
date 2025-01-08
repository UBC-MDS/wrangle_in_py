def remove_duplicates(data, subset_columns=None, keep='first'):
    """
    Remove duplicate rows from a list of dictionaries based on specified keys.

    Parameters:
    data (list of dict): The dataset to process.
    subset_columns (list or None): List of keys to consider for identifying duplicates.
                                   If None, consider all keys.
    keep (str): Determines which duplicates to keep:
                - 'first': Keep the first occurrence (default).
                - 'last': Keep the last occurrence.
                - False: Drop all duplicates.

    Returns:
    list of dict: A list with duplicates removed.

    Example:
    >>> data = [
    ...     {"A": 1, "B": 5},
    ...     {"A": 2, "B": 6},
    ...     {"A": 2, "B": 6},
    ...     {"A": 4, "B": 8}
    ... ]
    >>> remove_duplicates(data, subset_columns=["A"])
    [{'A': 1, 'B': 5}, {'A': 2, 'B': 6}, {'A': 4, 'B': 8}]
    """