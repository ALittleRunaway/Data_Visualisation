"""Temperatures for Death valley"""
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:  # Тот же объект чтения данных ! НАЧИНАЕТСЯ СО ВТОРОЙ СТРОКИ, ИБО ПЕРВАЯ УЖЕ ПРОЧИТАНА !
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # Преобразовывает строку в объект представляющий дату
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Нанесение данных на диаграмму
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(dates, highs, c='red', linewidth=1.5, alpha=0.5)  # alpha - определяет степень прозрачности вывода
    ax.plot(dates, lows, c='blue', linewidth=1.5, alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Форматирование диаграммы
    title = 'Daily high and low temperatures - 2018\nDeath Valley, CA'
    plt.title(title, font='monospace', fontsize=17)
    plt.xlabel('', font='monospace', fontsize=15)
    fig.autofmt_xdate()  # Делает диагональку и, наверное, что-то с датой
    plt.ylabel('Temeperature (F)', font='monospace', fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()


