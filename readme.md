
# 🔢 Simple UI mit Sortier-Tool für Zahlen aus Datei

Ein einfaches Python-Konsolenprogramm, das zufällige Zahlen generiert, sortiert, analysiert und als Textdatei speichert – mit einer farbigen Terminal-Benutzeroberfläche.

---
## 🧩 Projektstruktur

```plaintext
projekt/
│
├── main.py                  # Einstiegspunkt (Menü & Steuerung)
│
├── ui/
│   ├── __init__.py          # Paket-Init für UI
│   └── ui.py                # Terminal UI (Farben, Menü, Eingaben)
│
├── core/
│   ├── __init__.py          # Paket-Init für Aufgaben
│   └── tasks.py             # Aufgabenlogik (z. B. sortieren, analysieren)
│
└── process/
    ├── __init__.py          # Paket-Init für Datenverarbeitung
    └── process.py           # Helferfunktionen (Dateien, Berechnungen)
```

---


## 🚀 Ausführen

```bash
  python main.py
```

> Erfordert **Python 3.10+** wegen `match-case`.

---

## 📚 Aufgaben

- **Aufgabe 1**:
  - Erstellt `output.txt` mit 10 zufälligen Zahlen.
  - Liest die Zahlen, sortiert sie, berechnet Durchschnitt & Maximum.
  - Speichert alles in `processed_output.txt`.

- **Aufgabe 2 / 3**:
  - Noch nicht implementiert (Platzhalter vorhanden).

---

## 🎨 Benutzeroberfläche

- Konsolenbasierte UI mit ASCII-Art & Farben (`colorama`)
- Menüführung und Feedback (Success, Error, Warning etc.)

---

## 🧰 Abhängigkeiten

Installiere benötigte Pakete mit:

```bash
  pip install -r requirements.txt
```

**requirements.txt**
```
colorama
```

Alternativ manuell:

```bash
  pip install colorama
```

---

## 🧼 Sauber Beenden

Das Programm kann jederzeit mit `Strg + C` beendet werden. Dabei wird der Abbruch elegant abgefangen.

---

## 📦 Virtuelles Environment (venv)

Um sicherzustellen, dass alle Abhängigkeiten in einer isolierten Umgebung installiert werden, empfehle ich, ein virtuelles Environment zu verwenden:

1. Erstelle ein virtuelles Environment:

```bash
  python -m venv venv
```

2. Aktiviere das virtuelle Environment:

- Auf **Windows**:

```bash
  venv\Scripts\activate
```

- Auf **Linux/macOS**:

```bash
  source venv/bin/activate
```

3. Installiere alle Abhängigkeiten:

```bash
  pip install -r requirements.txt
```

4. Deaktiviere das virtuelle Environment nach Gebrauch:

```bash
  deactivate
```

---

## 👨‍💻 Autor

xqi 
Stand: 10.04.2025

---

## 📝 Lizenz

MIT – Frei nutzbar, änderbar und erweiterbar

