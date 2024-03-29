#!/usr/bin/python3

""" script that fetches https://alx-intranet.hbtn.io/status
using request package only"""

import requests


url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
