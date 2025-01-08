# wranglepy

A package for wrangling and tidy data in python.

This package consists of the following functions:
- `column_standardizer`: returns a copy of the inputted dataframe with standardized column names.
- `string_standardizer`: returns a string that is converted to lowercase and its non-alphanumerics (including spaces and punctuation) are replaced with underscores.
- `resulting_duplicates`: identifies which strings became duplicates after standardization.
- `extracting_ymd`: returns a copy of the inputted dataframe with three new columns: year, month, and day, splitting from inputted datetime column name.
- `extracting_hms`: returns a copy of the inputted dataframe with three new columns: hour, minute, and second, from inputted datetime column name.
- `remove_duplicates`: Remove duplicate rows from a list of dictionaries based on specified keys.

## Installation

```bash
$ pip install wranglepy
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`wranglepy` was created by Shannon Pflueger, Stephanie Ta, Wai Ming Wong, Yixuan(Clara) Gao. It is licensed under the terms of the MIT license.

## Credits

`wranglepy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
