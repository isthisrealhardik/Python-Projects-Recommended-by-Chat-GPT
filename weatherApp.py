# a weather app with basic gui
# enter a city name to get several details about the cities weather using an interface not cli

import tkinter as tk
import requests
import json


cityValue = ''

root = tk.Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Weather App')

def getWeather():
    apiKey = "783cfc9479bde19c0ee6f1e0ced05ca4" 
    cityName = cityValue.get()
    responseApi = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={key}')
    data = responseApi.json()

    textField.delete('1.0', 'end')

    if data['cod'] == 200:
        kelvin = 273
        temp = int(data['main']['temp'] - kelvin)
        feels_like_temp = int(data['main']['feels_like'] - kelvin)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed'] * 3.6
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        timezone = data['timezone']
        cloudy = data['clouds']['all']
        description = data['weather'][0]['description']

        weather = f"\nWeather of: {cityName}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"

        textField.insert(INSERT, weather)


heading = tk.Label(root, text="Enter your city name", font="Arial 12 bold").pack(pady=10)
cityInput = tk.Entry(root, textvariable=cityValue, width=20, font="Arial 14 bold").pack()
cityButton = tk.Button(root, command=getWeather, text='Get Weather', font='Arial 10 bold').pack()
weatherNow = tk.Label(root, text="The Weather is:").pack()
textField = tk.Text(root).pack


root.mainloop()