import json
import os

def load_curriculum():
    """Load curriculum.json from /data folder."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "data", "curriculum.json")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
