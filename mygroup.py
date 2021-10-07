groupmates = [
    {
        "name": "Николай",
        "surname": "Аношин",
        "exams": ["Высшмат","web","ИН"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Александр",
        "surname": "Барышев",
        "exams": ["ЭИЭС", "АиГ", "wEB"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Алексей",
        "surname": "Викулин",
        "exams": ["Философия", "Рус", "ИКГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алексей",
        "surname": "Гаврилов",
        "exams": ["WEB", "ЭИЭ", "ИКГ"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Ринат",
        "surname": "Галиев",
        "exams": ["АиГ", "История", "ИНО"],
        "marks": [3, 5, 4]
    },
      {
        "name": "Илья",
        "surname": "Дегтярев",
        "exams": ["WEB", "ЭИЭ", "ИКГ"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Денис",
        "surname": "Долганов",
        "exams": ["АиГ", "История", "ИНО"],
        "marks": [5, 5, 4]
    }
]

def filter_students(students, m_ball):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(20), u"Средний балл".ljust(15))
    for student in students:
        sum = 0
        for mark in student["marks"]:
            sum += mark
        average = sum / len(student["marks"])
        if (round(average, 2) > m_ball):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35), str(student["marks"]).ljust(20), str(round(average, 2)).ljust(15))

mid = float(input("средний балл: "))

filter_students(groupmates, mid)
