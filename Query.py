################################################################################################
#                                                                                              #
# Inspired by:                                                                                 #
#  https://www.abuseipdb.com/api                                                               #
#  https://docs.abuseipdb.com/#introduction                                                    #                                        
#  https://www.youtube.com/watch?v=9N6a-VLBa2I                                                 #
#                                                                                              #
################################################################################################


import os 
import json
import requests

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'
key = os.environ['AbuseKey']

#Example 47.115.218.63 on 120 days
ipAddress = input("Enter the ip address you wish to query:  \n")
maxAgeInDays = input("Enter the search time (min 1/max 365 days):  \n")

querystring = {
    'ipAddress': ipAddress,
    'maxAgeInDays': maxAgeInDays,
    'verbose': 'yes'
}

headers = {
    'Accept': 'application/json',
    'Key': key
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
# Solutions from theses guys here https://www.geeksforgeeks.org/python-nested-dictionary/
resp = json.loads(response.text)

#Convert resp in variables for further actions 
ipA = resp['data']['ipAddress']
print(resp['data']['abuseConfidenceScore'])
print(resp['data']['countryCode'])
print(resp['data']['isp'])
print(resp['data']['domain'])
print(resp['data']['totalReports'])

