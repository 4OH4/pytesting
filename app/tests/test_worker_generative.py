# -*- coding: utf-8 -*-
"""
Pytesting/test/test_worker.py

Generative test cases for the data processing Worker object

@author: Rupert.Thomas
Created 22/11/2019

Run tests (from the root folder using):
pytest

"""

from hypothesis.strategies import text
from hypothesis import given

from truth.truth import AssertThat

# Module under test
from app.core.worker import Worker


@given(text())
def test_worker_parseLine_generative(input):

    worker = Worker()

    AssertThat(worker.parseLine(input)).IsNone()


# from hypothesis.strategies import date

# @given(date())
# def test_worker_parseDate1_generative(input):

#     worker = Worker()

#     AssertThat(worker.parseLine(input)).IsString()



