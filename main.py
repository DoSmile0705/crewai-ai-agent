import os
from crewai import Crew, Task, Agent
from dotenv import load_dotenv

load_dotenv()

# Use the OPENAI_API_KEY from dotenv
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

# Define the agent
info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
        You love to know information. People love and hate you for it. You win most of the
        quizzes at your local pub.
    """
)

# Define the task
task = Task(
    description="Tell me all about the blue-ringed octopus",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it",
    agent=info_agent
)

# Create the crew
crew = Crew(
    agents=[info_agent],
    tasks=[task],
    verbose=True
)

# Kickoff the task
result = crew.kickoff()
print(result)
