import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("600x400")
        self.api_key = "47bd6ef51921a1a076d24c59c27c013c"  # Replace with your OpenWeatherMap API key

        self.create_widgets()

    def create_widgets(self):
        self.location_entry = tk.Entry(self, font=("Helvetica", 14))
        self.location_entry.pack(pady=20)

        self.search_button = tk.Button(self, text="Search", command=self.search_weather)
        self.search_button.pack()

        self.weather_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.weather_label.pack(pady=20)

        self.weather_icon = tk.Label(self)
        self.weather_icon.pack()

    def search_weather(self):
        location = self.location_entry.get()
        if location:
            weather_data = self.get_weather(location)
            if weather_data:
                self.display_weather(weather_data)
            else:
                messagebox.showerror("Error", "Failed to fetch weather data.")
        else:
            messagebox.showerror("Error", "Please enter a location.")

    def get_weather(self, location):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data

    def display_weather(self, weather_data):
        if weather_data["cod"] != 200:
            messagebox.showerror("Error", weather_data["message"])
        else:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            icon_id = weather_data['weather'][0]['icon']

            self.weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {description}")

            # Display weather icon
            icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
            icon_data = requests.get(icon_url).content
            icon_image = Image.open(icon_data)
            icon_image = icon_image.resize((50, 50), Image.ANTIALIAS)
            icon_photo = ImageTk.PhotoImage(icon_image)
            self.weather_icon.config(image=icon_photo)
            self.weather_icon.image = icon_photo

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
