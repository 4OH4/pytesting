# -*- coding: utf-8 -*-
"""
Pytesting/test/test_worker.py

Test cases for the data processing Worker object

@author: Rupert.Thomas
Created 17/11/2019

Run tests (from the root folder using):
pytest

"""

from truth.truth import AssertThat

# Module under test
from src.worker import Worker


def test_parseLine1(mocker):
    """ 
    Test parseLine with good data (all fields present)

    Expected result: dict returne with data
    """
    
    # given: setup test framework
    worker = Worker()
    testString = "11/11/19,Teacher,Brighter Futures,12000"
    expectedResult = {
                    'date': '11/11/2019',
                    'job_title': 'Teacher',
                    'company_name': 'Brighter Futures',
                    'salary': 12000
                }
    
    # when:
    result = worker.parseLine(testString)
    
    # then:
    assert result == expectedResult


def test_parseLine2(mocker):
    """ 
    Test parseLine with bad data (some fields missing)

    Expected result: result is None
    """
    
    # given: setup test framework
    worker = Worker()
    testString = "11/11/19,Brighter Futures,12000"
    
    # when:
    result = worker.parseLine(testString)
    
    # then: (Using PyTruth assertions)
    AssertThat(result).IsNone()


def test_parseDate1(mocker):
    """ 
    Test parseLine with Date format 1: dd/mm/yy

    Expected result: formatted string in dd/mm/YYYY
    """    
    # given: setup test framework
    worker = Worker()
    testString = "01/12/20"
    expected_result = "01/12/2020"
    
    # when:
    result = worker.parseDate(testString)
    
    # then: (Using PyTruth assertions)
    AssertThat(result).IsEqualTo(expected_result)


def test_parseDate2(mocker):
    """ 
    Test parseLine with Date format 2: ddmmmYYYY

    Expected result: formatted string in dd/mm/YYYY
    """    
    # given: setup test framework
    worker = Worker()
    testString = "04Jan2019"
    expected_result = "04/01/2019"
    
    # when:
    result = worker.parseDate(testString)
    
    # then: (Using PyTruth assertions)
    AssertThat(result).IsEqualTo(expected_result)


def test_parseDate3(mocker):
    """ 
    Test parseLine with bad Date format 1: dd/mmyy

    Expected result: result is None
    """    
    # given: setup test framework
    worker = Worker()
    testString = "12/1220"
    
    # when:
    result = worker.parseDate(testString)
    
    # then:
    AssertThat(result).IsNone()


def test_parseDate4(mocker):
    """ 
    Test parseLine with bad Date format 2: 32Jan2019

    Expected result: result is None
    """    
    # given: setup test framework
    worker = Worker()
    testString = "32Jan2019"
    
    # when:
    result = worker.parseDate(testString)
    
    # then:
    AssertThat(result).IsNone()
