import json
from pathlib import Path

quis_json = Path(__file__).parent / "quis.json"

def as_json_string() -> str:
    """Loads the QuIS JSON file content and returns it as a JSON string."""

    with open(quis_json) as file:
        quis = file.read()
    return quis

def as_dict() -> dict:
    """Loads the QuIS JSON file content and returns it as a Python dictionary."""

    with open(quis_json) as file:
        quis = json.load(file)
    return quis


# if __name__ == "__main__":
