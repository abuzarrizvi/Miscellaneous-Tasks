import datetime
import json
import logging
import requests
import sys
import traceback
from urllib import parse as urlparse

def getURLDomain(url):
    try:
        if url.find("http://")<0 and url.find("https://")<0:
            url = "http://"+url
        hostname = urlparse.urlparse(url)
        hostname = hostname.hostname
        domain = hostname.split(".")
        newdomain = []
        for d in domain:
            if d != "www":
                newdomain.append(d)
        domain = '.'.join(newdomain)
        return domain
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        logger.error(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
    return None


def handle():
    try:
        #ranking_list = RankingList.objects.get(list_name="Global 2000")
        print("start")
        #year = datetime.datetime.now().year
        url = "https://www.inc.com/inc5000list/json/inc5000_2019.json"
        response = requests.get(url)
        forbes_companies = []
        not_matched = []
        print("url loaded")
        try:
            forbes_companies = json.loads(response.content)
            if len(forbes_companies) == 0:
                url = "https://www.inc.com/inc5000list/json/inc5000_2018.json"
                response = requests.get(url)
                forbes_companies = json.loads(response.content)
        except Exception:
            logger.error("Unexpected response from Forbes API")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            logger.error(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        if forbes_companies:
            print("companies loaded")
            for company in forbes_companies:
                print('{}  {}'.format(company['company'],company['website']))
    except Exception:
        #print("exception")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        #print(exc_value)
    #print("end")
    return ''

if __name__ == "__main__": 
	st = handle()
    #st1 = getURLDomain("devada.com")
    #print(st1)