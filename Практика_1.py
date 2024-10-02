def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

student_grades = {'Johnny':[5, 5, 5, 4, 5],
                  'Bilbo': [4, 4, 3],
                  'Steve':[4, 5, 5, 2],
                  'Khendrik':[2, 2, 2, 3],
                  'Aaron':[5, 3, 3, 5, 4]
                  }
average_grades = {student: calculate_average(grades)
                  for student, grades in student_grades.items()}
print(average_grades)

# .for разбивает каждый кортеж (ключ, значение)
# in используется для проверки, содержится ли элемент в итерируемом объекте
#return — это ключевое слово, используемое внутри функции для завершения
#её выполнения и возвращения значения в место, где функция была вызвана
# .items() возвращает (пары ключ-значение)
# average для вычисления среднего значения оценок в списке