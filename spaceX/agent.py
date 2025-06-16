from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from .sub_agents.spacex_agent.agent import spacex_agent
from .sub_agents.weather_agent.agent import weather_agent
from .sub_agents.analysis_agent.agent import analysis_agent

root_agent = LlmAgent(
    name="spaceX_orchestrator",
    model="gemini-1.5-pro-latest",
    instruction="""
Output EXACTLY in this format:

1.Goal: Will the next SpaceX launch be delayed due to humidity?
Plan:
- Step 1: Get next SpaceX launch info
- Step 2: Fetch weather at that location
- Step 3: Assess delay risk based on humidity
2.Location: <location>
3.Weather:
- Temperature: <°C>
- Wind Speed: <m/s>
- Humidity: <%>
- Conditions: <desc>
4.Result: <launch is feasible / may be delayed based on humidity>
5.Agents Called: spacex_agent, weather_agent, analysis_agent
6.Summary: <one-line summary>

Return exactly these lines. No JSON, no extras.
""",
    sub_agents=[spacex_agent, weather_agent],
    tools=[AgentTool(analysis_agent)]
)
