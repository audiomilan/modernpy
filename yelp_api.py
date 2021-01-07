import requests


url = "https://api.yelp.com/v3/businesses/search"
api_key = "NqOVpGpc49yN41qxPCAVlfCFnaVRfe8UozWtMr2Gwd2vT3YVTI_NDEHJNWHJdZYxPi4W8a1dd2njJ-9CVAaFYLsfAFPG3Uc48i-8NMtNC78QqGZOn7JG6dAGujn3X3Yx"

headers = {
    "Authorization" : "Bearer " + api_key
}
params = {
    "term" : "Funeral Home",
    "location" : "Pittsburgh"
}

response = requests.get(url, headers=headers , params=params)
businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)
