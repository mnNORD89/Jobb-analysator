"""Huvudprogram för att analysera jobbannonser för AI-utvecklare."""

import argparse
import csv
from pathlib import Path

from job_analysis.analyzer import count_by_field, count_keyword_hits, make_job_objects
from job_analysis.api_handler import fetch_jobs
from job_analysis.visualizer import save_bar_chart

CSV_FILE = Path("data.csv")


def filter_jobs_by_region(jobs, region):
    if not region:
        return jobs
    region_name = region.lower()
    return [job for job in jobs if region_name in job.location.lower()]


def save_to_csv(jobs, filename=CSV_FILE):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["headline", "employer", "location", "webpage_url", "ai_focus"])
            for job in jobs:
                writer.writerow([job.headline, job.employer, job.location, job.url, job.ai_focus])
        print(f"Data sparades i {filename}.")
    except OSError as error:
        print(f"Kunde inte skriva CSV: {error}")


def main():
    parser = argparse.ArgumentParser(description="Analysera AI-jobbannonser från JobTech API.")
    parser.add_argument("--search-term", default="AI-utvecklare", help="Sökterm för JobTech API.")
    parser.add_argument("--limit", type=int, default=20, help="Antal annonser att hämta.")
    parser.add_argument("--region", default="", help="Valfri region att filtrera annonser på.")
    args = parser.parse_args()

    positions = fetch_jobs(args.search_term, limit=args.limit)
    if not positions:
        print("Inga jobb hittades. Testa ett annat sökord.")
        return

    jobs = make_job_objects(positions)
    jobs = filter_jobs_by_region(jobs, args.region)
    save_to_csv(jobs)

    print(f"\nTotalt antal jobb: {len(jobs)}")

    employer_count = count_by_field(jobs, "employer")
    print("\nVanligaste arbetsgivare:")
    for employer, count in employer_count.most_common(5):
        print(f"- {employer}: {count}")

    location_count = count_by_field(jobs, "location")
    print("\nVanligaste platser:")
    for place, count in location_count.most_common(5):
        print(f"- {place}: {count}")

    keyword_count = count_keyword_hits(jobs)
    print("\nVanliga sökord i annonserna:")
    for keyword, count in keyword_count.most_common(5):
        print(f"- {keyword}: {count}")

    save_bar_chart(employer_count, "Top arbetsgivare", "employers.png")
    save_bar_chart(location_count, "Top orter", "locations.png")
    save_bar_chart(keyword_count, "Vanliga nyckelord", "keywords.png")

    print("\nDiagram sparade i mappen charts/")


if __name__ == "__main__":
    main()
