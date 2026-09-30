"""Hantering av JobTech API-anrop."""

import requests

# Basadressen för JobTechs sök-API; sökordet läggs till i fetch_jobs.
API_URL = "https://jobsearch.api.jobtechdev.se/search?q="


def fetch_jobs(search_term, limit=20, region=None):
    """Hämtar annonser från JobTech API."""
    # Bygg URL:en med sökord och lägg till länets kod om region har angetts.
    url = API_URL + search_term
    if region:
        url += f"&county={region}"

    try:
        # Timeout hindrar programmet från att vänta obegränsat på API:t.
        response = requests.get(url, timeout=15)
        # Om HTTP-anropet misslyckades kastas ett RequestException-fel.
        response.raise_for_status()
        data = response.json()
        # API-svaret ska innehålla en lista med annonser under nyckeln "hits".
        hits = data.get("hits", [])
        if not isinstance(hits, list):
            print("API:t returnerade ingen jobblista.")
            return []
        # Begränsa antalet annonser som skickas vidare till analysen.
        return hits[:limit]
    except requests.exceptions.RequestException as error:
        # Hanterar nätverksproblem och HTTP-fel.
        print(f"Nätverksfel: {error}")
        return []
    except ValueError as error:
        # Hanterar exempelvis ett svar som inte går att läsa som JSON.
        print(f"Fel i API-svaret: {error}")
        return []
