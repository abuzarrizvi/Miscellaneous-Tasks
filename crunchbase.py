import traceback, sys
import requests
import json
import time


#Company Search
################################
query = "Siemens Healthineers"
################################

#Constants
################################
key = "your user key"
################################

################################
#Company Search API Call
################################

#Company API URL
url = "https://api.crunchbase.com/v3.1/odm-organizations?user_key="+key+"&name="
url += query
url += "&organization_types=company"
url += "&page=1"
print (url)

#Company API Call
response = requests.request("GET", url)
responseJSON = json.loads(response.text)
data = responseJSON["data"]
print("#####################################UUID########################")
print(data['items'][0]['uuid'])
print("#############################################################")
# Sleeping System so that Rate Limit is not breached
time.sleep(1)

#Parsing Results
companies = data["items"]
for company in companies:
    try:
        #Checking Type == Company
        if company["type"] == "OrganizationSummary":
            if(company["properties"]["primary_role"] == "company"):
                #Getting Company Properties
                companyname = company["properties"]["name"]
                companypermalink = company["properties"]["permalink"]

                print ("############################################################")
                print (companyname)

                ################################
                # Employees Search API Calls
                ################################

                currentpage = 1
                while True:
                    try:
                        # Person API URL
                        print ("Sending Request: "+str(currentpage))
                        url = "https://api.crunchbase.com/v3.1/odm-people?user_key="+key+"&query="
                        url += companyname
                        url += "&page="+str(currentpage)
                        print (url)

                        # Person API Call
                        response = requests.request("GET", url)
                        responseJSON = json.loads(response.text)
                        data = responseJSON["data"]

                        # Sleeping System so that Rate Limit is not breached
                        time.sleep(1)

                        #Calculating No. of Pages
                        noOfItems = responseJSON["data"]["paging"]["total_items"]
                        #If no Result then break
                        if(noOfItems == 0):
                            break

                        noOfPagesToSend = (noOfItems + 100 - 1) // 100
                        if(noOfPagesToSend > 10):
                            noOfPagesToSend = 10

                        persons = data["items"]
                        for person in persons:
                            # Checking Type == Person
                            if person["type"] == "PersonSummary":
                                # Checking if Employee belongs to Company
                                if (person["properties"]["organization_permalink"] == companypermalink):
                                    # Getting Person Properties
                                    personInfo = "Name: " + person["properties"]["first_name"] + " " + person["properties"]["last_name"]
                                    personInfo += " Designation: "+person["properties"]["title"]
                                    print (personInfo)

                        #Calculating if Next Page call need to be made
                        print ("C: "+str(currentpage))
                        print ("T: "+str(noOfPagesToSend))
                        if(currentpage == noOfPagesToSend):
                            break
                        else:
                            currentpage += 1


                    except Exception as e:
                        print ("Error Sending Request: " + str(currentpage))
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
                        # Sleeping System so that Rate Limit is not breached
                        time.sleep(3)
                print ("############################################################")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
