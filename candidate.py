from utils import load_candidates


class Candidate:
    def __init__(self, pk, name, picture, position, gender, age, skills):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

    def __repr__(self):
        return f'№{self.pk}. {self.name}, навыки: {self.skills}'

    def get_all(self):
        """Показывает короткое представление всех кандидатов"""
        return f"<pre>Имя кандидата: <a href='candidates/{self.pk}' _blank: target='_blank'>{self.name}</a>\nПозиция кандидата: {self.position}\nНавыки: {self.skills}</pre>"

    # def get_by_pk(self, pk):
    #     """Показывает кандидата по его номеру pk"""
    #
    #     all_candidates = len(load_candidates())
    #     if pk <= all_candidates:
    #         for i in load_candidates():
    #             if i['pk'] == pk:
    #                 a = list(i.values())
    #                 return a
    #     else:
    #         print(f'Извините в нашей базе нет кандидата с номером {pk}')
    #
    # def get_by_skill(skill_name):
    #     """Показывает кандидатов по запрашиваемому навыку"""
    #
    #     candidates = []
    #     for i in load_candidates():
    #         skills = i['skills'].split(', ')
    #         for skill in skills:
    #             if skill.lower() == skill_name.lower().strip():
    #                 candidates.append(i['name'])
    #     if candidates:
    #         print(*candidates, sep='\n')
    #     else:
    #         print(f'Извините в нашей базе нет кандидата с навыком: {skill_name}')
