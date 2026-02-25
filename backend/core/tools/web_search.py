from duckduckgo_search import DDGS
from typing import List


def web_search(query: str) -> List[str]:
    """
    Search the web for the given query and return the results.

    Args:
        query (str): The query to search for.

    Returns:
        List[str]: The results of the search.
    """
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        return results
