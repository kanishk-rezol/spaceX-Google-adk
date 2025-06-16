from google.adk.agents import Agent

analysis_agent = Agent(
    name="analysis_agent",
    model="gemini-1.5-pro-latest",
    instruction="""
Given weather JSON, if humidity > 85 respond "launch may be delayed based on humidity", else "launch is feasible based on humidity"
"""
)
