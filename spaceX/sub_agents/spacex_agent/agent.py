
from google.adk.agents import Agent
# import requests, datetime

spacex_agent = Agent(  
    name="spacex_agent",
    model="gemini-1.5-pro-latest",
    instruction="""
Fetch next SpaceX launch via SpaceX API and return JSON:
{"launch_name": "...", "date": "YYYY-MM-DD", "time": "HH:MM", "location": "..."}
"""
)
