import re
import requests
from bs4 import BeautifulSoup
import sqlite3

# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Function to create a SQLite database and table
def create_database():
    conn = sqlite3.connect('store_data.db')
    cursor = conn.cursor()

    # Create a table to store item information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            image TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to scrape data from the website and save it to the database
def scrape_and_save_data():
    url = 'https://jiji.ng/'  # Replace with the actual URL of the store website
    response = requests.get(url)
    # driver = webdriver.Chrome()
    # response = driver.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find("body").find("script")
        for items in re.findall(r"(\[.*\])", items.string):
            print("trials>>>>>>>>>>>>", items)


        conn = sqlite3.connect('store_data.db')
        cursor = conn.cursor()

        for item in items:
            name = item.get('name')
            price = float(item.get('price'))
            image = item.get('image')

            # Insert data into the database
            cursor.execute('''
                INSERT INTO items (name, price, description)
                VALUES (?, ?, ?)
            ''', (name, price, image))

        conn.commit()
        conn.close()
        print('Data successfully scraped and saved to the database.')

    else:
        print('Failed to retrieve data from the website.')

# Function to query data from the database
def query_data():
    conn = sqlite3.connect('store_data.db')
    cursor = conn.cursor()

    # Example query: retrieve all items with prices less than $50
    cursor.execute('SELECT * FROM items WHERE price < 50')
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Price: ${row[2]}, Description: {row[3]}")

    conn.close()

if __name__ == '__main__':
    create_database()
    scrape_and_save_data()
    query_data()
