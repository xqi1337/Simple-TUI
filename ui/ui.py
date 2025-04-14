#!/usr/bin/python
# ui/ui.py

# Terminal UI (Farben, Menü, Eingaben)

import shutil
import os
import colorama

colorama.init()

class UI:
    def __init__(self):
        self.banner = r'''
                                       ______
                    |\_______________ (_____\\______________
            HH======#H###############H#######################  
                    ' ~""""""""""""""`##(_))#H\"""""Y########    
                                      ))    \#H\       `"Y###
                                      "      }#H)
        '''
        self.colors = {
            "reset": colorama.Fore.RESET,
            "main": colorama.Fore.LIGHTCYAN_EX,
            "maindark": colorama.Fore.CYAN,
            "accent": colorama.Fore.MAGENTA,
            "success": colorama.Fore.LIGHTGREEN_EX,
            "error": colorama.Fore.LIGHTRED_EX,
            "warning": colorama.Fore.LIGHTYELLOW_EX
        }

        self.top_border = f"{self.colors['accent']}┌─────────────────────────────────────────────────────────────────────────────────────┐{self.colors['reset']}"
        self.bottom_border = f"{self.colors['accent']}└─────────────────────────────────────────────────────────────────────────────────────┘{self.colors['reset']}"

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_banner(self):
        self.clear()
        print(f"{self.colors['main']}{self.banner}{self.colors['reset']}")

    def print_centered(self, text, color="main"):
        terminal_width = shutil.get_terminal_size().columns
        print(f"{self.colors[color]}{text.center(terminal_width)}{self.colors['reset']}")

    def input_prompt(self, prompt):
        return input(f"{self.colors['accent']}[?] {prompt}{self.colors['reset']} > ")

    def menu_option(self, key, text):
        print(f" {self.colors['accent']}{key}{self.colors['reset']} > {self.colors['main']}{text}")

    def message(self, msg_type, text):
        print(f"{self.colors[msg_type]}[{msg_type[0].upper()}] {text}{self.colors['reset']}")

    def display_menu(self):
        self.print_banner()
        self.print_centered(self.top_border)
        self.menu_option("0", "Exit")
        self.menu_option("1", "Aufgabe 1")
        self.menu_option("2", "Aufgabe 2")
        self.menu_option("3", "Aufgabe 3")
        self.print_centered(self.bottom_border)

    def task_header(self):
        self.print_banner()
        self.print_centered(self.top_border)
