# scrapper
# Web Crawler and Database System

This Python script is designed to scrape data from a store website and persist it in an SQLite database. The system includes a web crawler using the `requests` library for web scraping, `BeautifulSoup` for HTML parsing, and `sqlite3` for database interaction.

## Prerequisites

- **Python**: Ensure that Python is installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).

- **Required Libraries**: Install the necessary Python libraries by running the following command in your terminal or command prompt:

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

### 1. Clone the Repository

Clone this repository or download the Python script (`scrapper.py`) from the provided example.

### 2. Modify URL and HTML Structure

Open the script in a text editor and replace the placeholder URL with the actual URL of the store website. Additionally, adjust the HTML parsing based on the structure of the website.

### 3. Run the Script

Execute the script in your terminal or command prompt:

```bash
python scrape.py
