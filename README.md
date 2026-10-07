# Books Web Scraping and Analysis

A beginner Python project that scrapes book information from [Books to Scrape](https://books.toscrape.com/) and performs simple data analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Jupyter Notebook
- Gmail SMTP

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
4. Converts price and rating into numeric values in the notebook.
5. Saves the final data to `books_data.csv`.
6. Performs simple analysis and visualizations.
7. Can run the scraper from `main.py`.
8. Sends an email when scraping finishes successfully.
9. Sends a failure email with the error message if scraping fails.

## How to Run the Notebook

Install the required libraries:

```bash
pip install -r requirements.txt
```

Open `books_web_scraping.ipynb` in Jupyter Notebook or Jupyter Lab and run the cells from top to bottom.

## How to Run the Email Notification Version

### 1. Set your email settings

On Windows Command Prompt:

```bash
set EMAIL_ADDRESS=yourgmail@gmail.com
set EMAIL_APP_PASSWORD=your_google_app_password
set EMAIL_TO=yourgmail@gmail.com
```

On PowerShell:

```powershell
$env:EMAIL_ADDRESS="yourgmail@gmail.com"
$env:EMAIL_APP_PASSWORD="your_google_app_password"
$env:EMAIL_TO="yourgmail@gmail.com"
```

Use a Google App Password, not your normal Gmail password.

### 2. Run the scraper

```bash
python main.py
```

If scraping succeeds, you will receive a success email with the number of books scraped.

If scraping fails, you will receive a failure email containing the error message.

## Files

- `books_web_scraping.ipynb` - scraping and data analysis notebook
- `scraper.py` - scrapes all book pages and saves the CSV
- `email_notifier.py` - sends email notifications
- `main.py` - runs scraping and handles success/failure
- `.env.example` - example email configuration
- `requirements.txt` - required Python libraries

## Website

https://books.toscrape.com/
