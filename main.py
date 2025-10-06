import os
from dotenv import load_dotenv
from scraper import scrape_product_hunt
from content_generator import gen_post_content 
from linkedin_poster import post_to_linkedin


load_dotenv()

def main():
    print("--- Starting the Automated Content Pipeline ---")

    # 1. Scrape the data
    scraped_products = scrape_product_hunt()
    if not scraped_products:
        print("Pipeline stopped: Scraping failed or no products found.")
        return 

    # 2. Generate the content
    post_content = gen_post_content(scraped_products)
    if not post_content:
        print("Pipeline stopped: Content generation failed.")
        return

    # 3. Post the content as a DRAFT to LinkedIn (No human review)
    print("Content generated. Proceeding to create draft on LinkedIn...")
    success = post_to_linkedin(post_content)

    if success:
        print("\n--- Pipeline completed successfully! Draft is ready for review on LinkedIn. ---")
    else:
        print("\n--- Pipeline finished with an error during the posting step. ---")

if __name__ == "__main__":
    main()