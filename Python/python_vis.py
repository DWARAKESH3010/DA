import requests
import json

'''
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
response = requests.get(url)
    
if response.status_code == 200:
    data = response.json()
    last_refreshed = data["Meta Data"]["3. Last Refreshed"]
    price = data["Time Series (5min)"][last_refreshed]["1. open"]
    print(price) 
else:
    print(None)

'''

url = "https://api.github.com/search/repositories?q=language:Javascript"
response = requests.get(url)
print(response)

if response.status_code == 200:
    data = response.json()
    count = 0
    
    for item in data["items"]:
        print("ID: ",item["id"])
        print("Name: " , item["name"])
        print("private: ",item["private"])
        print("Type: ",item["owner"]["type"])
        print("user_view_type: ",item["owner"]["user_view_type"])
        print("description: ",item["description"])
        print(" ")
        print(" ")
        count = count + 1
    print("The total count is ",count)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


