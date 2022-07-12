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
        return f"№{self.pk}. {self.name} " \
               f"Позиция: {self.position} " \
               f"Навыки: {self.skills}. " \
               f"Пол: {self.gender} " \
               f"Возраст: {self.age}."

    def get_all(self):
        """Показывает короткое представление всех кандидатов"""
        return f"<pre>Имя кандидата: <a href='/candidate/{self.pk}/' _blank: target='_blank'>" \
               f"{self.name}</a>\nПозиция кандидата: {self.position}\nНавыки: {self.skills}</pre>"
