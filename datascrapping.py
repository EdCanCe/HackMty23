import requests

ak = "SAJ8M4DTOL6CL1Q4"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey='+ak
r = requests.get(url)
data = r.json()

print(data)