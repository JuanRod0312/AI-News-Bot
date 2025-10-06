import os
from dotenv import load_dotenv
from scraper import scrape_product_hunt
from content_generator import gen_post_content
from linkedin_poster import post_to_linkedin


def main():
    print("--- Starting the Automated Content Pipeline ---")

    scraped_products = scrape_product_hunt()
    if not scraped_products:
        print("Pipeline stopped: Scraping failed or no products found.")
        return
    
    post_content = gen_post_content(scraped_products)
    if not post_content:
        print("Pipeline stopped: Content generation failed.")
        return
    
    print("\n--- AI-Generated Post for Your Review ---")
    print("-----------------------------------------")
    print(post_content)
    print("-----------------------------------------")

    approve = input("Do you want to post this to LinkedIn as a DRAFT? (y/n): ").lower()
    
    if approve != 'y':
        print("Post not approved. Exiting pipeline.")
        return
    
    print("User approved. Proceeding to post...")
    success = post_to_linkedin(post_content)

    if success:
        print("\n--- Pipeline completed successfully! Post is in your drafts. ---")
    else:
        print("\n--- Pipeline finished with an error during posting. ---")

if __name__ == "__main__":
    main()