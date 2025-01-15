from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)


    def pdf_agent(self):
        pdf_tool = PDFSearchTool("example.pdf")

        return Agent(
            role="Senior PDF Analyst",
            backstory=dedent(f"""You can find anything in a pdf. The people need you."""),
            goal=dedent(f"""Discover any information from pdf files exceptionally well."""),
            tools=[pdf_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def writer_agent(self):
        return Agent(
            role="Writer",
            backstory=dedent(f"""All your lifes you have loved writing summaries."""),
            goal=dedent(f"""Take the information from the pdf agent and summarize it nicely"""),
            verbose=True,
            llm=self.OpenAIGPT35,
        )
