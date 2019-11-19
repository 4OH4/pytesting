# -*- coding: utf-8 -*-
"""
Pytesting/worker.py

Core module for demo application

@author: Rupert.Thomas
Created 15/11/2019
"""

# Conversion map for three-letter months
short_months = {'Jan': 1, 'Feb': 1, 'Mar': 3, 'Apr': 4, 'May': 5, 'June': 6,
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

            parsed = self.parseLine(temp_line)
            if parsed is not None:
                output_data.append(parsed)
            
            else:
                # data incomplete
                continue

        return output_data


    def parseLine(self, input_string):
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
        Parses an input string, and extracts integer values for day, month and year

        N.B. this function is deliberately lacking in robust validation and checking of the input data

        :param input_string: (string) hopefully containing a date in one of the two recognised formats
        :returns result: (string) parsed date in dd/mm/YYYY format
        """
        result_string = None
        # Date format 1: dd/mm/yy     e.g. 01/09/19
        split_parts = input_string.split('/')
        if len(split_parts) == 3:
            dd = int(split_parts[0])
            mm = int(split_parts[1])
            YYYY = 2000 + int(split_parts[2])
            
            # Test and assemble output
            if (dd>0) and (dd<=31) and \
                (mm>0) and (mm<=12) and \
                (YYYY>2000) and (YYYY<2100):
                    result_string = f'{dd:02}/{mm:02}/{YYYY}'

        # Date format 2: ddmmmYYYY    09Jan2019
        elif any(month in input_string for month in short_months.keys()):
            # One of the three letter month strings is in the input
            match = next(month for month in short_months.keys() if month in input_string)
            split_parts = input_string.split(match)
            if len(split_parts) == 2:
                dd = int(split_parts[0])
                mm = short_months[match]
                YYYY = int(split_parts[1])
                
                # Test and assemble output
                if (dd>0) and (dd<=31) and \
                    (YYYY>2000) and (YYYY<2100):
                    result_string = f'{dd:02}/{mm:02}/{YYYY}'
                
#        else: # Unknown date format

        return result_string
