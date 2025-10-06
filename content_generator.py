import os
import google.generativeai as genai
from dotenv import load_dotenv

def gen_post_content(products_data):

    print("starting content Gen")

    load_dotenv()
    gemini_api_key = os.getenv('GEMINI_API_KEY')

    if not gemini_api_key:
        print("Error invalid/not present Gemini API key")
        return None
    
    try:
        genai.configure(api_key = gemini_api_key)
        model = genai.GenerativeModel('gemini-2.5-pro')

        prooduct_list_strings = ''
        for i, product in enumerate(products_data):
            prooduct_list_strings += f"{i+1}. {product['name']}: {product['tagline']} ({product['url']})\n"

        prompt = f"""
        Act as a software developer...Your tone should be down-to-earth, conversational, and chill, like you're sharing something cool you found with a colleague. Avoid marketing hype, buzzwords, and overly excited language. Be genuine and curious.

        Here is the list of products:
        ---
        {prooduct_list_strings}
        ---

        Please structure your post according to these rules:
        1.  **Catchy Hook:** Start with a strong, engaging opening question or statement to grab attention.
        2.  **Introduction:** Briefly state that you're sharing the top trending products from the world of AI.
        **Product Highlights (Bulleted List):** You MUST use the blue diamond emoji (🔹) as the bullet point for each product. Start with the product's name in bold and then briefly explain its purpose in simple terms based on the tagline.
        4.  **Call to Action:** Encourage discussion by asking a question like "Which of these are you most excited to try?" or "What amazing projects have you seen lately?".
        5.  **Hashtags:** End with 5-7 relevant hashtags, including #Tech #ProductHunt #Innovation and others related to the products (e.g., #AI, #Productivity).
        6.  **CRITICAL RULE:** Your final output must be ONLY the text for the LinkedIn post. Do not include any introductory phrases, explanations, or separators like "---". The very first character of your response must be the first letter of the catchy hook.

        Do not include the URLs in the main body of the post. The goal is to generate discussion.
        """

        print("Now sending out prompt to gemini")
        response = model.generate_content(prompt)
        print('content successfully generated!')

        return response.text
    
    except Exception as e:
        print(f'An error occurred with the Gemini API: {e}')
        return None 