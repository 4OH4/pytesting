# -*- coding: utf-8 -*-
"""
Pytesting/test/test_database.py

Test cases for the Data Access Object

@author: Rupert.Thomas
Created 15/11/2019

Run tests (from the root folder using):
python -m pytest test/

"""

import os
import mock

# Module under test
from src.database import DAO


def test_delete_db(mocker):
    """
        Test deleting the database file
    """

    mocker.patch('os.remove')

    # /given
    dao = DAO()

    # /when
    dao.delete_db()
    
    # /then
    os.remove.assert_called_once()