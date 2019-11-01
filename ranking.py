import datetime
import json
import logging
import requests
import sys
import traceback




def handle():
    try:
        #ranking_list = RankingList.objects.get(list_name="Global 2000")
        print("start")
        year = datetime.datetime.now().year
        url = "https://www.forbes.com/ajax/list/data?year=" + str(year) + "&uri=global2000&type=organization"
        response = requests.get(url)
        forbes_companies = []
        not_matched = []
        try:
            forbes_companies = json.loads(response.content)
            if len(forbes_companies) == 0:
                url = "https://www.forbes.com/ajax/list/data?year=" + str(
                    year - 1) + "&uri=global2000&type=organization"
                response = requests.get(url)
                forbes_companies = json.loads(response.content)
        except Exception:
            logger.error("Unexpected response from Forbes API")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            logger.error(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        if forbes_companies:
            for item in range(len(forbes_companies)-1):
                for item2 in range(item+1,len(forbes_companies)):
                    if forbes_companies[item]['rank'] == forbes_companies[item2]['rank'] and forbes_companies[item]['name'] != forbes_companies[item2]['name']:
                        print(forbes_companies[item]['rank'])
    except Exception:
        print("exception")
    print("end")
    return ''

if __name__ == "__main__": 
	st = handle()
