# Задаем исходные данные
score_1 = 85  # Очки команды Мастера кода
score_2 = 85  # Очки команды Волшебники Данных
team1_time = 120  # Время команды Мастера кода в минутах
team2_time = 115  # Время команды Волшебники Данных в минутах


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

tasks_total = 10  # Общее количество задач
time_avg = (team1_time + team2_time) / 2  # Среднее время выполнения задач

# Вывод результата
print(f"Результат соревнования: {result}")
print(f"Всего задач: {tasks_total}")
print(f"Среднее время выполнения задач: {time_avg} минут")


# Количество участников первой команды
team1 = "Мастера кода"
team1_num = 5
result = "В команде %s участников: %d !" % (team1, team1_num)
print(result)

# Количество участников в обеих командах
team1_num = 5
team2_num = 6
result = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(result)

# Количество задач решённых командой 2 (score_2)
score_2 = 42
result = "Команда Волшебники данных решила задач: {} !" .format(score_2)
print(result)

# Время за которое команда 2 решила задачи (team1_time)
team1_time = 18015.2
result = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(result)

# Количество решённых задач по командам: score_1, score_2
score_1 = 40
score_2 = 42
result = f'Команды решили {score_1} и {score_2} задач.'
print(result)

# Исход соревнования (challenge_result)
challenge_result = 'победа команды Мастера кода!'
result = f'Результат битвы: {challenge_result}'
print(result)

# количество задач (tasks_total) и среднее время решения (time_avg)
tasks_total = 82
time_avg = 350.4
result = f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."'
print(result)
