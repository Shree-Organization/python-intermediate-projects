

# 📊 Basic Data Visualization in Python

A Python script to **analyze and visualize data** using `pandas`, `seaborn`, and `matplotlib`.  
It demonstrates multiple types of visualizations including line plots, bar charts, scatter plots, heatmaps, and pie charts.

---

## 🚀 Features

- ✅ Load and manipulate data with **pandas**  
- ✅ Visualize trends with **line plots** 
- ✅ Compare categories with **bar charts**  
- ✅ Explore relationships with **scatter plots**  
- ✅ Analyze correlations with **heatmaps**  
- ✅ Display proportions with **pie charts**  
- ✅ Save plots as images for reports or presentations  

---

## 📦 Requirements

- `Python 3.x ` 
- `pandas`
- `matplotlib`
- `seaborn`

Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

---

## ⚙ Setup & Usage

1. Load Data



- Replace the sample dataset with your CSV file if needed:

```python
# df = pd.read_csv("your_data.csv")
```
2. Run the Script


```
python data_visualization.py
```
3. Outputs



- The script generates and saves plots as *`.png`* files:

    - *`line_plot.png`* → Monthly trends of Sales, Profit, and Expenses

    - *`bar_plot.png`* → Sales by Month

    - *`scatter_plot.png`* → Sales vs Profit

    - *`heatmap.png`* → Correlation Matrix

    - *`pie_chart.png`* → Sales distribution




---

## 🔧 Visualizations Explained

| Visualization | Purpose                                                 |
| ------------- | ------------------------------------------------------- |
| Line Plot     | Shows trends of Sales, Profit, and Expenses over months |
| Bar Chart     | Compares Sales across months                            |
| Scatter Plot  | Highlights relationship between Sales and Profit        |
| Heatmap       | Displays correlation between numerical variables        |
| Pie Chart     | Shows percentage contribution of each month’s sales     |




---

## 📈 Example Insights

- Which month had the **highest sales**

- How **profit relates to sales**

- **Trends** in expenses over time

- **Distribution** of sales across months

- **Correlation** between metrics to identify patterns



---

## 💡 Extending the Script

- Replace sample data with **real datasets**

- Add **new columns** to visualize additional metrics

- Customize **Seaborn/Matplotlib styles** for better aesthetics

- Integrate into **Jupyter Notebooks** for interactive analysis



---

## 📌 Notes

- Ensure `Month` column is **categorical** or properly sorted for meaningful plots.

- Adjust figure size, palette, or plot type based on dataset and requirements.



---
