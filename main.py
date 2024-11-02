import PySimpleGUI as sg
import requests

API_KEY = '8dc2a7b590f6f9b596bb9c4327dd695e'

layout = [
    [sg.Input(
        key='-CITY_NAME-',
        size=(85, 5), 
        border_width=0,
        font=('Arial', 14),
        justification='center',
        pad=(0,10)
    ), sg.Button('Ok', visible=False, bind_return_key=True)],
    [sg.Column([
        [sg.Text('', key='-TEXT1-', font=('Arial', 16), pad=(1,30), background_color='#270763')],
        [sg.Text('', key='-TEXT2-', font=('Arial', 16), background_color='#270763')]
    ], justification='center', element_justification='center', background_color='#270763')] 
]

window = sg.Window('Weather', layout, size=(500, 300), background_color='#270763', finalize=True)

while True:
    event, values = window.read(timeout=100)

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Ok' or event == 'Return:13':
        city_name = values['-CITY_NAME-']
        call = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
        response = requests.get(call)
        data = response.json()

        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']

        window['-TEXT1-'].update(f'Temperature: {temperature:.0f}°C\n')
        window['-TEXT2-'].update(f'Feels Like: {feels_like:.0f}°C')

window.close()