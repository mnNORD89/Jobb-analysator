"""Hantering av JobTech API-anrop."""

import requests

API_URL = "https://jobsearch.api.jobtechdev.se/search?q="


def fetch_jobs(search_term, limit=20, region=None):
    """Hämtar annonser från JobTech API."""
    url = API_URL + search_term
    if region:
        url += f"&county={region}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        hits = data.get("hits", [])
        if not isinstance(hits, list):
            print("API:t returnerade ingen jobblista.")
            return []
        return hits[:limit]
    except requests.exceptions.RequestException as error:
        print(f"Nätverksfel: {error}")
        return []
    except ValueError as error:
        print(f"Fel i API-svaret: {error}")
        return []
