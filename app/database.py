# -*- coding: utf-8 -*-
"""
Pytesting/database.py

Database Access Object (DAO) for demo application

@author: Rupert.Thomas
Created 15/11/2019

Adapted from this snippet: https://codereview.stackexchange.com/questions/182700/python-class-to-manage-a-table-in-sqlite

N.B. This class is a useful demo example, but in practice an 
Object-Relational Mapper (such as SQLAlchemy) would be more appropriate

Run integrated doctest using the following command:
python -m doctest -v database.py
"""

import os
import sqlite3

class DAO(object):
    """
    Sqlite3 database DAO for Pytesting demo application
    Handles a database table for job information:
    job title, job ID, company name, job salary

    Usage:
    >>> dao = DAO('example.db')
    Database connection initialised
    >>> dao.create_jobs_table()
    >>> dao.insert_job('Cook','Tasty Food Shack',11000,'11/06/2019')
    1
    >>> dao.query_job(1)
    ('Cook', 1, 'Tasty Food Shack', 11000, '11/06/2019')
    >>> dao.close()
    >>> dao.delete_db()

    """

    def __init__(self, db_filepath='example.db'):
        """Initialize DB class variables"""
        self.db_filepath = db_filepath
        self.connection = sqlite3.connect(self.db_filepath)
        self.cur = self.connection.cursor()
        print('Database connection initialised')

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def delete_db(self):
        """delete the database file"""
        os.remove(self.db_filepath)

    def create_jobs_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS jobs(job_title text,
                                                            job_id integer PRIMARY KEY, 
                                                            company_name text,
                                                            salary integer,
                                                            date text)''')
    def insert_job(self, job_title, company_name, salary, date):
        sql = """
            INSERT INTO jobs (job_title, company_name, salary, date)
            VALUES (?, ?, ?, ?)"""
        self.cur.execute(sql, (job_title, company_name, salary, date))
        self.commit()
        return self.cur.lastrowid

    def query_job(self, job_id):
        sql = """
            SELECT job_title, job_id, company_name, salary, date FROM jobs WHERE job_id = ?
            """
        self.cur.execute(sql, str(job_id))
        result = self.cur.fetchone()
        return result

    def commit(self):
        """commit changes to database"""
        self.connection.commit()
    
    # Support for context management
    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()
