"""Einstiegspunkt für das neue Projekt."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable


ENV_FILE = Path(".env")


def load_env(path: Path = ENV_FILE) -> None:
    """Lädt einfache KEY=VALUE Paare aus einer .env-Datei, falls vorhanden."""
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def ensure_directories(folders: Iterable[Path]) -> None:
    """Erstellt benötigte Ordner, falls sie fehlen."""
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)


def build_status_message() -> str:
    project_name = os.environ.get("PROJECT_NAME", "Neues Projekt")
    environment = os.environ.get("ENVIRONMENT", "development")
    return f"Projekt '{project_name}' ist bereit (Umgebung: {environment})."


def main() -> None:
    load_env()
    data_root = Path("data")
    ensure_directories(
        [
            data_root / "input",
            data_root / "output",
            data_root / "samples",
        ]
    )

    print(build_status_message())
    print(f"Datenordner geprüft unter: {data_root.resolve()}")


if __name__ == "__main__":
    main()
