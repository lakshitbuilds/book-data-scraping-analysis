from datetime import datetime
from scraper import scrape_books
from email_notifier import send_email


try:
    total_books = scrape_books()

    message = (
        "Web scraping completed successfully.\n\n"
        "Website: Books to Scrape\n"
        f"Records scraped: {total_books}\n"
        "File: books_data.csv\n"
        f"Completed at: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
    )

    send_email("Web Scraping Completed", message)
    print("Scraping completed successfully.")
    print(f"Total books scraped: {total_books}")

except Exception as error:
    print("Scraping failed:", error)

    try:
        message = (
            "The web scraping process failed.\n\n"
            "Website: Books to Scrape\n"
            f"Error: {error}\n"
            f"Failed at: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
        )

        send_email("Web Scraping Failed", message)

    except Exception as email_error:
        print("Failure email could not be sent:", email_error)
