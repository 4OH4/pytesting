# -*- coding: utf-8 -*-
"""
Pytesting/run_tests.py

Test runner for demo app

@author: Rupert.Thomas
Created 16/11/2019

Adapted from: https://github.com/cambridgespark/pydata-testing-for-data-science
Raoul-Gabriel Urma

Run tests (from the root folder using):
python -m pytest test/

"""
import argparse
import os
# import urllib.request
import sys

import pytest

def run_unittests():
    print("Unittesting model...")
    pytest.main(['-v', 'tests'])

def run_coverage():
    print("Running coverage report...")
    pytest.main(['--cov-report', 'term-missing', '--cov=src/', 'tests/'])

def run_generative():
    print("Running generative testing...")
    pytest.main(['-v', '--hypothesis-show-statistics', 'tests/test_transformers_hypothesis.py'])


def main():
    parser = argparse.ArgumentParser(
        description="A command line-tool to manage the project.")
    parser.add_argument(
        'stage',
        metavar='stage',
        type=str,
        choices=['unittest', 'generative', 'coverage'],
        help="Stage to run. Either unittest, generative, coverage")

    if len(sys.argv[1:]) == 0:
        # parser.print_help()
        # parser.exit()
        print("Running all...")
        run_unittests()
        run_generative()
        run_coverage()
        return

    stage = parser.parse_args().stage

    if stage == "unittest":
        run_unittests()

    elif stage == "coverage":
        run_coverage()

    elif stage == "generative":
        run_generative()


if __name__ == "__main__":
    main()
