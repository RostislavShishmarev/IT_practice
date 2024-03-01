import csv

P, M = 67, 10 ** 9 + 9


def generate_hash(row):
    hash_ = 0
    name = ''.join(row[1].split())
    for i, char in enumerate(name):
        add = ord(char) * P ** i
        hash_ += add

    return hash_ % M


with open('students.csv') as file:
    data = [row.split(',')
            for row in file.read().split('\n')
            if row]

for i, row in enumerate(data[1:]):
    data[i + 1][0] = generate_hash(row)

with open('students_with_hash.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data)
