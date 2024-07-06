# Programmer: Samir Ranabhat
# Date: July 03, 2024

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary with the data
data = {
    'City': ['Bristol', 'Cardiff', 'Bath', 'Liverpool', 'Glasgow', 'Edinburgh', 'Leeds', 'Reading', 'Swansea', 'Manchester'],
    'Population': [617280, 447287, 94782, 864122, 591620, 464990, 455123, 318014, 300352, 395515]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Set up the figure and axes for subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))  # 1 row, 2 columns for the plots

# Scatter Plot
ax1.scatter(df['City'], df['Population'], color='blue')  # Create scatter plot
ax1.set_title('City vs Population - Scatter Plot')  # Set the title of the plot
ax1.set_xlabel('City')  # Set the label for the x-axis
ax1.set_ylabel('Population')  # Set the label for the y-axis
ax1.tick_params(axis='x', rotation=45)  # Rotate the x-axis labels by 45 degrees
ax1.grid(True)  # Enable grid lines

# Bar Chart
ax2.bar(df['City'], df['Population'], color='green')  # Create bar chart
ax2.set_title('City vs Population - Bar Chart')  # Set the title of the plot
ax2.set_xlabel('City')  # Set the label for the x-axis
ax2.set_ylabel('Population')  # Set the label for the y-axis
ax2.tick_params(axis='x', rotation=45)  # Rotate the x-axis labels by 45 degrees

# Adjust layout and save the figure
plt.tight_layout()
plt.show()  # Display the plot