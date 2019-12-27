# -*- coding: utf-8 -*-
"""
Pytesting/test/test_main.py

Test cases for the main application

@author: Rupert.Thomas
Created 17/11/2019

Run tests (from the root folder using):
pytest

"""

from truth.truth import AssertThat

# Module under test
from src.main import Application


def test_init(mocker):
    """ 
    Test application initialisation

    Expected result: DAO and Worker classes instantiated
    """
    
    # given: setup test framework
    mock_dao = mocker.patch('src.main.DAO')
    mock_worker = mocker.patch('src.main.Worker')
    
    # when:
    app = Application()
    
    # then:
    AssertThat(mock_dao).WasCalled().Once()
    AssertThat(mock_worker).WasCalled().Once()


def test_loadData(mocker):
    """ 
    Test parseLine with good data (all fields present)

    Expected result: dict returne with data
    """
    
    # given: setup test framework
    mock_dao = mocker.patch('src.main.DAO')
    mock_worker = mocker.patch('src.main.Worker')
    mock_worker.readData.return_value = None
    app = Application()
    
    # when:
    
    # then:
    AssertThat(mock_worker.readData).WasCalled().Once()
