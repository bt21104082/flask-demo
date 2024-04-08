import requests

url = 'http://127.0.0.1:5000/output-csv'

response = requests.get(url)

print(response.text)