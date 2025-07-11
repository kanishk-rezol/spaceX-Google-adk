## 🚀 SpaceX Launch Delay Analyzer (Google ADK)
This project uses Google Agent Development Kit (ADK) to orchestrate multiple AI agents and determine if the next SpaceX launch might be delayed due to weather, especially humidity.

## 🤖 Agents Involved
spacex_agent: Fetches the next SpaceX launch details (name, date, location).

weather_agent: Gets real-time weather data for the launch site.

analysis_agent: Analyzes the weather to decide if the launch may be delayed.

## 🧠 Orchestrator Agent
The root_agent coordinates all agents, processes the data, and returns a final decision in a clean, 6-line formatted report.

## 📋 Example Output

1.Goal: Will the next SpaceX launch be delayed due to humidity?
Plan:
- Step 1: Get next SpaceX launch info
- Step 2: Fetch weather at that location
- Step 3: Assess delay risk based on humidity
2.Location: Cape Canaveral
3.Weather:
- Temperature: 28°C
- Wind Speed: 6 m/s
- Humidity: 88%
- Conditions: Clear
4.Result: launch may be delayed based on humidity
5.Agents Called: spacex_agent, weather_agent, analysis_agent
6.Summary: High humidity detected—delay likely.

## 🛠 Tech Stack
Google ADK

Gemini 1.5 Pro

SpaceX API

OpenWeatherMap API

Python 3

## ✅ How it Works
The orchestrator gets launch details.

It queries weather conditions using tools.

The system analyzes humidity to check delay risk.

Outputs a human-readable final assessment.

## Download requierments 
```bash 
pip install -r requirements.txt
```
## Clone the Repo
```bash
git clone https://github.com/kanishk-rezol/spaceX-Google-adk
``` 
<h1 align="center"><strong>ALL DONE BYEE</strong></h1>
