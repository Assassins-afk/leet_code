from datetime import datetime, timedelta
import random

# Список возможных сообщений о состоянии данных
random_save = ['Данные были изменены', 'данные остались без изменений']

# Случайный выбор состояния данных
random_save1 = random.choice(random_save)

# Вывод случайного сообщения о состоянии данных
print(random_save1)

# Получение текущего времени
now = datetime.now()
print('Время: ', now.hour, ':', now.minute, sep='')

# Преобразование текущего времени в строку формата %H:%M
current_time = now.strftime('%H:%M')

# Время сохранения данных (пример: 20:00)
save_time = '20:00'
# Определение номера дня недели
weekday = now.weekday()
print(weekday)
# Создание объекта datetime для времени сохранения
time1 = datetime.strptime(save_time, '%H:%M').replace(year=now.year, month=now.month, day=now.day)

# Если текущее время больше времени сохранения, добавляем сутки
if time1 < now:
    time1 += timedelta(days=1)

# Вычисление разницы во времени между временем сохранения и текущим моментом
a = time1 - now

# Основной цикл проверки условий
while True:
    # Проверяем, прошло ли более 20 часов с момента последнего изменения
    if a > timedelta(hours=20):
        # Если сегодняшний день - пятница
        if weekday == 4:
            # Если данные были изменены
            if random_save1 == 'Данные были изменены':
                print('Данные сохранины')
                break
            else:
                print('Изменений за неделю не было')
                break
        else:
            print('сегодня не пятница')
            break

    else:
        print('время еще не пришло')
        break
