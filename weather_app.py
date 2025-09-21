# Weather Forecast Application Refactored (OOP & Modular)

class WeatherDataFetcher:
    """Handles fetching weather data for a given city."""
    
    def __init__(self):
        # Simulated weather database
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch(self, city):
        """Return weather data dictionary for the city."""
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})


class DataParser:
    """Parses weather data dictionaries and formats output."""

    @staticmethod
    def parse(data):
        """Parse the weather data and return a formatted string."""
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature}°F, {condition}, Humidity: {humidity}%"


class UserInterface:
    """Handles user interaction for the weather forecast application."""

    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def display_weather(self, city):
        """Display weather for a city."""
        data = self.fetcher.fetch(city)
        if not data:
            print(f"Weather data not available for {city}")
            return f"Weather data not available for {city}"
        else:
            weather_report = self.parser.parse(data)
            print(weather_report)
            return weather_report

    def get_detailed_forecast(self, city):
        """Return detailed forecast string."""
        data = self.fetcher.fetch(city)
        return self.parser.parse(data)

    def run(self):
        """Main loop for user interaction."""
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                print("Exiting Weather Forecast Application.")
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)


# -----------------------------
# Run the application
# -----------------------------
if __name__ == "__main__":
    ui = UserInterface()
    ui.run()

