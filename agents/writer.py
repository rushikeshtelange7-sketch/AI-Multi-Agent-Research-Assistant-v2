import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
)

def writer_agent(topic, analysis):

    prompt = f"""
You are a Professional Research Report Writer.

Topic:
{topic}

Analysis:
{analysis}

Create a professional report.

Include:

# Introduction

# Objectives

# Research Analysis

# Conclusion

# References

Make the report easy to understand and suitable for a college project.
"""

    response = llm.invoke(prompt)

    return response.content