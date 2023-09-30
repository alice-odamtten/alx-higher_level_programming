#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(
                'https://alx-intranet.hbtn.io/status'
                ) as response:
            content = response.read()
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content.decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
