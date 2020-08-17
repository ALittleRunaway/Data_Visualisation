"""Learning csv format"""
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # Объект чтения данных
    header_row = next(reader) # next - читает следующую строку, т.е. тут: первую

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # for i in range(len(header_row)):
    #     print(i, header_row[i])

    # Чтение дат, температурных минимумов и максимумов из файла
    dates, highs, lows = [], [], []
    for row in reader: # Тот же объект чтения данных ! НАЧИНАЕТСЯ СО ВТОРОЙ СТРОКИ, ИБО ПЕРВАЯ УЖЕ ПРОЧИТАНА !
        current_date = datetime.strptime(row[2], '%Y-%m-%d') # Преобразовывает строку в объект представляющий дату
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Нанесение данных на диаграмму
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(dates, highs, c='red', linewidth=1.5, alpha=0.5) # alpha - определяет степень прозрачности вывода
    ax.plot(dates, lows, c='blue', linewidth=1.5, alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Форматирование диаграммы
    plt.title('Daily high and low temperatures - 2018', font='monospace', fontsize=18)
    plt.xlabel('', font='monospace', fontsize=16)
    fig.autofmt_xdate() # Делает диагональку и, наверное, что-то с датой
    plt.ylabel('Temeperature (F)', font='monospace', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()

