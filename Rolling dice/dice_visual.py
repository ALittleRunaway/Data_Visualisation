"""Visual of two cubics"""
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Создание кубиков D6 и D10
die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
x_values = list(range(2, max_result+1)) # You need list
data = [Bar(x=x_values, y=frequencies)] # Brackets

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling D6 and D10 dice 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
