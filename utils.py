import json


def load_candidates_from_json(path):
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
        return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'picture': candidate['picture'],
                'position': candidate['position'],
                'skills': candidate['skills'],
            }
    return {'not_found': 'Ушел на обед'}


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates = []
    for candidate in __data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates
