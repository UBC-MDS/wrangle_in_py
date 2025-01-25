import pandas as pd
import pytest
from wrangle_in_py.column_drop_threshold import column_drop_threshold

#test data
empty_df = pd.DataFrame()
expected_df = pd.DataFrame({
    'apple': ['red delicious', 'pink lady', 'granny smith', 'gala'],
    'weight_g': [110, 100, 100, 105],
    'height_cm': [8, pd.NA, pd.NA, 12]
})
new3_df = expected_df.drop(columns=["weight_g", "height_cm"])
pd.set_option('future.no_silent_downcasting', True)

#expected cases
def test_expected_missing_drop():
    """
    Column_drop_threshold should drop any columns with more than 15% missing data. 
    The variance argument will default to None and no columns should be removed because of high variance
    """
    dropped_thr_df = column_drop_threshold(expected_df, 0.15, 0.01)
    new_df = expected_df.drop(columns=["height_cm"])
    assert dropped_thr_df.shape == new_df.shape, f"Expected shape {new_df.shape}, but got {dropped_thr_df.shape}"

def test_expected_var_drop():
    """
    column_drop_threshold should drop any columns with a coefficient of variance lower than 0.01 .
    Threshold will be set high to allow test only the variance dropping aspect here.
    """
    dropped_var_df = column_drop_threshold(expected_df, 0.95, 0.3)
    new2_df = expected_df.drop(columns=["weight_g"])
    assert dropped_var_df.shape == new2_df.shape, f"Expected shape {new2_df.shape}, but got {dropped_var_df.shape}"
    
def test_expected_thr_var_drop():
    """
    column_drop_threshold should drop any columns with more than 15% missing data and
    any columns with a coefficient of variance lower than 0.01
    """
    dropped_thr_var_df = column_drop_threshold(expected_df, 0.15, 0.3)
    assert dropped_thr_var_df.shape == new3_df.shape, f"Expected shape {new3_df.shape}, but got {dropped_thr_var_df.shape}"

# #edge cases
def test_no_drops():
    """
    column_drop_threshold should not drop any columns, there are no missing values and 
    the variance is below the specified max.
    """
    expected_copy = expected_df.copy()
    expected_copy['height_cm'] = expected_copy['height_cm'].fillna(10).infer_objects(copy=False) # Fill existing NA values with a number
    assert column_drop_threshold(expected_copy, 0.4).shape == expected_copy.shape, f"Expected shape {expected_copy.shape}, but got {column_drop_threshold(expected_copy, 0.4).shape}"

def test_high_missingness():
    """
    column_drop_threshold should drop every column due to missing values
    """ 
    missing_copy = expected_df.copy()
    missing_copy = missing_copy.astype('object')  # Convert to nullable object type
    missing_copy[:] = pd.NA # Replace all values with NA
    no_columns = expected_df.drop(columns=["apple", "weight_g", "height_cm"])
    assert column_drop_threshold(missing_copy, 0.5).shape == no_columns.shape, f"Expected shape {no_columns.shape}, but got {column_drop_threshold(missing_copy, 0.5).shape}"

def test_low_variance():
    """
    column_drop_threshold should drop every column due to a too low coefficient of variance
    """
    var_copy = expected_df.copy()
    var_copy['height_cm'] = var_copy['height_cm'].fillna(10).infer_objects(copy=False) # Fill existing NA values with 10
    assert column_drop_threshold(var_copy, 0.98, 0.9).shape == new3_df.shape, f"Expected shape {new3_df.shape}, but got {column_drop_threshold(var_copy, 0.98, 0.9).shape}"

def test_high_missing_low_var():
    """
    column_drop_threshold should drop every column, some due to missing values,
    and other columns due to low coefficient of variance
    """
    assert column_drop_threshold(expected_df, 0.15, 0.9).shape == new3_df.shape, f"Expected shape {new3_df}, but got {column_drop_threshold(expected_df, 0.15, 0.9).shape}"

def test_empty_test():
    """
    column_drop_threshold should return the same empty dataframe
    """
    assert column_drop_threshold(empty_df, 0.4).shape == empty_df.shape, f"Expected shape {empty_df.shape}, but got {column_drop_threshold(empty_df, 0.4).shape}"

# invalid input tests

def test_invalid_dataframe_type():
    """
    column_drop_threshold should raise a TypeError if the input for df is an invalid data type (not a pandas DataFrame).
    """
    # Invalid data type (not a DataFrame)
    invalid_inputs = [123, "string", [], None]
    
    for input in invalid_inputs:
        with pytest.raises(TypeError):  # Expect a TypeError
            column_drop_threshold(input, 0.5, 0.5)  

def test_invalid_missingness():
    """
    column_drop_threshold should raise a ValueError if the input for threshold is invalid (not a float in the inclusive range 0 to <= 1).
    """
    invalid_inputs = [-0.5, 1.5, "string", [], None]

    for input in invalid_inputs:
        with pytest.raises(ValueError):  # Expect a ValueError for invalid missingness
            column_drop_threshold(expected_df, input, 0.5)

def test_invalid_cv():
    """
    column_drop_threshold should raise a ValueError if the input for variance is invalid (not a float >= 0)
    """
    invalid_inputs = [-1, "string", []]

    for input in invalid_inputs:
        with pytest.raises(ValueError):  # Expect a ValueError for invalid cv
            column_drop_threshold(expected_df, 0.5, input)
