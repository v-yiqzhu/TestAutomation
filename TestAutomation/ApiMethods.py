#!usr/bin/env python
# -*-coding: utf-8-*-

"""
# the functions of api methods
# 1. api_method_get  #
# 2. api_method_delete
# 3. api_method_post
# 4. api_method_put
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


def api_method_delete(url, headers):
    response = requests.delete(url=url, headers=headers)
    response = response.json()
    if response['error_code'] == 0 and response['message'] == 'operation successful':
        return True
    else:
        return False


def api_method_post(url, headers, body):
    response = requests.post(url=url, headers=headers, json=body)
    response = response.json()
    if response['error_code'] == 0 and response['message'] == 'operation successful':
        return True
    else:
        return False


def api_method_put(url, headers):
    pass
