# -*- coding: utf-8 -*-
"""
Pytesting/test/test_worker.py

Test cases for the data processing Worker object

@author: Rupert.Thomas
Created 17/11/2019

Run tests (from the root folder using):
pytest

"""

import pytest
from truth.truth import AssertThat

# Module under test
from app.core.worker import Worker


def test_parseLine1(mocker):
    """ 
    Test parseLineCSV with good data (all fields present)

    Expected result: dict returned with data
    """
    
    # given: setup test framework
    worker = Worker()
    testString = "12Nov2019,Teacher,Brighter Futures,12000"
    expectedResult = {
                    'date': '2019-11-12',
                    'job_title': 'Teacher',
                    'company_name': 'Brighter Futures',
                    'salary': 12000
                }
    
    # when:
    result = worker.parseLineCSV(testString)
    
    # then:
    assert result == expectedResult


def test_parseLine2(mocker):
    """ 
    Test parseLineCSV with bad data (some fields missing)

    Expected result: result is None
    """
    
    # given: setup test framework
    worker = Worker()
    testString = "11/11/19,Brighter Futures,12000"
    
    # when:
    result = worker.parseLineCSV(testString)
    
    # then: (Using PyTruth assertions)
    AssertThat(result).IsNone()


def test_parseDate1(mocker):
    """ 
    Test parseDate with date format: ddmmmYYYY

    Expected result: formatted string in YYYY-mm-dd
    """    
    # given: setup test framework
    worker = Worker()
    testString = "01Dec2020"
    expected_result = "2020-12-01"
    
    # when:
    result = worker.parseDate(testString)
    
    # then: (Using PyTruth assertions)
    AssertThat(result).IsEqualTo(expected_result)


def test_parseDate2(mocker):
    """ 
    Test parseDate with date format: ddmmmYYYY

    Expected result: formatted string in YYYY-mm-dd
    """    
    # given: setup test framework
    worker = Worker()
    testString = "04Jan2019"
    expected_result = "2019-01-04"
    
    # when:
    result = worker.parseDate(testString)
    
    # then: (Using PyTruth assertions)
    AssertThat(result).IsEqualTo(expected_result)


@pytest.mark.xfail  # This test case is currently expected to fail
def test_parseDate3(mocker):
    """ 
    Test parseDate with unusual input

    Expected result: result is None

    N.B. Worker.parseDate doesn't implement robust input validation, so will
    trigger an unhandled exception when fed non-string inputs. Hence, this
    test case is currently expected to fail.

    """    
    # given: setup test framework
    worker = Worker()
    input_strings = ["12/1220", "01/01/19999", "Monday", -1, [], {"hello": "world"}, 3.5] 
    
    # when:
    for input_string in input_strings:
        result = worker.parseDate(input_string)
        
        # then:
        AssertThat(result).IsNone()


@pytest.mark.xfail  # This test case is currently expected to fail
def test_parseDate4(mocker):
    """ 
    Test parseDate with unusual input

    Expected result: result is None

    N.B. Worker.parseDate contains some complicated logic, that can get tripped
    by some unusual input - in this case a real-world date format "19th June 2020".
    Hence, this test case is currently expected to fail.

    """    
    # given: setup test framework
    worker = Worker()
    input_strings = ["32Jan2019", "Tuesday", "19th June 2020"]
    
    # when:
    for input_string in input_strings:
        result = worker.parseDate(input_string)
    
    # then:
        AssertThat(result).IsNone()
