from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool

# Flight Booking Agent: Specializes in flight booking and information
flightBooking_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o-mini"),
    name="FlightBookingAgent",
    description="Flight booking agent",
    instruction=f"""You are a flight booking agent, in the absence of information suggest the best options... You always return a valid JSON...""")

# Hotel Booking Agent: Specializes in hotel booking and information
hotelBookingAgent_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o-mini"),
    name="HotelBookingAgent",
    description="Hotel booking agent",
    instruction=f"""You are a hotel booking agent, in the absence of information suggest the best options... You always return a valid JSON...""")

# Travel Booking Agent: Specializes in providing sightseeing recommendations
travelBookingAgent = Agent(
    model=LiteLlm(model="openai/gpt-4o-mini"),
    name="TravelBookingAgent",
    description="Travel information agent",
    instruction=f"""You are a sightseeing information agent, in the absence of information suggest the best options... You always return a valid JSON...""")

# Convert specialized agents into AgentTools
flight_tool = AgentTool(agent=flightBooking_agent)
hotel_tool = AgentTool(agent=hotelBookingAgent_agent)
travel_tool = AgentTool(agent=travelBookingAgent)

# Root agent now uses these agents as tools
root_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o-mini"),
    name="TravelAssistant",
    instruction=f"""Acts as a comprehensive trip planner...
    Based on the user request, sequentially invoke the tools to gather all necessary trip details...""",
    tools=[flight_tool, hotel_tool, travel_tool] # The root agent can use these tools
)
