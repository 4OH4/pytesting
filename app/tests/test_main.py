# -*- coding: utf-8 -*-
"""
Pytesting/test/test_main.py

Test cases for the main application

@author: Rupert.Thomas
Created 17/11/2019

Run tests (from the root folder using):
pytest

"""

import os

from truth.truth import AssertThat

# Module under test
from app.core.main import Application


def test_init(mocker):
    """ 
    Test application initialisation

    Expected result: DAO and Worker classes instantiated
    """
    
    # given: setup test framework
    mock_dao = mocker.patch('app.core.main.DAO')
    mock_worker = mocker.patch('app.core.main.Worker')
    
    # when:
    app = Application()
    
    # then:
    AssertThat(mock_dao).WasCalled().Once()
    AssertThat(mock_worker).WasCalled().Once()


def test_loadData(mocker):
    """ 
    Test application loading data from text file

    Expected result: app loads data into DB via DAO
    """
    
    # given: setup test framework
    mock_dao = mocker.patch('app.core.main.DAO')
    mock_worker = mocker.patch('app.core.main.Worker')
    dummy_data_filepath = 'data/dummy_datafile.txt'
    mock_data = {'job_title': 'Mechanic',
                'company_name': 'Red123',
                'salary': 98765,
                'date': '14/06/2019'}
    mock_worker.readData.return_value = mock_data
    app = Application()
    
    # when:    
    app.loadData(dummy_data_filepath)
    
    # then:
    # AssertThat(mock_worker.readData).WasCalled().Once().With(dummy_data_filepath)
    # AssertThat(mock_dao.insert_job).WasCalled().Once().With(mock_data['job_title'],
    #                 mock_data['company_name'],
    #                 mock_data['salary'],
    #                 mock_data['date'])
