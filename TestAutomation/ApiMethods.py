#!usr/bin/env python
# -*-coding: utf-8-*-

"""
# the functions of api methods
# 1. api_method_get  #
# 2.
"""

import requests
import json


def api_method_get(url, headers):
    response = requests.get(url=url, headers=headers)
    response = response.json()
    if response['error_code'] == 0 and response['message'] == 'operation successful':
        return True
    else:
        return False
