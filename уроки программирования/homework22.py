team1_num = int(input('Количество участников команды 1:'))
team2_num = int(input('Количество участников команды 2:'))
print('"В команде %s участников %d!"' % ('Мастер кода', team1_num))
print('"Итого сегодня в командах участников: %d и %d!"' % (team1_num, team2_num))

score_2 = 42
print('"Команда {} решила задач: {}"!'.format('Волшебники данных', score_2))
team2_time = 18015.2
print('"{} решили задачи за {} c!"'.format('Волшебники данных', team2_time))

score_1 = 40
print(f'"Команды решили {score_1} и {score_2} задач."')

tasks_total = score_1 + score_2
time_avg = 350.4
team1_time = (tasks_total * time_avg) - team2_time
print(team1_time)

challenge_result = ''
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"')
print(challenge_result)