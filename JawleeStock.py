import requests
import json
import time
import datetime
from datetime import date

watchList = []

headers = {
        'x-rapidapi-key': "ce893d5db6msh1745bc8abfd1f74p1fc1b4jsn919472a60eca",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

querystring = {"symbol":"TSLA","region":"US","frequency":"1mo"}


# Basic search for a stock
# Input: 
#   region: Region of the stock user is looking for
#   sym: Symbol of the stock user is looking for
# 
# Output: 
#   Returns a list with deltaday and moving average of a stock

def searchStock(region, sym):
    
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes'
    querystring = {"region":region,"symbols":sym}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    print(json.dumps(data,indent=2))
    print(len(data["prices"]))
    return data

# Retrieve the Historical Data of a stock from API
# Input: 
#   histData: data returned from getHistoricalData function
#   deltaday: how many days moving average e.g. 50 or 200 day moving average
# 
# Output: 
#   Returns a list with deltaday and moving average of a stock

def getHistoricalData(querystring):
    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"
   
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # data = response.json()
    with open('SampleResponses\getHistoricalDataSampleResponse.json') as file:
        data = json.load(file)

    return data
    # print(json.dumps(data,indent=2))
    # print(len(data["prices"]))


# Calculate the Moving Average of a stock
# Input: 
#   histData: data returned from getHistoricalData function
#   deltaday: how many days moving average e.g. 50 or 200 day moving average
# 
# Output: 
#   Returns a list with deltaday and moving average of a stock

def MovAvg(histData, deltaday):
    total = 0
    count = 0
    avg = 0

    histPrices = histData["prices"]

    for d in range(0,deltaday):
        dateObj = histPrices[d]["date"]
        dat = datetime.datetime.fromtimestamp(dateObj)
        total += histPrices[d]["close"]
        count += 1
    
    avg = total / count
    print (f'Count: {count}')
    print(f'"{deltaday} Day Moving Average: " {avg}')
    print("---------------------------------------------------------------------\n")

    return [deltaday,avg]


# Converts Epoch Time to Human Readable Format
# Input: 
#   e: Epoch Time
# 
# Output: 
#   Returns time in string format
def convertEpochTime(e):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(e))

def main():
    MovAvg(getHistoricalData(querystring),50)
    MovAvg(getHistoricalData(querystring),200)

if __name__ == "__main__":
    main()