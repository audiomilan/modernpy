#Studying making calls with API to get quotes in real time from Coin Market Cap

#Import Results, Sessions, Json, Results Exceptions for connection error, timeout and toomanyredirections

from requests import Result, Session
from requests.exceptions import ConnectionError, Timeout, Toomanyredirects
import json

# You want to head over to https://coinmarketapp.com/api and set up a basic account to get you a personal api key and read documentation
# which you will need to get the quotes you want using endpoints of url. I chose the default, which makes a API for following quotes

get_url = 'https://pro.api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#next you want to set your parameters in which you want to see the quotes. place them in a dictionary

parameters = {
    'start1' : '1' ,
    'limit' : '5000' ,
    'convert' : 'USD'
}
# Set your headers and give your api key
headers = {
    'Accepts' : 'application/json' ,
    'X-CMC_PRO_API_KEY' : #YOUR API GOES HERE
}

session = Session()
session.headers.update(headers)

#Creat a Try block for exceptions

try:
    response =session.get(url, parama=parameters)
    data = json.loads(response.txt)
    print(data)
except (ConnectionError , Timeout , Toomanyredirects) as e:
    print(e)



