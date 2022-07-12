from flask import Flask
from utils import load_candidates, find_skill
from candidate import Candidate

app = Flask(__name__)

all_candidates = load_candidates()


@app.route("/")
def page_main():
    return f"<h2>Выбери необходимое действие:</h2>" \
           f"<h3><li><a href='/candidates/'>Список всех кандидатов</a>" \
           f"<li><a href='/candidate/0/'>Страница конкретного кандидата по номеру</a>" \
           f"<li><a href='/skills/0/'>Страница поиска кандидатов по навыку</a></h3>"


@app.route("/candidates/")
def page_candidates():
    result = '<h2>Список всех кандидатов:<h2>\n'
    for i in all_candidates:
        candidate = Candidate(i['pk'], i['name'], i['picture'], i['position'], i['gender'], i['age'], i['skills'])
        result += f'{candidate.get_all()}\n'
    return result


@app.route("/candidate/<int:uid>/")
def page_candidate(uid):
    if uid == 0:
        return '<h2>Введите выше номер необходимого кандидата</h2>'
    elif uid <= len(all_candidates):
        for i in all_candidates:
            if i['pk'] == uid:
                return f"<h2>Страница кандидата №{i['pk']}</h2>" \
                       f"<p><img src='{i['picture']}'>" \
                       f"<p>Имя кандидата: {i['name']}" \
                       f"<p>Позиция кандидата: {i['position']}" \
                       f"<p>Навыки: {i['skills']}" \
                       f"<p>Возраст: {i['age']}" \
                       f"<p>Пол: {i['gender']}"
    else:
        return f'<h2>Извините в нашей базе нет страницы кандидата с номером <font color="red">{uid}'


@app.route("/skills/<skill>/")
def page_skills(skill):
    if skill == '0':
        return "<h2>Введите искомый навык выше</h2>"
    elif find_skill(skill):
        list_skill = f'<h2>Список кандидатов с навыком {skill}:\n</h2>'
        for i in all_candidates:
            for value in i['skills'].split(', '):
                if skill.lower().strip() == value.lower():
                    list_skill += f"<p><li>Имя кандидата: <a href='/candidate/{i['pk']}/' _blank: target='_blank'>" \
                                  f"{i['name']}</a></p>" \
                                  f"<p>Позиция кандидата: {i['position']}</p>" \
                                  f"<p>Навыки: {i['skills']}\n</p>"
        return list_skill
    else:
        return f'<h2>Извините в нашей базе нет кандидатов с навыком <font color="red">{skill}'


app.run(debug=True)
