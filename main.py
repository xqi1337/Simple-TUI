#!/usr/bin/python
# main.py

# Einstiegspunkt (Menü & Steuerung)

import sys
from ui import UI
from core import aufgabe_1, aufgabe_2, aufgabe_3

def main():
    ui = UI()
    try:
        while True:
            ui.display_menu()
            command = ui.input_prompt("MENU")

            match command:
                case "0":
                    sys.exit()
                case "1":
                    aufgabe_1(ui)
                case "2":
                    aufgabe_2(ui)
                case "3":
                    aufgabe_3(ui)
                case _:
                    ui.task_header()
                    ui.message("error", "Ungültige Eingabe! Bitte erneut versuchen.")
                    ui.print_centered(ui.bottom_border)
                    ui.input_prompt("Press Enter to return to menu")
    except KeyboardInterrupt:
        print("\n[!] Programm wurde manuell beendet.")

if __name__ == "__main__":
    main()
