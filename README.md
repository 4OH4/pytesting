[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status - Travis](https://travis-ci.org/4OH4/pytesting.svg?branch=master)](https://travis-ci.org/4OH4/pytesting)
[![Build Status - GitHub](https://github.com/4oh4/pytesting/workflows/pytesting/badge.svg)](https://github.com/4OH4/pytesting/actions?query=workflow%3Apytesting)
[![Coverage Status](https://coveralls.io/repos/github/4OH4/pytesting/badge.svg?branch=master)](https://coveralls.io/github/4OH4/pytesting?branch=master)

# pytesting
Unit testing, code coverage and mocking with `Pytest`, and property-based testing with `Hypothesis`.

[https://github.com/4OH4/pytesting](https://github.com/4OH4/pytesting)

This repository is the companion code for a forthcoming blog post on Python software testing. Feedback encouraged - please raise an issue.

### Quickstart

Clone the repository, install requirements into your Python environment and run the tests:

    git clone https://github.com/4OH4/pytesting
    cd pytesting
    pip install -r requirements.txt
    python run_tests.py

### Quickstart with Docker

Clone the repository and run everything inside a Docker container:

    git clone https://github.com/4OH4/pytesting
    cd pytesting/Docker
    docker-compose -d up
    docker-compose run pytesting
    python run_tests.py

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
To run all test cases:

    pytest

To run the code coverage report:

    pytest --cov=src tests

