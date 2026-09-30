# Jobbannonsanalys för AI-utvecklare

## Mål

Detta projekt analyserar jobbannonser för AI-relaterade roller i Sverige. Syftet är att se vilka arbetsgivare, orter och kompetenser som är vanligast i annonserna för ett yrke som AI-utvecklare.

## Metod

1. Hämta jobbannonser från JobTech API.
2. Normalisera och strukturera datan i objekt.
3. Spara resultatet i en CSV-fil.
4. Räkna antalet annonser per arbetsgivare, plats och nyckelord.
5. Visualisera resultaten i diagram.
6. Dokumentera resultatet i notebooket och i detta README.

## Teknisk lösning

Projektet använder:

- Python 3
- requests för API-anrop
- csv för filhantering
- collections.Counter för statistik
- klasser och arv för objektorienterad struktur
- matplotlib för diagram
- try/except för felhantering

Koden är nu uppdelad i separata moduler för bättre struktur och återanvändbarhet:

- `main.py` – programstart och körning
- `job_analysis/api_handler.py` – API-hantering
- `job_analysis/analyzer.py` – datamodell och analys
- `job_analysis/visualizer.py` – diagram och visualisering

## Projektstruktur

Projektet innehåller nu följande filer:

- `main.py` – huvudprogrammet
- `projekt.ipynb` – notebookversionen av projektet
- `data.csv` – sparad jobbdata
- `job_analysis/` – moduler för API, analys och visualisering
- `charts/` – genererade diagram
- `README.md` – projektinformation

## Extra funktionalitet

Projektet har utökats med:

- val av region via kommandoradsparameter
- diagram för arbetsgivare, platser och nyckelord
- modulär kodstruktur för bättre underhåll och skalbarhet

Exempel på körning:

```bash
python3 main.py --search-term "AI-utvecklare" --limit 20 --region "Stockholm"
```

## Resultat

Programmet kan:

- hämta jobbannonser från JobTech API
- skapa objekt från varje annons
- spara data i CSV-format
- räkna hur ofta olika arbetsgivare förekommer
- räkna hur ofta olika platser förekommer
- hitta vanliga tekniska sökord i annonserna
- skapa diagram som visar trender i data

Exempel på sökord som analyseras:

- Python
- AI
- SQL
- Azure
- AWS
- machine learning

## Analys

Genom att analysera annonserna får vi en tydlig bild av vilka kompetenser och arbetsplatser som är vanligast. Resultaten visar vilka områden som dominerar arbetsmarknaden för AI-relaterade roller och hjälper oss att förstå vilken typ av kunskap som efterfrågas mest.

## Reflektion

Det största lärdomarna i projektet var att arbeta med ett verkligt API och att förstå att data inte alltid kommer i den struktur man förväntar sig. Det krävdes felhantering och kontroll av svaren för att göra analysen robust. Jag lärde mig också att en tydlig modulär struktur gör lösningen enklare att testa, förbättra och underhålla. Detta har också gjort det enklare att lägga till visualisering och val av region.

## Relevanta certifikat

För arbete med AI, data och molntjänster kan följande certifikat vara relevanta:

- Azure AI Engineer Associate
- AWS Certified Machine Learning – Specialty
- Microsoft Azure Fundamentals
- AWS Cloud Practitioner

## Installation och körning

1. Skapa en virtuell miljö om du vill.
2. Installera beroenden:

```bash
pip install -r requirements.txt
```

3. Kör programmet:

```bash
python3 main.py --search-term "AI-utvecklare" --limit 20
```

4. Diagram sparas automatiskt i mappen `charts/`.

## GitHub-länk

[github.com/mnNORD89/Jobb-analysator.git](https://github.com/mnNORD89/Jobb-analysator.git)

## Slutsats

Detta projekt visar hur Python kan användas för att samla in, analysera och sammanfatta information från arbetsmarknaden. Det kombinerar datainsamling, struktur, statistik, visualisering och reflektion kring relevant kompetens för AI-yrken.

## Verifiering

Projektet har verifierats genom att köra programmet mot JobTech API och kontrollera att data hämtas, analyseras och sparas korrekt. Diagram skapades också utan att programmet kraschar.
