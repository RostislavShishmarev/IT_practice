with open('students.csv') as file:
    data = [row.split(',') for row in file.read().split('\n') if row]


def get_pupil(project_id):
    res = 'Ничего не найдено.'
    for row in data[1:]:
        if int(row[2]) == project_id:
            fam, name, father = row[1].split()
            part1 = f'Проект № {project_id} делал: {name[0]}. {fam}'
            part2 = f'он(а) получил(а) оценку - {row[4]}'
            res = f'{part1} {part2}'
            break
    return res


while True:
    input_ = input()
    if input_ == 'СТОП':
        break
    print(get_pupil(int(input_)))
