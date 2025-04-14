#!/usr/bin/python
# core/tasks.py

# Aufgabenlogik (z. B. sortieren, analysieren)

import os
from random import randint
from process import save_to_file, read_numbers_from_file, calculate_average_and_max

def aufgabe_1(ui):
    """Aufgabe 1: Zufallszahlen generieren, sortieren, analysieren und speichern."""
    ui.task_header()

    path = "./"
    input_filename = "output.txt"
    output_filename = "processed_output.txt"

    try:
        # 1. Zufallszahlen erzeugen und speichern
        numbers = [randint(1, 100) for _ in range(10)]
        success, msg = save_to_file(path, input_filename, [str(n) for n in numbers])
        if not success:
            raise Exception(msg)

        # 2. Zahlen aus Datei lesen
        filepath = os.path.join(path, input_filename)
        numbers = read_numbers_from_file(filepath)

        # 3. Zahlen sortieren + Durchschnitt & Maximum berechnen
        numbers.sort()
        average, maximum = calculate_average_and_max(numbers)

        # 4. Ergebnisse speichern
        output_lines = ["Sortierte Zahlen:"]
        output_lines.extend([str(num) for num in numbers])
        output_lines.append(f"\nDurchschnittliche Zahl: {average}")
        output_lines.append(f"Maximale Zahl: {maximum}")

        success, msg = save_to_file(path, output_filename, output_lines)
        if not success:
            raise Exception(msg)

        # 5. Ergebnisse anzeigen
        output = " | ".join([str(num) for num in numbers])
        ui.print_centered(output)
        ui.print_centered(f"Durchschnitt: {average} | Maximum: {maximum}")
        ui.message("success", "Task completed successfully")

    except Exception as e:
        ui.message("error", f"Fehler beim Verarbeiten der Datei: {e}")

    ui.print_centered(ui.bottom_border)
    ui.input_prompt("Press Enter to return to menu")


def aufgabe_2(ui):
    """Aufgabe 2: Noch nicht implementiert."""
    ui.task_header()
    ui.print_centered("Task 2 functionality not yet implemented")
    ui.print_centered(ui.bottom_border)
    ui.input_prompt("Press Enter to return to menu")


def aufgabe_3(ui):
    """Aufgabe 3: Noch nicht implementiert."""
    ui.task_header()
    ui.print_centered("Task 3 functionality not yet implemented")
    ui.print_centered(ui.bottom_border)
    ui.input_prompt("Press Enter to return to menu")
