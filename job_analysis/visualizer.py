"""Visualisering av analysdata."""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_bar_chart(data, title, filename, xlabel="", ylabel="Antal"):
    """Sparar ett stapeldiagram i en mapp."""
    os.makedirs("charts", exist_ok=True)
    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color="#4C78A8")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f"charts/{filename}", dpi=200)
    plt.close()

    return f"charts/{filename}"
