def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)

average_grades = {}

for i, student in enumerate(sorted_students):
    average_grades[student] = calculate_average(grades[i])

print(average_grades)
