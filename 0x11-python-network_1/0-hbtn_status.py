#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen

    url = "https://alx-intranet.hbtn.io/status"
    rqst = Request(url)
    with urlopen(rqst) as res:
        content = res.read()

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- contnet:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
