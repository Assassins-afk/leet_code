#Используем datetime для определения времени работы сотрудников
from datetime import datetime
#Поучаем текущее время
now = datetime.now()
current_time = now.strftime('%H:%M')
#Определяем начало и конец рабочего дня
start_time = '8:00'
end_time = '20:00'
print('Вермя:',now.hour, ':', now.minute, sep='')
#Определяем рабочие дни недели
current_day = now.weekday()
#Пишем должность пользователя
user = input('Введите свою должность:')
if user == 'Руководитель':
    print('Вам открыт путь всегда')
elif user == 'Сотрудник':
    # Преобразуем строки времени в объекты datetime для сравнения
    current_time_obj = datetime.strptime(current_time, '%H:%M')
    start_time_obj = datetime.strptime(start_time, '%H:%M')
    end_time_obj = datetime.strptime(end_time, '%H:%M')
    # Проверяем, находится ли текущее время в рабочем диапазоне
    if start_time_obj <= current_time_obj <= end_time_obj:
        print('Вам разрешен вход с 8:00 до 20:00 в рабочие дни')
    else:
        print('Рабочий день закончен')
# Проверка рабочего дня
    if 0 <= current_day <= 5:
            print('Сегодня не рабочий день приходите в понедельник')
    else:
        print('сегодня рабочий день, можете проходить')
else:
    print('Должность не определена')