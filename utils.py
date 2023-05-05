import json


def load_candidates():
    """Загружает всех кандидатов"""

    with open('candidates.json', encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_all():
    """Возвращает всех кандидатов"""

    return load_candidates()


def get_by_skill(skill_name):
    """Возвращает кандидатов по skill"""

    candidates = load_candidates()
    skilled_candidates = []
    skill_lower = skill_name.lower()
    for candidate in candidates:
        if skill_lower in candidate["skills"].lower().split(", "):
            skilled_candidates.append(candidate)

    return skilled_candidates


def get_by_pk(pk):
    """Возвращает кандидатов по pk"""

    candidates = load_candidates()
    for candidate in candidates:
        if pk == candidate["pk"]:

            return candidate


def build_preformatted_list(candidates):
    """Собирает данные о кандидатах и возвращает в корректном формате"""

    page_content = ""
    for candidate in candidates:
        page_content += candidate["name"] + "\n"
        page_content += candidate["position"] + "\n"
        page_content += candidate["skills"] + "\n"
        page_content += "\n"

    return "<pre>" + page_content + "</pre>"
