import requests


url = "http://127.0.0.1:8000/price"
cart = int(input("Enter Diamond Cart"))
x = int(input("Enter Diamond x"))
y = int(input("Enter Diamond y"))
z = int(input("Enter Diamond z"))
#data that will be passed to the api
testing_data = {
    "cart": cart,
    "x": x,
    "y": y,
    "z": z 
    }

response = requests.post(url, json=testing_data)

if response.status_code == 200:
    print(response.json()[0],response.json()[1])

else:
    print(f"Error: {response.status_code}, {response.text}")
