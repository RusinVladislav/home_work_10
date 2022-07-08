import json

SOURCE = "candidates.json"


def load_candidates():
    """Загружает данные из локального файла"""
    with open(SOURCE, mode='r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    return candidates_list

