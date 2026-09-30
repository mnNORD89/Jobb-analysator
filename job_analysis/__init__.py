"""Jobbannonsanalysmodul."""

# Samla de vanligaste funktionerna och klasserna på paketnivå för enkel import.
from .analyzer import AI_Job_Annons, JobAnnons, count_by_field, count_keyword_hits, make_job_objects
from .api_handler import fetch_jobs

# Namn som ska räknas som paketets publika gränssnitt.
__all__ = [
    "AI_Job_Annons",
    "JobAnnons",
    "count_by_field",
    "count_keyword_hits",
    "fetch_jobs",
    "make_job_objects",
]
