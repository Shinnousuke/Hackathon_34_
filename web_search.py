from duckduckgo_search import DDGS


def search_web(query):

    try:

        results = []

        with DDGS(timeout=20) as ddgs:

            for r in ddgs.text(
                query,
                max_results=5
            ):
                results.append(r)

        return results

    except Exception as e:

        return [
            {
                "body": f"Search failed: {str(e)}"
            }
        ]