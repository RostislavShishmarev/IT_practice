import csv
import random
import string



def generate_login(row):
    fam, name, father = row[1].split()
    return f'{fam}_{name[0]}{father[0]}'


def generate_password(already_used):  # already_used - already used passwords
    password = ''
    while not password or password in already_used:
        password_list = []
        password_list += random.choices(string.ascii_lowercase, k=4)
        password_list += random.choices(string.ascii_uppercase, k=2)
        password_list += random.choices(string.digits, k=2)
        random.shuffle(password_list)
        password = ''.join(password_list)
    return password


with open('students.csv') as file:
    data = [row.split(',')
            for row in file.read().split('\n')
            if row]

passwords = []
data[0] += ['login', 'password']
for i, row in enumerate(data[1:]):
    login, password = generate_login(row), generate_password(passwords)
    data[i + 1] += [login, password]

with open('student_password.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data)
