import requests
import json
ak = "SAJ8M4DTOL6CL1Q4"

def getData(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey='+ak
    r = requests.get(url)
    dataAux = r.json()
    data = json.loads(dataAux)
    data = data[1]
    return data

s1 = "AAPL"
s2 = "IBM"

d1 = getData(s1)
for i in range(d1.size()):
    print(d1[i].open)