from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'],2)
            lon = round(results[0]['geometry']['lng'],2)
            country = results[0]['components']['country']
            osm_url = f"openstreetmap.org/?mlat={lat}&mlon={lon}"

            if "state" in results[0]['components']:
                region = results[0]['components']['state']
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}. \n Регион: {region}",
                "map_url": osm_url
                        }
            else:
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}.",
                        "map_url": osm_url
                        }

        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"

def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f'Координаты города {city}:\n {result["coordinates"]}')
    map_url = result["map_url"]


def show_map():
    if map_url:
        webbrowser.open(map_url)


key = 'bae2871de12f4b3ea92b4f80fcfbb984'
map_url = ""

window = Tk()
window.title('Координаты городов')
window.geometry('500x400')

entry = Entry(window)
entry.pack()
entry.bind("<Return>", show_coordinates)


button = Button(window, text='Поиск координат', command=show_coordinates)
button.pack()

map_button = Button(window, text='Показать карту', command=show_map)
map_button.pack()

label = Label(window, text='Введите город и нажмите на кнопку')
label.pack()

window.mainloop()