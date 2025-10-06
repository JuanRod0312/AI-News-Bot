import os
import requests
from dotenv import load_dotenv

def get_linkedin_user_id():
    load_dotenv()
    access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    if not access_token:
        print("Error: LINKEDIN_ACCESS_TOKEN not found in .env file.")
        return None

    url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        user_info = response.json()
        return user_info.get('sub')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching LinkedIn user ID: {e}')
        if '403' in str(e):
            print("This is a permission error. Your token may lack the required 'profile' and 'openid' scopes.")
        return None

def post_to_linkedin(content):
    print("Attempting to post to LinkedIn...")
    user_id = get_linkedin_user_id()
    
    if not user_id:
        print("Could not get user ID. Aborting post.")
        return False

    load_dotenv()
    access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    if not access_token:
        print("Could not load access token for posting. Aborting.")
        return False

    post_url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    
    post_data = {
        "author": f"urn:li:person:{user_id}",
        "lifecycleState": "DRAFT",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    try:
        response = requests.post(post_url, headers=headers, json=post_data)
        response.raise_for_status()
        print("--- Successfully loaded into drafts ---")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error posting to LinkedIn: {e}")
        if 'response' in locals() and hasattr(response, 'text'):
            print(f"Response body: {response.text}")
        return False
