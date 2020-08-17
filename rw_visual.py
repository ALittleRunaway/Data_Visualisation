"""Visual"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# новые блуждания строятся до тех пор, пока пролграмма остается ктивной
while True:
    # Построение случайного блуждания
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(6, 3), dpi=166)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=3, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    # ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_title('Random Walking', fontsize=20, font='monospace')
    ax.tick_params(axis='both', which='major', labelsize=9)

    # Выделение первой и последней точек
    # ax.scatter(0, 0, c='cyan', edgecolors='none', s=80)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='cyan', edgecolors='none', s=80)
    ax.scatter(0, 0, c='cyan', s=25)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='cyan', s=25)

    # Удалени осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
