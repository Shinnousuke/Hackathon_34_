def route_query(query, pdf_uploaded=False):

    query = query.lower()

    web_keywords = [
        "latest",
        "news",
        "breaking",
        "current events",
        "stock market",
        "share price",
        "weather",
        "today news"
    ]

    if any(word in query for word in web_keywords):
        return "web"

    if pdf_uploaded:
        return "rag"

    return "llm"