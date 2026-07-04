from pathlib import Path
import json


def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_folder(folder_path):
    """
    Load all .txt files from folder
    """
    folder = Path(folder_path)

    data = []

    for file in folder.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            data.append({
                "filename": file.name,
                "text": f.read()
            })

    return data


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)