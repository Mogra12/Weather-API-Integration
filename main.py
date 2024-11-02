import requests
import PySimpleGUI as sg

API_KEY = '8dc2a7b590f6f9b596bb9c4327dd695e'

layout = [
    [sg.Input(key='-CITY_NAME-'), sg.Button('Ok')],
    [sg.Column([
        [sg.Text('', key='-TEXT1-'), sg.Text('', key='-TEXT2-')]],  # Coloque os Texts dentro de uma lista
        justification='center')
    ]
]

window = sg.Window('Weather', layout, size=(400, 200))

while True:
    event, values = window.read(timeout=100)

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Ok':
        city_name = values['-CITY_NAME-']
        call = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
        response = requests.get(call)
        data = response.json()

        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']

        window['-TEXT1-'].update(f'Temperature: {temperature}°C')
        window['-TEXT2-'].update(f'Feels Like: {feels_like}°C')

window.close()