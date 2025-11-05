import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Optional: set Seaborn theme
sns.set_theme(style="whitegrid")

# Load data (replace with your file path or use the sample below)
# df = pd.read_csv("your_data.csv")

# Sample dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 120, 90, 140, 160],
    'Profit': [20, 25, 18, 30, 35],
    'Expenses': [80, 90, 70, 110, 125]
}

df = pd.DataFrame(data)

# Summary stats
print("Summary Statistics:\n", df.describe())

# Line Plot with multiple metrics
plt.figure(figsize=(10, 6))
sns.lineplot(data=df.set_index("Month"), markers=True, dashes=False)
plt.title("Monthly Sales, Profit, and Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("line_plot.png")
plt.show()

# Bar Plot - Sales by Month
plt.figure(figsize=(8, 5))
sns.barplot(x="Month", y="Sales", data=df, palette="Blues_d")
plt.title("Sales by Month")
plt.tight_layout()
plt.savefig("bar_plot.png")
plt.show()

# Scatter Plot - Sales vs Profit
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Sales", y="Profit", data=df, hue="Month", s=100, palette="viridis")
plt.title("Sales vs Profit")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# Heatmap - Correlation Matrix
plt.figure(figsize=(6, 4))
corr = df.drop(columns='Month').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()

# Pie Chart - Sales Distribution (using matplotlib)
plt.figure(figsize=(6, 6))
colors = sns.color_palette('pastel')
plt.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%', colors=colors, startangle=90)
plt.title("Sales Distribution by Month")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

