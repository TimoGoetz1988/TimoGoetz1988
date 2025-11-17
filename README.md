# Neues Projekt-Repository

Dieses Repository stellt ein schlankes Projekt-Template bereit, damit du schnell mit frischen Ideen starten kannst – ohne den alten Node.js-Stand. Die Struktur folgt deinen bevorzugten Standards und bietet sofort nutzbare Skripte für Setup und Ausführung.

## 🚀 Quickstart
1. Kopiere die Beispiel-Umgebungsvariablen und passe sie an:
   ```bash
   cp .env.example .env
   ```
2. Starte Setup und Demo-Ausführung:
   ```bash
   ./start.sh
   ```
3. Passe den Code unter `src/` an dein Vorhaben an.

## 📦 Struktur
```text
./
├─ README.md             → Projektüberblick & Anleitungen
├─ start.sh              → Setup (venv) & Demo-Run
├─ requirements.txt      → Python-Abhängigkeiten (aktuell leer)
├─ .env.example          → Beispiel-Variablen
├─ /data                 → input/, output/, samples/
├─ /notebooks            → Experimente & Analysen
├─ /src                  → Ausführbarer Code
├─ /docker               → Compose-Setup als Vorlage
└─ /docs                 → Zusatzdokus & Diagramme
```

## ⚙️ Umgebungsvariablen
| Variable      | Beschreibung                                         | Standard        |
| ------------- | ---------------------------------------------------- | --------------- |
| `PROJECT_NAME`| Anzeigename deines Projekts                          | `Neues Projekt` |
| `ENVIRONMENT` | Umgebungskennung (z. B. `development`, `production`) | `development`   |

## 🧪 Skript-Details
- `start.sh` erstellt eine lokale Python-Umgebung (`.venv`), installiert Abhängigkeiten aus `requirements.txt` (falls vorhanden) und führt `src/main.py` aus.
- `src/main.py` lädt Variablen aus `.env` (falls vorhanden), sorgt für die Standard-Ordner unter `data/` und gibt den aktuellen Projektstatus aus.

## 🐳 Docker (Vorlage)
`docker/compose.yml` enthält einen minimalen Service, der denselben Code in einem Container ausführt. Passe die Datei nach Bedarf an (Ports, Binds, Abhängigkeiten).

## ✅ Nächste Schritte
- Erweitere `requirements.txt`, falls zusätzliche Libraries nötig sind.
- Ergänze Business-Logik in `src/main.py` oder lege weitere Module an.
- Ergänze Notebooks unter `notebooks/` für Analysen und Demos.

Viel Erfolg beim Starten deines neuen Projekts!
