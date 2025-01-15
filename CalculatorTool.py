from langchain_community.tools import tool

@tool("Calculate")
def calculate(equation):
	""" Useful for solving math equation """
	
	return eval(equation)