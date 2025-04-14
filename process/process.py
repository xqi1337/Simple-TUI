#!/usr/bin/python
# process.py

# Helferfunktionen für Datenverarbeitung (z. B. Dateioperationen, Berechnungen)

import os

def save_to_file(path, filename, content_lines):
    """Speichert eine Liste von Textzeilen in eine Datei."""
    try:
        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, filename)
        with open(full_path, "w", encoding="utf-8") as f:
            for line in content_lines:
                f.write(f"{line}\n")
        return True, full_path
    except Exception as e:
        return False, str(e)


def read_numbers_from_file(filepath):
    """Liest eine Liste von Ganzzahlen aus einer Datei."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [int(line.strip()) for line in f.readlines()]
    except Exception as e:
        raise ValueError(f"Fehler beim Einlesen der Datei: {e}")


def calculate_average_and_max(numbers):
    """Berechnet Durchschnitt und Maximum einer Zahlenliste."""
    if not numbers:
        return 0, None
    average = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return average, maximum
