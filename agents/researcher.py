from tools.search_tool import search_web


def researcher_agent(topic):

    results = search_web(topic)

    if not results:

        return "No research results found."

    return results