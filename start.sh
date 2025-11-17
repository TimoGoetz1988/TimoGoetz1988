#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_ROOT"

# 1) Virtualenv
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

# 2) Optional: pip aktualisieren, Fehlversuche werden nur geloggt
python -m pip install --upgrade pip >/dev/null 2>&1 || echo "Hinweis: pip konnte nicht aktualisiert werden (vermutlich offline)."

# 3) Dependencies (nur wenn Datei Inhalte hat)
if [ -s requirements.txt ]; then
  pip install -r requirements.txt
fi

# 4) Run demo application
python src/main.py
