# -*- coding: utf-8 -*-
"""
Pytesting/worker.py

Start point for demo application

@author: Rupert.Thomas
Created 15/11/2019
"""

from app.core.worker import Worker
from app.core.database import DAO

class Application:
    def __init__(self):
        """ Constructor """
        super().__init__()
        
        # Setup database access
        dao = DAO()
        dao.create_jobs_table()
        self.dao = dao
        self.last_DB_row = None

        # Setup processing worker
        self.worker = Worker()

    def loadData(self, data_filepath):

        parsed_data = self.worker.readData(data_filepath)

        for row in parsed_data:
            self.last_DB_row = self.dao.insert_job(row['job_title'], 
                                row['company_name'], 
                                row['salary'], 
                                row['date'])
        
        print(f'Last row in database: {self.last_DB_row}')


if __name__ == '__main__':
    
    # if being exectuted, create the app object
    app = Application()
    app.loadData('data/salary_data.csv')
