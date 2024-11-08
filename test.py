import requests


url = "http://127.0.0.1:8000/price"

#data that will be passed to the api
testing_data = {
    "cart": 5,
    "x": 10,
    "y": 2,
    "z": 4 
    }

response = requests.post(url, json=testing_data)

if response.status_code == 200:
    print(response.json()[0],response.json()[1])

else:
    print(f"Error: {response.status_code}, {response.text}")