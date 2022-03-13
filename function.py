import json
from pprint import pprint as pp

'''функция вывода списка кандидатов и их данные'''


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        candidates = json.load(f)
    return candidates



'''функция вывода данных кандидатов по 'id' '''


def get_data_candidate(uid):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate



'''функция для поиска по навыкам'''


def get_candidates_by_skills(skill):
    candidates = load_candidates()
    skill_candidate = []
    skill_lower = skill.lower()

    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(', ')
        if skill_lower in candidate_skills:
            skill_candidate.append(candidate)

    return skill_candidate

def get_datta_candidate(candidates):
    data_line = ''

    for candidate in candidates:
        data_line += candidate['name'] + '\n'
        data_line += candidate['position'] + '\n'
        data_line += candidate['skills'] + '\n'
        data_line += '\n'
    return '<pre>' + data_line + '<pre>'