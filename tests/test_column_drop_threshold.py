import pandas as pd
import pytest
from wrangle_in_py import column_drop_threshold

#test data
empty_df = pd.DataFrame()
expected_df = pd.DataFrame({
    'apple': ['red delicious', 'granny smith', 'gala'],
    'weight_g': [110, 100, 100],
    'height_cm': [8, pd.NA, pd.NA]
})

#expected cases
def expected_missing_drop():
    """
    Column_drop_threshold should drop any columns with more than 15% missing data. 
    The variance argument will default to None and no columns should be removed because of high variance
    """
    dropped_thr_df = column_drop_threshold(expected_df, 0.15)
    assert dropped_thr_df == expected_df.drop(columns=["height_cm"], inplace=True)

def expected_var_drop():
    """
    column_drop_threshold should drop any columns with variance higher than ___.
    Threshold will be set high to allow test only the variance dropping aspect here.
    """
    
def expected_thr_var_drop():
    """
    column_drop_threshold should drop any columns with more than 15% missing data and
    any columns with variance higher than ___
    """

#edge cases
def no_drops():
    """
    column_drop_threshold should not drop any columns, there are no missing values and 
    the variance is below the specified max.
    """
    expected_copy = expected_df.copy()
    expected_copy['height_cm'] = expected_copy['height_cm'].fillna(10) # Fill existing NA values with a number
    assert column_drop_threshold(expected_copy, 0.4) == expected_copy

def high_missingness():
    """
    column_drop_threshold should drop every column due to missing values
    """ 
    missing_copy = expected_df.copy()
    missing_copy[:] = pd.NA # Replace all values with NA
    assert column_drop_threshold(missing_copy, 0.5) == empty_df

def high_variance():
    """
    column_drop_threshold should drop every column due to variance
    """

def high_missing_var():
    """
    column_drop_threshold should drop every column, some due to missing values,
    and other columns due to variance
    """

def empty_test():
    """
    column_drop_threshold should return the same empty dataframe
    """
    assert column_drop_threshold(empty_df, 0.4) == empty_df

# invalid input tests