################################################################################################
#                                                                                              #
# Inspired by:                                                                                 #
#  https://www.abuseipdb.com/api                                                               #
#  https://docs.abuseipdb.com/#introduction                                                    #                                        #
#                                                                                              #
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
decodedResponse = json.loads(response.text)
print (json.dumps(decodedResponse, sort_keys=True, indent=4))
