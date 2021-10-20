import requests

key="Ha3bdUIhJW5hv9JASOtoiht9AmOW1fK7Hva75r2laT9h8HXD7kicJfkCMGYXsQ0SIwHCchWyVyMbH3QDUgBCb6pKBd5lsrbLauEWwJpsgaFU1ZTh3SNq08bqrXVwYXYx"

#from the tutorial; need this headers line to create a dictionary to hold the api key
headers = {'Authorization': 'Bearer {}'.format(key)}
api_url = 'https://api.yelp.com/v3/businesses/search/phone'
parameters = {'phone' : '+14349756796', 'locale': 'en_US'}

response = requests.get(api_url,headers=headers,params=parameters,timeout=5)

dict = response.json()
# This is what prints out: dict_keys(['businesses', 'total'])
# Keys are businesses and total

# prints out number of businesses found with that number
print(len(dict['businesses']))


#should print out the information for Orzo Kitchen & Wine Bar
print(dict['businesses'][0])




