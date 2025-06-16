from google.adk.agents import Agent
from ...tools.weather_tool import OpenWeatherMapTool

weather_agent = Agent(
    name="weather_agent",
    model="gemini-1.5-pro-latest",
    instruction="Use the tool to fetch weather JSON with keys temperature, wind_speed, humidity, conditions.",
    tools=[OpenWeatherMapTool()]
)
