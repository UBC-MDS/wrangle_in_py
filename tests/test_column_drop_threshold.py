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
    
    column_drop_threshold should drop any columns with a coefficient of variance lower than 0.01 .
    Threshold will be set high to allow test only the variance dropping aspect here.
    """
    dropped_var_df = column_drop_threshold(expected_df, 0.95, 0.01)
    assert dropped_var_df == expected_df.drop(columns=["weight_g"], inplace=True)
    
def expected_thr_var_drop():
    """
    column_drop_threshold should drop any columns with more than 15% missing data and
    any columns with a coefficient of variance lower than 0.01
    """
    dropped_thr_var_df = column_drop_threshold(expected_df, 0.15, 0.01)
    assert dropped_thr_var_df == expected_df.drop(columns=["weight_g", "height_cm"], inplace=True)

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

def low_variance():
    """
    column_drop_threshold should drop every column due to a too low coefficient of variance
    """
    var_copy = expected_df.copy()
    var_copy['height_cm'] = var_copy['height_cm'].fillna(10) # Fill existing NA values with 10
    assert column_drop_threshold(var_copy, 0.95, 0.9) == expected_df.drop(columns=["weight_g", "height_cm"], inplace=True)

def high_missing_low_var():
    """
    column_drop_threshold should drop every column, some due to missing values,
    and other columns due to low coefficient of variance
    """
    assert column_drop_threshold(expected_df, 0.15, 0.9) == expected_df.drop(columns=["weight_g", "height_cm"], inplace=True)

def empty_test():
    """
    column_drop_threshold should return the same empty dataframe
    """
    assert column_drop_threshold(empty_df, 0.4) == empty_df

# invalid input tests

def test_invalid_dataframe_type():
    # Invalid data type (not a DataFrame)
    invalid_inputs = [123, "string", [], None, True]
    
    for input in invalid_inputs:
        with pytest.raises(TypeError):  # Expect a TypeError
            column_drop_threshold(input, 0.5, 0.5)  

def test_invalid_missingness():
    invalid_inputs = [-0.5, 1.5, "string", [], None, True]

    for input in invalid_inputs:
        with pytest.raises(ValueError):  # Expect a ValueError for invalid missingness
            column_drop_threshold(expected_df, input, 0.5)

def test_invalid_cv():
    invalid_inputs = [-1, "string", [], None, True]

    for input in invalid_inputs:
        with pytest.raises(ValueError):  # Expect a ValueError for invalid cv
            column_drop_threshold(expected_df, 0.5, input)