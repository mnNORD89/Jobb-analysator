
# Jobbannonsanalys för AI-utvecklare

## Mål
Detta projekt analyserar jobbannonser för AI-relaterade roller i Sverige. Syftet är att se vilka arbetsgivare, orter och kompetenser som är vanligast i annonserna för ett yrke som AI-utvecklare.

## Metod
1. Hämta jobbannonser från JobTech API.
2. Spara resultatet i en CSV-fil.
3. Tolka och sammanfatta data med Python.
4. Räkna antalet annonser per arbetsgivare, plats och relevanta nyckelord.
5. Dokumentera resultatet i notebooket och i detta README.

## Teknisk lösning
Projektet använder:
- Python
- requests för API-anrop
- csv för filhantering
- collections.Counter för statistik
- klasser och arv för objektorienterad struktur
- try/except för felhantering

Det är byggt som ett Jupyter Notebook och körs i projekt.ipynb.

## Projektstruktur
Detta projekt innehåller bara dessa tre filer:
- projekt.ipynb – huvudprogram och analys
- data.csv – sparad jobbdata
- README.md – projektinformation

## Resultat
Programmet kan:
- hämta jobbannonser från JobTech API
- skapa objekt från varje annons
- spara data i CSV-format
- räkna hur ofta olika arbetsgivare förekommer
- räkna hur ofta olika platser förekommer
- hitta vanliga tekniska sökord i annonserna

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
Det största lärdomarna i projektet var att arbeta med ett verkligt API och att förstå att data inte alltid kommer i den struktur man förväntar sig. Det krävdes felhantering och kontroll av svaren för att göra analysen robust. Jag lärde mig också att ett enklare och tydligare upplägg ofta är bättre än en mer avancerad lösning.

## Relevanta certifikat
För arbete med AI, data och molntjänster kan följande certifikat vara relevanta:
- Azure AI Engineer Associate
- AWS Certified Machine Learning – Specialty
- Microsoft Azure Fundamentals
- AWS Cloud Practitioner

## Installation och körning
1. Öppna projektet i Jupyter Notebook eller VS Code.
2. Kör cellerna i projekt.ipynb i ordning.
3. Notebooket hämtar jobbdata automatiskt från JobTech API och sparar den i data.csv.

## GitHub-länk
Sätt in din faktiska GitHub-länk här.

## Slutsats
Detta projekt visar hur Python kan användas för att samla in, analysera och sammanfatta information från arbetsmarknaden. Det kombinerar datainsamling, struktur, statistik och reflektion kring relevant kompetens för AI-yrken.
