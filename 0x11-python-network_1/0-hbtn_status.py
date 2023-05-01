#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- contnet:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
