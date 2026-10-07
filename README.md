# Books Web Scraping and Analysis

A beginner Python project that scrapes book information from [Books to Scrape](https://books.toscrape.com/) and performs simple data analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Jupyter Notebook

## Data Collected

- Book Title
- Price
- Rating
- Availability
- Product URL

## What This Project Does

1. Scrapes all 50 pages of the website.
2. Collects information for around 1,000 books.
3. Stores the data in a Pandas DataFrame.
4. Converts price and rating into numeric values.
5. Saves the final data to `books_data.csv`.
6. Performs simple analysis and visualizations.

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Open `books_web_scraping.ipynb` in Jupyter Notebook or Jupyter Lab and run the cells from top to bottom.

## Website

https://books.toscrape.com/
