from flask import Flask

from function import load_candidates, get_data_candidate, get_candidates_by_skills, get_datta_candidate
app = Flask(__name__)

@app.route('/')
def page_index():
    candidates = load_candidates()
    empty_line = get_datta_candidate(candidates)
    return empty_line


@app.route('/skill/<name>')
def page_skill(name):
    candidates = get_candidates_by_skills(name)
    skills_condidate = get_datta_candidate(candidates)
    return skills_condidate
@app.route('/candidate/<int:uid>')
def data_candidate(uid):
    candidate = get_data_candidate(uid)
    id_condidate = f'''
    <pre>
{candidate['name']}
{candidate['position']}
{candidate['skills']}
    </pre>
    '''
    return id_condidate
app.run()