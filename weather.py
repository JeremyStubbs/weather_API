import requests

API_key = '187413fb14e195bb9d965a8e8714435c'
city_name = input("Enter a city name: ")

base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    print (data)
else:
    print("An error")
