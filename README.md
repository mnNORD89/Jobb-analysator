# Jobbannonsanalys för AI-utvecklare

## Mål

Detta projekt analyserar jobbannonser för AI-relaterade roller i Sverige. Syftet är att identifiera vilka arbetsgivare, orter och tekniska kompetenser som dominerar marknaden för AI-utvecklare.

## Metod

1. Läs jobbannonser från `data.csv`.
2. Normalisera och strukturera datan i objekt.
3. Filtrera annonserna efter ort om ett regionval har angetts.
4. Räkna antalet annonser per arbetsgivare, plats och nyckelord.
5. Visa sammanställningen och enkla stapeldiagram direkt i notebooken.
6. Dokumentera resultatet i notebooken och i detta README.

## Teknisk lösning

Projektet använder:

- Python 3
- csv för filhantering
- collections.Counter för statistik
- klasser och arv för objektorienterad struktur
- try/except för felhantering
- ipykernel för att köra notebooken
- matplotlib för att visa diagram över arbetsgivare och orter

Programmets kod finns samlad i olika celler i notebooken. Cellerna körs uppifrån och ned:

- `projekt.ipynb` – hela programmet och dess stegvisa resultat

Detta visar att projektet inte bara löser uppgiften utan också använder ett mer professionellt arbetssätt för större lösningar.

## Projektstruktur

Projektet innehåller nu följande filer:

- `projekt.ipynb` – huvudprogrammet, uppdelat i notebookceller
- `data.csv` – jobbdata som läses in och analyseras
- `README.md` – projektinformation

## Extra funktionalitet

Projektet har utökats med:

- valfri filtrering efter ort direkt i notebooken
- analys av arbetsgivare, orter och tekniska nyckelord
- stapeldiagram som jämför de vanligaste arbetsgivarna och orterna

Regionfiltret finns i cell 7 i `projekt.ipynb`.

## Resultat

Programmet kan:

- läsa in jobbannonser från CSV-filen
- skapa objekt från varje annons
- filtrera annonser efter ort
- räkna hur ofta olika arbetsgivare förekommer
- räkna hur ofta olika platser förekommer
- hitta vanliga tekniska sökord i annonserna
- visa arbetsgivare och orter i stapeldiagram direkt i notebooken

Det kombinerar dataanalys, statistik och visualisering i en samlad notebook.

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

De största lärdomarna i projektet var att läsa in data från en CSV-fil och förstå att data behöver kontrolleras innan analys. Genom att dela upp notebooken i celler blir arbetsflödet lättare att följa och testa steg för steg.

## Relevanta certifikat

För arbete med AI, data och molntjänster kan följande certifikat vara relevanta:

- Azure AI Engineer Associate
- AWS Certified Machine Learning – Specialty
- Microsoft Azure Fundamentals
- AWS Cloud Practitioner

## Installation och körning

1. Skapa och aktivera en virtuell miljö:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Installera beroenden:

```bash
python -m pip install ipykernel matplotlib
```

3. Öppna `projekt.ipynb` i VS Code, välj `.venv` som notebook-kärna och kör cellerna uppifrån och ned. CSV-filen läses i cell 7; ange en ort där om du vill filtrera resultatet.

4. Resultaten visas i notebooken. `data.csv` används som indata och skrivs inte över.

## GitHub-länk

[github.com/mnNORD89/Jobb-analysator.git](https://github.com/mnNORD89/Jobb-analysator.git)

## Slutsats

Detta projekt visar hur Python kan användas för att läsa in, analysera, visualisera och sammanfatta information från arbetsmarknaden. Det kombinerar datastrukturering, statistik och reflektion kring relevant kompetens för AI-yrken.

## Verifiering

Projektet har verifierats genom att läsa `data.csv` i notebooken, kontrollera analysen och visa diagrammen.

Det visar att lösningen inte bara är teoretisk; den fungerar i praktiken och kan användas för vidare analys och presentation.
