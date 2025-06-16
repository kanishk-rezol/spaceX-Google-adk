import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class OpenWeatherMapTool:
    def __call__(self, location: str, units: str = "metric") -> Dict[str, Any]:
        try:
            response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "q": location,
                    "units": units,
                    "appid": os.getenv("OPENWEATHERMAP_API_KEY")
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "wind_speed": data["wind"]["speed"],
                "conditions": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        except Exception as e:
            return {"error": f"Failed to fetch weather: {str(e)}"}
