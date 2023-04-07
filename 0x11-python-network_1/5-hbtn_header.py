#!/usr/bin/python3

""" script that takes in a URL, sends a request to
the URL and displays the value of the variable
X-Request-Id in the response header
requests and sys packages only must be used"""

import requests
import sys


url = sys.argv[1]
response = requests.get(url)
print(response.headers.get('X-Request-Id'))
