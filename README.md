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
Tests should be run from the command line, in the repository root.

### Doctest
Doctests are executed for a single module at a time. The command runs the tests in database.py (for example):

    python -m doctest -v src/database.py

The `-v` argument requests verbose output - otherwise it only reports test failures.

### Pytest
To run all test cases (in the `tests/` folder):

    python -m pytest tests
