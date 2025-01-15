import os
from crewai import Crew, Task, Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
	model="phi3:3.8b",
	base_url="http://localhost:11434/v1",
)

# Set environment variables correctly
os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

# Define the agent
info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
        You love to know information. People love and hate you for it. You win most of the
        quizzes at your local pub.
    """,
    llm=llm
)

# Define the task
task = Task(
    description="Tell me all about the box jellyfish",
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
