# -*- coding: utf-8 -*-
"""
Pytesting/run_tests.py

Test runner for demo app

@author: Rupert.Thomas
Created 16/11/2019

Adapted from: https://github.com/cambridgespark/pydata-testing-for-data-science
Raoul-Gabriel Urma

Run tests (from the root folder using):
python -m pytest app/tests

"""
import argparse
import os
# import urllib.request
import sys

import pytest

def run_all():
    print("Running all tests...")
    pytest.main(['-v', 'app/tests', '--cov-report', 'term-missing', '--cov=app/'])

def run_coverage_only():
    print("Running coverage report...")
    pytest.main(['--cov-report', 'term-missing', '--cov=app/', 'app/tests'])

def run_generative_only():
    print("Running generative testing...")
    pytest.main(['-v', 'app/tests', '--hypothesis-show-statistics', '-k', 'generative'])


def main():
    parser = argparse.ArgumentParser(
        description="A command line-tool to manage the project.")
    parser.add_argument(
        'stage',
        metavar='stage',
        type=str,
        choices=['all', 'generative', 'coverage'],
        help="Testing to run. Either: all, generative, coverage")

    if len(sys.argv[1:]) == 0:
        print("Running all...")
        run_all()
        return

    stage = parser.parse_args().stage

    if stage == "all":
        run_all()

    elif stage == "coverage":
        run_coverage_only()

    elif stage == "generative":
        run_generative_only()


if __name__ == "__main__":
    main()
