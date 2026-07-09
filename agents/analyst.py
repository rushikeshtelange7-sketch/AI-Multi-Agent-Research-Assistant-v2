import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="meta-llama/llama-3.3-70b-instruct:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyst_agent(topic, research):

    prompt = f"""
    Topic:

    {topic}

    Research Data:

    {research}

    Summarize the important insights in 5 bullet points.
    """

    response = llm.invoke(prompt)

    return response.content