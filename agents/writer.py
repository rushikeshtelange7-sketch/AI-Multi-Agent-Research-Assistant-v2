import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="meta-llama/llama-3.3-70b-instruct:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def writer_agent(topic, analysis):

    prompt = f"""
    Create a professional research report.

    Topic:

    {topic}

    Analysis:

    {analysis}

    Include:

    1. Introduction

    2. Key Findings

    3. Conclusion

    Keep it concise and professional.
    """

    response = llm.invoke(prompt)

    return response.content