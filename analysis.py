import matplotlib.pyplot as plt
import pandas as pd

# Create chart with 985x812 pixels
# plt.figure(figsize=(985/100, 812/100), dpi=100)

# Read data from csv file
data = pd.read_csv('985x812_394x180.csv')

# Stretch the x axis
data['t'] = data['t'] * 100

# Plot x position as a function of time
plt.plot(data['t'], data['x'])

# Add labels
plt.xlabel('t')
plt.ylabel('x')

# Show chart
plt.show()
