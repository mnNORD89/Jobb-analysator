"""Visualisering av analysdata."""

import os

import matplotlib
# Välj ett bakgrundsläge så diagram kan sparas även utan ett öppet grafikfönster.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_bar_chart(data, title, filename, xlabel="", ylabel="Antal"):
    """Sparar ett stapeldiagram i en mapp."""
    # Skapa diagrammappen vid behov; gör inget om den redan finns.
    os.makedirs("charts", exist_ok=True)
    # Counter eller dict delas upp i etiketter (namn) och stapelhöjder (antal).
    labels = list(data.keys())
    values = list(data.values())

    # Skapa diagrammet och märk det så att resultatet blir begripligt.
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color="#4C78A8")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    # Spara bilden med hög upplösning och stäng figuren för att frigöra minne.
    plt.savefig(f"charts/{filename}", dpi=200)
    plt.close()

    # Returnera sökvägen så att anroparen kan använda eller visa den.
    return f"charts/{filename}"
