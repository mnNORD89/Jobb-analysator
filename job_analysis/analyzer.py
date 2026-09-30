"""Analys- och datamodul för jobbannonser."""

from collections import Counter

# Ord som räknas i annonsernas rubrik, arbetsgivare och ort.
KEYWORDS = ["python", "ai", "sql", "azure", "aws", "machine learning"]


class JobAnnons:
    # Samlar de grundläggande uppgifterna som finns för varje annons.
    def __init__(self, headline, employer, url, location):
        self.headline = headline
        self.employer = employer
        self.url = url
        self.location = location

    def __str__(self):
        # Ger en kort och läsbar textversion av jobbobjektet.
        return f"{self.headline} - {self.employer} ({self.location})"


class AI_Job_Annons(JobAnnons):
    # Ärver grunduppgifterna och lägger till en markering för AI-fokus.
    def __init__(self, headline, employer, url, location, ai_focus=False):
        super().__init__(headline, employer, url, location)
        self.ai_focus = ai_focus


def make_job_objects(positions):
    # API:t ger dictionaries; här omvandlas varje träff till ett Python-objekt.
    jobs = []
    for job in positions:
        # Använd reservtext om API-svaret saknar någon av uppgifterna.
        headline = job.get("headline") or "Okänd titel"
        employer = job.get("employer", {}).get("name") or "Okänd arbetsgivare"
        # Länken kan finnas på olika ställen i API-svaret.
        url = (
            job.get("webpage_url")
            or job.get("application_details", {}).get("url")
            or job.get("url")
            or "Ingen länk"
        )
        location = job.get("workplace_address", {}).get("municipality") or "Okänd ort"

        # Kontrollera om någon relevant term finns i rubrik, arbetsgivare eller ort.
        text = (headline + " " + employer + " " + location).lower()
        ai_focus = any(word in text for word in ["ai", "machine learning", "python", "sql", "azure", "aws"])

        # Lägg till det färdiga objektet i resultatlistan.
        jobs.append(AI_Job_Annons(headline, employer, url, location, ai_focus))
    return jobs


def count_by_field(jobs, field_name):
    # Counter håller reda på hur många gånger varje fältvärde förekommer.
    counter = Counter()
    for job in jobs:
        # getattr läser det attribut vars namn skickats in, till exempel "employer".
        value = getattr(job, field_name)
        counter[value] += 1
    return counter


def count_keyword_hits(jobs, keywords=None):
    counter = Counter()
    # Egna sökord kan skickas in; annars används projektets standardlista.
    keyword_list = keywords or KEYWORDS
    for job in jobs:
        # Sökningen görs utan skillnad mellan stora och små bokstäver.
        text = (job.headline + " " + job.employer + " " + job.location).lower()
        for keyword in keyword_list:
            if keyword in text:
                # Öka räknaren en gång för varje annons som innehåller ordet.
                counter[keyword] += 1
    return counter
