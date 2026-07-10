import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
)

def analyst_agent(topic, research):

    prompt = f"""
You are an AI Research Analyst.

Topic:
{topic}

Research Data:
{research}

Create a professional analysis.

Include:

• Key Insights

• Advantages

• Challenges

• Future Scope

Write using bullet points.
"""

    response = llm.invoke(prompt)

    return response.content