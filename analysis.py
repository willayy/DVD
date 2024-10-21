import matplotlib.pyplot as plt
import pandas as pd

# Create chart with 985x812 pixels
plt.figure(figsize=(985/100, 812/100), dpi=100)

# Read data from csv file
data = pd.read_csv('985x812_394x180.csv')

# Get all points that have speed 0
data = data[data['dx'] == 0]



