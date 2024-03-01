def sort(list_, column_index=0):
    def f(element):  # function to get sort parameter
        return int(element[column_index])

    new = [[-1] * (column_index + 1)]
    for el in list_:
        i = 0
        while i < len(new) and f(el) > f(new[i]):
            i += 1
        new.insert(i, el)
    return new[1:]


with open('students.csv') as file:
    data = [
        row.split(',')
        for row in file.read().split('\n')
        if row and row.split(
            ',',
        )[4].isdigit() and row.split(
            ',',
        )[3].startswith('10')
    ]

sorted_data = sort(data, 4)

for i, row in enumerate(sorted_data[::-1][:3]):
    fam, name, father = row[1].split()
    print(f"{i + 1} место: {name[0]}. {fam}")
