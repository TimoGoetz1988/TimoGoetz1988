# Datei-Organizer

Dieses Repository stellt einen flexiblen Datei-Organizer bereit, der eingehende Dateien automatisch sortiert. Über die YAML-Konfiguration kannst du Regeln für Datum, Projekte, Dateitypen und Spezialfälle definieren. Der Organizer überwacht den Eingangsordner kontinuierlich und protokolliert jede Aktion.

## 🚀 Quickstart
1. Kopiere die Beispiel-Umgebungsvariablen und passe sie an:
   ```bash
   cp .env.example .env
   ```
2. Starte Setup und Organizer:
   ```bash
   ./start.sh
   ```
3. Lege Dateien in `data/input/` ab und beobachte die einsortierten Ergebnisse unter `data/output/`.

## 📦 Struktur
```text
./
├─ README.md             → Projektüberblick & Anleitungen
├─ start.sh              → Setup (venv) & Demo-Run
├─ requirements.txt      → Python-Abhängigkeiten (watchdog, pyyaml)
├─ .env.example          → Beispiel-Variablen
├─ /data                 → input/, output/, samples/
├─ /notebooks            → Experimente & Analysen
├─ /src                  → Ausführbarer Code
├─ /docker               → Compose-Setup als Vorlage
└─ /docs                 → Zusatzdokus & Diagramme
```

## ⚙️ Umgebungsvariablen
| Variable         | Beschreibung                                                          | Standard            |
| ---------------- | --------------------------------------------------------------------- | ------------------- |
| `PROJECT_NAME`   | Anzeigename des Projekts                                               | `Datei-Organizer`   |
| `ENVIRONMENT`    | Umgebungskennung (z. B. `development`, `production`)                   | `development`       |
| `ORGANIZER_CONFIG` | Pfad zu einer alternativen YAML-Konfiguration (z. B. `configs/dev.yaml`) | `data/organizer.yaml` |

## 🧪 Skript-Details
- `start.sh` erstellt eine lokale Python-Umgebung (`.venv`), installiert Abhängigkeiten aus `requirements.txt` und führt `src/main.py` aus.
- `src/main.py` lädt Variablen aus `.env` (falls vorhanden), liest die Organizer-Konfiguration, verarbeitet vorhandene Dateien im Eingangsordner und startet anschließend die kontinuierliche Überwachung via `watchdog`.
- `data/organizer.yaml` enthält Beispielregeln für Datum, Projektschlagwörter, Dateitypen, Ignore-Patterns und Spezialordner.

## 🐳 Docker (Vorlage)
`docker/compose.yml` enthält einen minimalen Service, der denselben Code in einem Container ausführt. Passe die Datei nach Bedarf an (Ports, Binds, Abhängigkeiten).

## ✅ Nächste Schritte
- Erweitere `requirements.txt`, falls zusätzliche Libraries nötig sind.
- Ergänze Business-Logik in `src/main.py` oder lege weitere Module an.
- Ergänze Notebooks unter `notebooks/` für Analysen und Demos.

Viel Erfolg beim Starten deines neuen Projekts!
