#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import base64
import getpass
try:
    import requests
except ImportError:
    print("Please install the python-requests module.")
    sys.exit(-1)
try:
    import json
except ImportError:
    print("Please install the python-json module.")
    sys.exit(-1)



def run ():

    username = '''username_base64'''
    username = base64.b64decode(username)
    password = '''password_base64'''
    password = base64.b64decode(password)

    with open('hosts', 'r') as file:

        for hostname in file:

            hostname = hostname.strip()
            response = os.system("ping -c 1 -W 1 " + hostname + " >/dev/null 2>&1")

            if response == 0:
                print(f"{hostname} is up!")
                enablehost(hostname, username, password)
                enableservices(hostname, username, password)
            else:
                print(f"{hostname} is down!")

def enablehost(hostname, username, password):

    request_url = "https://icinga2host:5665/v1/objects/hosts?host=" + hostname
    headers = {
            'Accept': 'application/json',
            'X-HTTP-Method-Override': 'POST'
    }
    data = {
            "attrs": { "enable_active_checks": True }
    }

    r = requests.post(request_url,
            headers=headers,
            auth=(username, password),
            data=json.dumps(data),
            verify="icinga.crt")

    if (r.status_code == 200):
            print("Result: " + json.dumps(r.json()))
    else:
            print(r.text)
           r.raise_for_status()

def enableservices(hostname, username, password):

    request_url = "https://icinga2host:5665/v1/objects/services"
    headers = {
            'Accept': 'application/json',
            'X-HTTP-Method-Override': 'POST'
    }
    data = {
            "type": "Service",
            "filter": "host.name==\"" + hostname + "\"",
            "attrs": { "enable_active_checks": True }
    }

    r = requests.post(request_url,
            headers=headers,
            auth=(username, password),
            data=json.dumps(data),
            verify="icinga.crt")

    if (r.status_code == 200):
            print("Result: " + json.dumps(r.json()))
    else:
            print(r.text)
           r.raise_for_status()

try:

    run()

except Exception as e:

    print (e)
    sys.exit(1)
