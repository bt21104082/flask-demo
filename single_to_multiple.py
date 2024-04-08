import requests

url = 'http://127.0.0.1:5000/multple-post'

input2 = input("enter the things you know")

response = requests.post(url, data = {'data' : input2})

print(response.text)