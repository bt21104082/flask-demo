import requests

url = 'http://127.0.0.1:5000/calculate-csv'

str = input("do you want to fetch name or age from the csv file")

response = requests.post(url, data = {'data' : str})

print(response.text)