#!usr/bin/env python
# -*-coding: utf-8-*-

"""
# 1. read test case files from Folder ApiTestCases
# 2. read test cases by row
# 2.1 Get the Method of request {Get Post Delete Put}
# 2.2 call function by method
"""
from typing import Any, Union

import openpyxl
import ApiMethods
import json

# get work book by file path, and file name
TestCasePath = r'D:\test\TestAutomation\TestAutomation\ApiTestCases\ApiTestCase_1.xlsx'
workbook = openpyxl.load_workbook(filename=TestCasePath)

# get work sheet by sheet name "TestCase"
worksheet = workbook['TestCase']

# get the test case by row of sheet
for row in worksheet.iter_rows(min_row=2, max_col=len(worksheet[1]), max_row=len(worksheet['A'])):
    # call function by Method
    if row[3].value == 'GET':
        # to deal with the case of 'url + None'
        if row[5].value:
            url = 'https://' + row[4].value + row[5].value
        else:
            url = 'https://' + row[4].value

        headers = json.loads(row[6].value)
        if ApiMethods.api_method_get(url, headers):
            print("{} test passed".format(row[0].value))
        else:
            print("{} test failed".format(row[0].value))
    elif row[3].value == 'POST':
        pass
    elif row[3].value == 'DELETE':
        pass
    elif row[3].value == 'PUT':
        pass
    else:
        print("The case {} has wrong method".format(row[0].value))
