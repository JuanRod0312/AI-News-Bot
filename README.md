# 🤖 AI-Powered Weekly LinkedIn Bot

This repository contains a **Python-based automation pipeline** that scrapes Product Hunt for the top products of the week, uses **Google Gemini AI** to generate an insightful LinkedIn post, and creates a **draft post on LinkedIn** for final human review and publication.

The entire process runs automatically **every Monday at noon EST** using **GitHub Actions**.

---

## 🧩 Project Workflow

This project follows a simple, robust, and automated **ETL (Extract, Transform, Load)** process:

| Step | Action | Technology Used |
|------|--------|-----------------|
| **1. Extract** | Scrapes Product Hunt’s “Last Week’s Top Products” and extracts the top 5 product names and taglines. | Python, Selenium, BeautifulSoup |
| **2. Transform** | Sends the scraped data to the **Google Gemini API** to generate a high-quality LinkedIn post. | Google Gemini API |
| **3. Load** | Uses the **LinkedIn API** to create a new **draft post**, ready for review and manual publishing. | LinkedIn API, OAuth 2.0 |
| **4. Automate** | A **GitHub Actions workflow** runs the entire pipeline weekly for consistent, hands-off operation. | GitHub Actions |

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Selenium** & **BeautifulSoup** for web scraping  
- **Google Gemini API** for content generation  
- **LinkedIn API** with OAuth 2.0 for post creation  
- **GitHub Actions** for automation

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up the Environment
Create and activate a Python virtual environment.

### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
### 4. Configure Your Credentials
Create a .env file in the root directory and add the following (replace placeholders with your real credentials):
```bash
# Google Gemini API Key
GEMINI_API_KEY="AIzaSy..."

# LinkedIn Developer App Credentials
LINKEDIN_CLIENT_ID="your_client_id"
LINKEDIN_CLIENT_SECRET="your_client_secret"

# Must be generated manually from the LinkedIn Developer Portal’s "Tools" tab
LINKEDIN_ACCESS_TOKEN="AQA..."
```
## ⚠️ Important:
You must generate your LINKEDIN_ACCESS_TOKEN manually using the LinkedIn Developer App “Tools” tab with the following scopes:
* openid
* profile
* w_member_social

## ⚙️ Usage
You can test each component independently or run the entire pipeline.

### Test the Scraper:
```bash
python scraper.py
```
### Test the Content Generator:
```bash
python content_generator.py
```
### Run the Full Pipeline:
```bash
python main.py
```

## 📂 Project Structure
```bash
.
├── .github/workflows/main.yml  # GitHub Actions workflow for automation
├── .env                        # Stores secret API keys (not committed)
├── .gitignore                  # Specifies files for Git to ignore
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── scraper.py                  # Scrapes Product Hunt
├── content_generator.py        # Generates post content with Gemini AI
├── linkedin_poster.py          # Creates drafts on LinkedIn
└── main.py                     # Orchestrates the entire pipeline
```

## 🧠 Future Improvements
* Add automatic hashtag and emoji optimization
* Include OpenAI or Claude integration as fallback models
* Auto-publish approved posts after review
* Support for Twitter and Mastodon cross-posting

## 📅 Automation Schedule
This workflow runs automatically via GitHub Actions:
* Frequency: Every Monday at 12:00 PM EST
* Trigger: .github/workflows/main.yml

## 💡 Inspiration 
The idea came from wanting to combine AI creativity with automation reliability — letting AI handle the heavy lifting of content generation while keeping human review in the loop for authenticity.

## 🧑‍💻 Author
Juan Rodriguez
📍 USA, FL
[💼 LinkedIn ](https://www.linkedin.com/in/juan-sebastian-rodriguez-hernandez/)

## ⭐ If you found this project useful, please consider giving it a star!

