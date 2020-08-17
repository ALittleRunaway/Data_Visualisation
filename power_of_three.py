"""cubes"""
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]
x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(x_values, y_values, linewidth=3)
ax.scatter(x_values, y_values, s=10)

ax.set_title('Cubes', fontsize=24)
ax.set_xlabel('Numbers', fontsize=14)
ax.set_ylabel('Cubes of numbers', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=12)

ax.axis([0, 5100, 0, 130_100_100_000])
plt.show()