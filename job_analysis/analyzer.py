"""Analys- och datamodul för jobbannonser."""

from collections import Counter

KEYWORDS = ["python", "ai", "sql", "azure", "aws", "machine learning"]


class JobAnnons:
    def __init__(self, headline, employer, url, location):
        self.headline = headline
        self.employer = employer
        self.url = url
        self.location = location

    def __str__(self):
        return f"{self.headline} - {self.employer} ({self.location})"


class AI_Job_Annons(JobAnnons):
    def __init__(self, headline, employer, url, location, ai_focus=False):
        super().__init__(headline, employer, url, location)
        self.ai_focus = ai_focus


def make_job_objects(positions):
    jobs = []
    for job in positions:
        headline = job.get("headline") or "Okänd titel"
        employer = job.get("employer", {}).get("name") or "Okänd arbetsgivare"
        url = (
            job.get("webpage_url")
            or job.get("application_details", {}).get("url")
            or job.get("url")
            or "Ingen länk"
        )
        location = job.get("workplace_address", {}).get("municipality") or "Okänd ort"

        text = (headline + " " + employer + " " + location).lower()
        ai_focus = any(word in text for word in ["ai", "machine learning", "python", "sql", "azure", "aws"])

        jobs.append(AI_Job_Annons(headline, employer, url, location, ai_focus))
    return jobs


def count_by_field(jobs, field_name):
    counter = Counter()
    for job in jobs:
        value = getattr(job, field_name)
        counter[value] += 1
    return counter


def count_keyword_hits(jobs, keywords=None):
    counter = Counter()
    keyword_list = keywords or KEYWORDS
    for job in jobs:
        text = (job.headline + " " + job.employer + " " + job.location).lower()
        for keyword in keyword_list:
            if keyword in text:
                counter[keyword] += 1
    return counter
