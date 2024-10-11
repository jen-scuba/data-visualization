import matplotlib.pyplot as plt

# x_values = range(1,6)
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.

# ax.axis([0, 6, 0, 130])
ax.axis([0, 1000, 0, 999_999_999])
ax.ticklabel_format(style='plain')

plt.show()
# plt.savefig('squares_cube_5k.jpg', bbox_inches='tight')
