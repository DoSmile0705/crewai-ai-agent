# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def pdf_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Tell me precisely what I need know from the RAG tool.
            Use this as what I want to lookup: {var1}
            
            {self.__tip_section()}
            
            Make sure to be as accurate as possible.
        """
            ),
            expected_output="Full analysis.",
            agent=agent,
        )

    def writer_task(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from task 1 and write a compelling narrative about it.                                       
            {self.__tip_section()}

            Make sure to do something else.
        """
            ),
            expected_output="Give me the title, then brief summary, then bullet points, and TLDR",
            agent=agent,
        )
