students = [
    {'name': 'Rezso', 'age': 9.5, 'candies': 2},
    {'name': 'Gerzson', 'age': 10, 'candies': 1},
    {'name': 'Aurel', 'age': 7, 'candies': 3},
    {'name': 'Zsombor', 'age': 12, 'candies': 5},
    {'name': 'Olaf', 'age': 12, 'candies': 7},
    {'name': 'Teodor', 'age': 3, 'candies': 2},
    {'name': 'Zsombor', 'age': 12, 'candies': 5}
]


def get_candies(students):
    candies = 0
    for student in students:
        candies += student['candies']
    return candies

def get_names(students):
    names = []
    for student in students:
        names.append(student['name'])
    return names


def filter_age(students, age):
    filtered_students = []
    for student in students:
        if student['age'] >= age:
            filtered_students.append(student)
    return filtered_students


def get_name(student):
    return student['name']

def is_old(student):
    return student['age'] >= 5

print(list(filter(is_old, students)))
print((map(get_name, students)))



