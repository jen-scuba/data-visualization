import matplotlib.pyplot as plt

# x_values = range(1,6)
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
# ax.ticklabel_format(style='plain')
# ax.axis([0, 6, 0, 130])
ax.axis([0, 810, 0, 50_500_000])

plt.show()
# plt.savefig('squares_cube_5k.jpg', bbox_inches='tight')
