# -*- coding: utf-8 -*-
"""
Pytesting/worker.py

Core module for demo application

@author: Rupert.Thomas
Created 15/11/2019
"""

# Conversion map for three-letter months
short_months = {'Jan': 1, 'Feb': 1, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# Data file format (columns)
# (date, job_title, company_name, salary)

class Worker:

    def readData(self, data_filepath):
        """
        Read comma-separated data from a data file, and parse.

        N.B. this function is deliberately lacking in robust validation and checking of the input data

        :param data_filepath: (string) path to data file
        :returns outputdata: (list) of dictionaries, one per row of imported data
        """
        
        output_data = []

        in_file = open(data_filepath, 'r')
        in_file.readline()  # skip the header line

        for temp_line in in_file.readlines():

            parsed = self.parseLineCSV(temp_line)
            if parsed is not None:
                output_data.append(parsed)
            
            else:
                # data incomplete
                continue

        return output_data

    def parseLineCSV(self, input_string):
        """
        Parse a single row of input data, and run rudimentary checks

        N.B. this function is deliberately lacking in robust validation and checking of the input data

        :param input_string: (string) of data, hopefully comma-separated
        :returns result: (dict) parsed data
        """

        result = None

        temp_data = input_string.split(',')
        if len(temp_data) == 4:
            date_string = self.parseDate(temp_data[0])
            
            if date_string is not None:
                result = {
                    'date': date_string,
                    'job_title': temp_data[1],
                    'company_name': temp_data[2],
                    'salary': int(temp_data[3])
                }

        return result
                
    def parseDate(self, input_string):
        """ 
        Parses an input string, and extracts a date in ddmmmYYYY format.
        Returns result in ISO8601 timestamp format

        N.B. this function is deliberately lacking in robust validation and checking of the input data.
        This functionality may be better handled by the datetime module, although as a demonstration
        it is written from scratch.

        :param input_string: (string) hopefully containing a date in the recognised format
        :returns result: (string) parsed date in YYYY-mm-dd format
        """
        result_string = None

        # Date format: ddmmmYYYY   e.g. 09Jan2019
        if any(month.lower() in input_string.lower() for month in short_months.keys()):
            # One of the three letter month strings is in the input
            match = next(month for month in short_months.keys() if month in input_string)
            split_parts = input_string.split(match)
            if len(split_parts) == 2:
                dd = int(split_parts[0])
                mm = short_months[match]
                YYYY = int(split_parts[1])
                
                # Test and assemble output
                if (dd>0) and (dd<=31): # and (YYYY>2000) and (YYYY<2100):
                    result_string = f'{YYYY}-{mm:02}-{dd:02}'

        return result_string
