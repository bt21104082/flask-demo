import requests

url = 'http://127.0.0.1:5000/calculate'

color_red = '\033[91m'
color_reset = '\033[0m'

print(color_red + "Basic Arithematic calculator" + color_reset)
print("Addition \nSubstraction \nMultiplication \nDivision")
num1 = int(input("For Addition press-1, Substraction press-2, Multiplication press-3, Division press-4 : "))

print("enter two numbers : ")
num2 = int(input("enter first number : "))
num3 = int(input("enter second number : "))

response = requests.post(url, data={'data': f"{num1},{num2},{num3}"})

print("result is : ", response.text)