#Selenium is the library we will use to control our web browser(chrome)
#Beautifulsoup is our HTML parser

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pprint


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
    runs firefox without the need of a visible browser, 
    sets up our disguise to send a human like user agent to avoid being blocked

    '''

    # Sets the amount of times my script will try to run and how long it will wait in between
    max_retries = 3
    retry_delay = 5

    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} of {max_retries}...")

        options = Options()
        #runs without needing to physically open the browser
        options.add_argument("--headless")
        options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")


        driver = None

        try:

    # Launch our browser using our preset service and options
            driver = webdriver.Firefox(options=options)

    # Navigate to the web page
            print("Navigating to Product Hunt...")
            driver.get("https://www.producthunt.com/")

    # wait up to 10 seconds for the css of a DIV named datatast with a value of post item to become visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "section[data-test^='post-item']"))
            )
            print("Page content loaded.")

    # safety buffer in case any last minute page animations happen.
            time.sleep(5)

    # take a snapshot of the HTML on our driver page and pass it into our Beautiful soup which uses an HTML parser to parse. 
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")

    # search our soup item for all div items with the tag data test that both exist(x) and starts with the specified text
            all_products = soup.find_all("section", attrs = {"data-test": lambda x: x and x.startswith('post-item')})

            if not all_products:
                raise ValueError("Could not find any products. The website structure may have changed!")
        

        # create empty list as our for our final return
            products_data = []

            print(f"Found {len(all_products)} products. Extracting top 5...")
        
        #loop through our all_products list up to the 5th element
            for product_html in all_products[:5]:
            
        #set our variable to the value located by our find(must have <a> tag and be labeled data-test, it must also exist(x) and start with 'post-name')   
                name_element = product_html.find("a", attrs={"data-test": lambda x: x and x.startswith('post-name')})
            
        #based on the sites structure we ask BS to find the next part with the <a> tag which in our case we know is the tagline    
                tagline_element = name_element.find_next_sibling("a") if name_element else None

        #checks if name_element exist and set full name text to our raw data that we found under the above function    

                if name_element:
                
                    full_name_text = name_element.get_text(strip=True)

        #We know this site structures its product names as such (1.example) we do .split('. ', 1) meaning split at the first instance of '. '
        # we now have ['1.', 'example'] so doing -1 selects the name of the product and cleans it using strip the condition checks if '. ' exists in the text if not it just returns the full text
                    product_name = full_name_text.split('. ', 1)[-1].strip() if '. ' in full_name_text else full_name_text

        # takes the element in the href and appends it to the end of the link to give complete url        
                    product_url = "https://www.producthunt.com" + name_element['href']
                else:
                
                    product_name = "Name not found"
                    product_url = "URL not found"

            
                product_tagline = tagline_element.get_text(strip=True) if tagline_element else "Tagline not found"

        # packs all our data into a dictionary that is appended into our list products_data  
                products_data.append({
                    "name": product_name,
                    "tagline": product_tagline,
                    "url": product_url
                })

            print("--- Scraping successful on this attempt! ---")
            return products_data
        

    
        except Exception as e:
    # displays error and attempt number(zero index)
            print(f"An error occurred on attempt {attempt + 1}: {e}")
    # based on what attempt we are on we check if we have reached our third try (0,1,2) we set max_retries to 3 for readablitiy
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("--- Max retries reached. Scraping failed. ---")

        finally:
            if driver:
                print("closing the browser.")
                driver.quit()
    return []

#test
if __name__ == "__main__":
    top_products = scrape_product_hunt()
    if top_products:
        print("\n--- Scraping Successful! Top 5 Products ---")
        pprint.pprint(top_products)
        print("------------------------------------------")
    else:
        print("\n--- Scraping failed. No products found. ---")   