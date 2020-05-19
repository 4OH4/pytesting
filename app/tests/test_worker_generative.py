# -*- coding: utf-8 -*-
"""
Pytesting/test/test_worker.py

Generative test cases for the data processing Worker object

@author: Rupert.Thomas
Created 22/11/2019

Run tests (from the root folder using):
pytest

"""

import datetime
from string import printable  # digits + ascii_letters + punctuation + whitespace

from hypothesis.strategies import text, dates
from hypothesis import given

from truth.truth import AssertThat

# Module under test
from app.core.worker import Worker


# Generate strings using all printable characters, except forward slashes
@given(input_string=text(alphabet=[char for char in printable if char !=',']))
def test_worker_parseLineCSV_generative(input_string):
    
    # given
    worker = Worker()

    # when
    result = worker.parseLineCSV(input_string)
    
    # then
    AssertThat(result).IsNone()


# Generate dates within the four digit year range
@given(input_date=dates(min_value=datetime.date(1000, 1, 1), max_value=datetime.date(9999, 1, 1)))
def test_worker_parseDate1_generative(mocker, input_date):

    # given
    input_string = input_date.strftime(format="%d%b%Y")
    worker = Worker()

    # when 
    result = worker.parseDate(input_string)
    
    print(input_string, result)
    
    # then
    AssertThat(result).IsInstanceOf(str)
    AssertThat(result).HasSize(10)
    AssertThat(result.split('-')).HasSize(3)


# Generate strings using all printable characters, except forward slashes
@given(input_string=text())
def test_worker_parseDate2_generative(input_string):
    
    # given
    worker = Worker()

    # when
    result = worker.parseLineCSV(input_string)
    
    # then
    # returns None or a string
    # Must not throw unhandled exception
    if result is not None:
        AssertThat(result).IsInstanceOf(str)
