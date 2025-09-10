#Selenium is the library we will use to control our web browser(chrome)
#Beautifulsoup is our HTML parser

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


"""
Goal: scrape the Product Hunt website for the top 5 Products Launching today.

Uses: using Selenium we control our chrome browser, wait for the content to load, then we parse through the sites HTML using
BeautifulSoup to extract the top 5 products name,tagline and URL.

Return: a dictionary containg the name, tagline, and url of the top 5 products
If false: returns NONE if we fail to scrape

"""
def scrape_product_hunt():
    print("Starting the scraper...")

    '''
    runs chrome without the need of a visible browser, 
    disables the chrome sandbox due to issues with Unix(github actions)
    tells our webdriver to not use the shm storage due to being too small in some virtual env leading to crashes
    sets up our disguise to send a human like user agent to avoid being blocked

    '''
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


    driver = None

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    


