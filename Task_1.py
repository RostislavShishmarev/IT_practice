import csv

with open('students.csv') as file:
    data = [row.split(',') for row in file.read().split('\n') if row]

sum_ = 0
n = 0
missed = []
for i, row in enumerate(data[1:]):
    id_, name, project_id, class_, score = row
    if score != 'None':
        sum_ += int(score)
        n += 1
        if name.startswith('Хадаров Владимир'):
            print(f'Ты получил: {score}, за проект - {project_id}')
    else:
        missed.append(i + 1)  # Get array of None positions indexes
        # + 1 because of string 9

av = round(sum_ / n, 3)
for i in missed:
    data[i][4] = str(av)  # Set average mark on None positions

with open('student_new.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data)
