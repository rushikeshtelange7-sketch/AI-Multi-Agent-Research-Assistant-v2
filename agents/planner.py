import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
)

def planner_agent(topic):

    prompt = f"""
You are an AI Research Planner.

Create a professional research plan.

Topic:
{topic}

Requirements:

1. Introduction
2. Background
3. Current Technologies
4. Advantages and Challenges
5. Future Scope

Return only the plan.
"""

    response = llm.invoke(prompt)

    return response.content