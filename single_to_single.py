import requests

url = 'http://127.0.0.1:5000/post'

input1 = input("Enter some single string: ")

response = requests.post(url, data={'data': input1})

print(response.text)