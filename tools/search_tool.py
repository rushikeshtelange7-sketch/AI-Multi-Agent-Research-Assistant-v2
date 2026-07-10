from ddgs import DDGS


def search_web(query):

    results = []

    try:

        with DDGS() as ddgs:

            search_results = ddgs.text(query, max_results=5)

            for item in search_results:

                title = item.get("title", "No Title")
                body = item.get("body", "No Description")
                url = item.get("href", "")

                results.append(
                    f"""
Title:
{title}

Description:
{body}

Source:
{url}
"""
                )

    except Exception as e:

        return f"Search Error: {e}"

    return "\n\n".join(results)