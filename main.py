"""Huvudprogram för att analysera jobbannonser för AI-utvecklare."""

import argparse
import csv
from pathlib import Path

# Huvudfilen kopplar ihop API-hämtning, analys, CSV och diagram.
from job_analysis.analyzer import count_by_field, count_keyword_hits, make_job_objects
from job_analysis.api_handler import fetch_jobs
from job_analysis.visualizer import save_bar_chart

# Standardfilen där de hämtade och filtrerade annonserna sparas.
CSV_FILE = Path("data.csv")


def filter_jobs_by_region(jobs, region):
    # Utan regionval ska alla hämtade annonser behållas.
    if not region:
        return jobs
    # Jämför med små bokstäver så att stora och små bokstäver inte spelar roll.
    region_name = region.lower()
    return [job for job in jobs if region_name in job.location.lower()]


def save_to_csv(jobs, filename=CSV_FILE):
    try:
        # "w" skapar filen eller skriver över den; UTF-8 hanterar svenska tecken.
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Första raden beskriver vad värdena i varje efterföljande rad betyder.
            writer.writerow(["headline", "employer", "location", "webpage_url", "ai_focus"])
            for job in jobs:
                # Varje jobbobjekt blir en egen rad i CSV-filen.
                writer.writerow([job.headline, job.employer, job.location, job.url, job.ai_focus])
        print(f"Data sparades i {filename}.")
    except OSError as error:
        # Fångar till exempel problem med behörighet eller en ogiltig sökväg.
        print(f"Kunde inte skriva CSV: {error}")


def main():
    # Kommandoradsval gör det möjligt att välja sökord, antal annonser och region.
    parser = argparse.ArgumentParser(description="Analysera AI-jobbannonser från JobTech API.")
    parser.add_argument("--search-term", default="AI-utvecklare", help="Sökterm för JobTech API.")
    parser.add_argument("--limit", type=int, default=20, help="Antal annonser att hämta.")
    parser.add_argument("--region", default="", help="Valfri region att filtrera annonser på.")
    args = parser.parse_args()

    # Hämtar rå annonser från API:t med de val som användaren angav.
    positions = fetch_jobs(args.search_term, limit=args.limit)
    if not positions:
        # Avsluta tidigt om API:t inte gav några annonser att analysera.
        print("Inga jobb hittades. Testa ett annat sökord.")
        return

    # Gör om API-datan till jobbobjekt och filtrerar sedan eventuellt på region.
    jobs = make_job_objects(positions)
    jobs = filter_jobs_by_region(jobs, args.region)
    save_to_csv(jobs)

    # Räkna hur många annonser som återstår efter regionfiltret.
    print(f"\nTotalt antal jobb: {len(jobs)}")

    # Räkna annonser per arbetsgivare och skriv ut de fem vanligaste.
    employer_count = count_by_field(jobs, "employer")
    print("\nVanligaste arbetsgivare:")
    for employer, count in employer_count.most_common(5):
        print(f"- {employer}: {count}")

    # Gör samma sammanställning för annonsens ort.
    location_count = count_by_field(jobs, "location")
    print("\nVanligaste platser:")
    for place, count in location_count.most_common(5):
        print(f"- {place}: {count}")

    # Räknar vilka av de förinställda kompetensorden som förekommer oftast.
    keyword_count = count_keyword_hits(jobs)
    print("\nVanliga sökord i annonserna:")
    for keyword, count in keyword_count.most_common(5):
        print(f"- {keyword}: {count}")

    # Spara en separat stapelbild för varje typ av sammanställning.
    save_bar_chart(employer_count, "Top arbetsgivare", "employers.png")
    save_bar_chart(location_count, "Top orter", "locations.png")
    save_bar_chart(keyword_count, "Vanliga nyckelord", "keywords.png")

    print("\nDiagram sparade i mappen charts/")


if __name__ == "__main__":
    # Kör huvudflödet bara när filen startas direkt, inte när den importeras.
    main()
