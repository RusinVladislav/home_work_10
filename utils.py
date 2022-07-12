import json

SOURCE = "candidates.json"


def load_candidates() -> list:
    """Загружает данные из локального файла в список"""

    with open(SOURCE, mode='r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    return candidates_list


def find_skill(skill):
    all_skills = []
    candidates = load_candidates()
    for i in candidates:
        all_skills.extend(i['skills'].split(', '))

    if skill.lower().strip() in all_skills:
        return True
    else:
        return False
