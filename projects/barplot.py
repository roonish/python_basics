import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

# Set up the style and palette
sns.set(style="whitegrid")
palette = sns.color_palette("husl", len(categories))

# Create the plot
plt.figure(figsize=(8, 5))
barplot = sns.barplot(x=categories, y=values, palette=palette)

# Add a title and labels
plt.title('Visually Appealing Bar Plot', fontsize=16, weight='bold')
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Values', fontsize=12)

# Enhance the visual aesthetics
for index, value in enumerate(values):
    barplot.text(index, value + 0.2, str(value), color='black', ha="center", fontsize=12)

plt.tight_layout()
plt.show()
