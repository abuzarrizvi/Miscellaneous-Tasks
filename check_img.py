import datetime
import json
import logging
import requests
import sys
import traceback
from urllib import parse as urlparse



if requests.get("https://api.xiq.io/static/admin/images/Executives/263421.jpg").status_code != 404:
	print("Image exists")
else:
	print("Image not exists")