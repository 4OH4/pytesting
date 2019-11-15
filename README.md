[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# pytesting
Unit testing, code coverage and mocking with `Pytest`, and property-based testing with `Hypothesis`.

## Setup and requirements
Python 3 and the following packages (all available via `pip`):
 - pytest
 - pytest-cov
 - pytest-mock
 - pytruth
 - hypothesis

Or install via the `requirements.txt` file:
    pip install -r requirements.txt

## Running test cases

### Doctest
    python -m doctest -v src/database.py

### Pytest
    python -m pytest test/