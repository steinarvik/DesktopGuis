import requests
import FreeSimpleGUI as sg

# Replace with your OpenWeatherMap API key
API_KEY = "141710af2113bab9f55ef73e1bcd33d5"

def get_temperature(city):
    """Fetches the current temperature for a given city.

    Args:
      city: The name of the city to get weather data for.

    Returns:
      A string containing the current temperature in Fahrenheit or None if an error occurs.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        return f"Current temperature in {city}: {temp:.1f}°C"
    else:
        print(f"Error: {response.status_code}")
        return None

layout = [
    [sg.Text("Enter City:"), sg.InputText(key="city")],
    [sg.Button("Get Weather"), sg.Exit()],
    [sg.Text("", key="output")],
]

window = sg.Window("Weather App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    city = values["city"]
    temperature = get_temperature(city)
    window["output"].update(temperature or "Failed to retrieve temperature.")

window.close()
