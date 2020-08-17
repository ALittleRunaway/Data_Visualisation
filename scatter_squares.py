"""dots"""
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Назначение заголовка диаграммы и меток осек
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', which='major', labelsize=12)
# plt.ticklabel_format(style='plain')

# Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('Pictures of graphics/Figure_9.png', bbox_inches='tight')