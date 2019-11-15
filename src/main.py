# -*- coding: utf-8 -*-
"""
Pytesting/worker.py

Start point for demo application

@author: Rupert.Thomas
Created 15/11/2019
"""

from worker import Worker
from database import DAO

class Application:
    def __init__(self):
        super().__init__()
        
        # Setup database access
        dao = DAO()
        dao.create_jobs_table()
        self.dao = dao



if __name__ == '__main__':
    
    # if being exectuted, create the app object
    app = Application()
