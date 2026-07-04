def clean_text(text: str):
    """
    Basic text cleaning
    """
    return text.strip().replace("\n", " ").lower()


def extract_skills(text: str, skill_list):
    """
    Match skills from text
    """
    text = text.lower()

    matched = []

    for skill in skill_list:
        if skill.lower() in text:
            matched.append(skill)

    return matched


def calculate_score(matched, total):
    if total == 0:
        return 0
    return int((len(matched) / total) * 100)