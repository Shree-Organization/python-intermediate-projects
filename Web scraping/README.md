
# 🕷 Advanced Web Scraper

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/) 
[![CSV](https://img.shields.io/badge/Output-CSV-orange.svg)](csv.gif)

A **robust and professional web scraping tool** built with Python to extract product data from paginated websites. It uses `requests` and `BeautifulSoup` with logging, retry logic, and CSV export capabilities.  

---

## ✨ Features

- 🌐 Fetch HTML pages with **custom browser headers**.
- 🛒 Extract product details:
  - Product **name**
  - Product **price**
  - Product **link**
- 🔄 *Retry **logic** for failed requests.
- 📄 Scrape **multiple pages** automatically.
- 💾 Save results to **CSV file**.
- 📊 **Logging** for progress and error tracking.
- 🛠 Easily customizable CSS selectors for any website structure.

---

## 🛠 Requirements

- `Python 3.x`  
- Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas` (optional for CSV formatting)

Install dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

---

## 🚀 Usage

1. Open `Web Scraper Code.py`.


2. Modify the BASE_URL to target the website you want to scrape.


3. Adjust pagination in *`scrape_all_pages(start, end)`*.


4. Run the script:


``
python 
Web Scraper Code.py
``
The script will log progress and save all scraped products to:

``
products.csv
``

---

## 📊 Example Output

| Name      | Price   | Link               |
| --------- | ------- | ------------------ |
| Product 1 | $99.99  | /products/product1 |
| Product 2 | $49.99  | /products/product2 |
| Product 3 | $149.99 | /products/product3 |


---

## 💡 Tips & Best Practices

✅ Always check the website's `robots.txt` before scraping.

✅ Use `time.sleep()` between requests to avoid overwhelming servers.

✅ Use headers to **mimic a real browser**.

⚡ For dynamic content (JS-loaded pages), consider **Selenium**.

🔧 Customize CSS selectors in `parse_products()` for each website.

🗂 For large datasets, you can save output to **JSON or a database**.



---

## 📜 Logging

- The script logs:

- URL fetch attempts

- Status codes and errors

- Number of products found per page

- CSV save confirmation





---

## 🌟 Bonus

- You can extend this project to:

- Scrape multiple websites simultaneously

- Schedule scraping tasks with cron or task scheduler

- Visualize product trends with Matplotlib or Seaborn

- Integrate with APIs or dashboards for real-time updates



---
