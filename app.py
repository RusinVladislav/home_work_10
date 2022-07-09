from flask import Flask
from utils import load_candidates
from candidate import Candidate

app = Flask(__name__)

all_candidates = load_candidates()


@app.route("/")
def page_index():
    res = '<h2>Список всех кандидатов:<h2>\n'
    for i in all_candidates:
        candidate = Candidate(i['pk'], i['name'], i['picture'], i['position'], i['gender'], i['age'], i['skills'])
        res += f'{candidate.get_all()}\n'
    return res


@app.route("/candidates/<int:pk>/")
def page_candidates(pk):
    if pk <= len(all_candidates):
        for i in all_candidates:
            if i['pk'] == pk:
                return f"""<pre>Страница кандидата №{i['pk']}\n
                            <img src="{i['picture']}">
                            Имя кандидата: {i['name']}\n
                            Позиция кандидата: {i['position']}\n
                            Навыки: {i['skills']}\n
                            Возраст: {i['age']}\n
                            Пол: {i['gender']}\n</pre>"""
    else:
        return f'Извините в нашей базе нет страницы кандидата с номером {pk}'


@app.route("/skills/<skill>")
def page_skills(skill):
    list_skill = f'<h2>Список кандидатов с навыком {skill}:\n</h2>'
    for i in all_candidates:
        for value in i['skills'].split(', '):
            if skill.lower().strip() == value.lower():
                list_skill += f"<pre><h3><li>Имя кандидата: <a href='/candidates/{i['pk']}' _blank: target='_blank'>{i['name']}</a>\nПозиция кандидата: {i['position']}\nНавыки: {i['skills']}\n<h3></pre>"
    return list_skill


app.run(host='127.0.0.2', port=80)
