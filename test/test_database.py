# -*- coding: utf-8 -*-
"""
Pytesting/test/test_database.py

Test cases for the Data Access Object

@author: Rupert.Thomas
Created 15/11/2019

Run tests (from the root folder using):
python -m pytest test/

"""
import sqlite3

from pytest_mock import MockerFixture
from truth.truth import AssertThat

# Module under test
from app.database import DAO


def test_init(mocker: MockerFixture):
    """
        Test database initialisation
    """

    # given: setup test framework
    mock_SQLite3 = mocker.patch('app.database.sqlite3')
    mock_ConnectionObj = mocker.MagicMock(
        sqlite3.Connection)  # mock Connection object
    mock_CursorObj = mocker.MagicMock(sqlite3.Cursor)  # mock Cursor object
    mock_ConnectionObj.cursor.return_value = mock_CursorObj  # setup method calls
    mock_SQLite3.connect.return_value = mock_ConnectionObj

    # when: database is initialised
    dao = DAO()

    # then: expect connection and request for cursor
    AssertThat(mock_SQLite3.connect).WasCalled().Once()
    mock_SQLite3.connect.assert_called_once()
    mock_ConnectionObj.cursor.assert_called_once()


def test_delete_db(mocker: MockerFixture):
    """
        Test deleting the database file
    """

    # given: setup test framework
    # patch database createion in DAO.__init__
    mock_SQLite3 = mocker.patch('app.database.sqlite3')
    dao = DAO()
    # patch database deletion command
    mock_os_remove = mocker.patch('app.database.os.remove')

    # /when
    dao.delete_db()

    # /then
    mock_os_remove.assert_called_once()


def test_close_db(mocker: MockerFixture):
    pass


def test_create_jobs_table(mocker: MockerFixture):
    pass


def test_insert_job(mocker: MockerFixture):
    pass


def test_query_job(mocker: MockerFixture):
    pass
