import datetime
import json
import logging
import requests
import sys
import traceback
from urllib import parse as urlparse
import urllib.request
import requests
response = requests.get("http://www.berkley.com")
if response.history:
    print ("Request was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url) 
    print ("Final destination:")
    print (response.status_code, response.url)
else:
    print ("Request was not redirected")

url = 'http://www.wrberkley.com'
r = requests.head(url, allow_redirects=True)
if r.url != url:
	print("url was redirected")
	print(r.url)


tplist = []
if tplist:
	print("list is not empty")
else:
	print("list is empty")


# edisoninvestor.com
url = "https://www.edison.com/"
if '.com/' in url:
	sp = url.split('.com/')
	url = sp[0]+'.com'

	print(url)
