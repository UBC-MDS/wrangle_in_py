# wrangle_in_py
[![Documentation Status](https://readthedocs.org/projects/wrangle-in-py/badge/?version=latest)](https://wrangle-in-py.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/UBC-MDS/wrangle_in_py/graph/badge.svg?token=2TTQ23iNKM)](https://codecov.io/gh/UBC-MDS/wrangle_in_py)

A package for wrangling and tidy data in python. This package includes functions to assist the user with common data wrangling and tidying tasks in python such as changing column names or removing duplicate rows. 

This package fills a niche in the Python ecosystem by offering specialized tools for tidying and wrangling data, focusing on standardizing column names and strings, detecting duplicates after standardization, and extracting components from datetime columns. While libraries like [pandas](https://pypi.org/project/pandas/) provide general-purpose methods for similar tasks, such as renaming columns or working with datetime data, these often require multiple steps or custom scripts. By combining these focused functionalities into a single package, it offers a lightweight, user-friendly alternative for efficient data preprocessing.

## User-Facing Functions

This package consists of the following user-facing functions:

- **`column_name_standardizer`**: Returns a copy of the inputted dataframe with standardized column names.
- **`extracting_ymd`**: Returns a copy of the inputted dataframe with three new columns: year, month, and day, splitting from inputted datetime column name.
- **`extracting_hms`**: Returns a copy of the inputted dataframe with three new columns: hour, minute, and second, from inputted datetime column name.
- **`remove_duplicates`**: Removes duplicate rows from a DataFrame based on specified columns.
- **`column_drop_threshold`**: Returns a copy of the dataframe inputted with columns removed if they did not meet the threshold specified or if they had a lower coefficient of variance than specified.

## Helper Functions

This package also includes the following helper functions:

- **`string_standardizer`**: Returns a string that is converted to lowercase and its non-alphanumerics (including spaces and punctuation) are replaced with underscores. A helper function for `column_name_standardizer`.
- **`resulting_duplicates`**: Identifies which strings became duplicates after standardization. A helper function for `column_name_standardizer`.


## Installation

```bash
$ pip install wrangle_in_py
```

## Package Dependencies
Our package has the following dependencies:
- pandas >= 2.2.3
- scipy >= 1.15.1
Please note these packages will be installed when pip installing this package.

## Documentation

Our online documentation can be found [here](https://wrangle-in-py.readthedocs.io/en/latest/?badge=latest).

## Contributing

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`wrangle_in_py` was created by Shannon Pflueger, Stephanie Ta, Wai Ming Wong, Yixuan(Clara) Gao. It is licensed under the terms of the MIT license and Creative Commons Attribution 4.0 International License. [LICENSE](LICENSE)

## Credits

`wrangle_in_py` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors
- Shannon Pflueger
- Stephanie Ta
- Wai Ming Wong
- Yixuan(Clara) Gao
