🤖 AI-Powered Weekly LinkedIn Bot
This repository contains a Python-based automation pipeline that scrapes Product Hunt for the top products of the week, uses the Google Gemini AI to generate an insightful LinkedIn post, and creates a draft on LinkedIn for final human review and publication.

The entire process is orchestrated to run automatically every Monday at noon EST using GitHub Actions.

Project Workflow
This project follows a simple, robust, and automated ETL (Extract, Transform, Load) process:

Step

Action

Technology Used

1. Extract

Scrapes the Product Hunt homepage to find the "Last Week's Top Products" section and extracts the top 5 product names and taglines.

Python, Selenium, BeautifulSoup

2. Transform

Sends the scraped data to the Google Gemini API with a carefully engineered prompt to generate a well-written, down-to-earth LinkedIn post.

Google Gemini API

3. Load

Uses the LinkedIn API to create a new draft post containing the AI-generated content, ready for final review and manual publishing.

LinkedIn API, OAuth 2.0

4. Automate

A GitHub Actions workflow runs the entire pipeline on a weekly schedule, ensuring consistent, hands-off operation.

GitHub Actions

🛠️ Tech Stack
🚀 Getting Started
To run this project locally, you will need Python 3.9+ and the Firefox browser installed.

1. Clone the Repository

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

2. Set Up the Environment

Create and activate a Python virtual environment:

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Your Credentials

Create a .env file in the root of the project folder. This file will hold your secret API keys and is ignored by Git. Add the following lines, replacing the placeholder values with your actual credentials:

# Google Gemini API Key
GEMINI_API_KEY="AIzaSy..."

# LinkedIn Developer App Credentials
LINKEDIN_CLIENT_ID="your_client_id"
LINKEDIN_CLIENT_SECRET="your_client_secret"

# This will be populated after the first manual run
LINKEDIN_ACCESS_TOKEN=""

You will need to manually generate your LINKEDIN_ACCESS_TOKEN using the Tools tab in your LinkedIn Developer App and paste it here.

⚙️ Usage
The project is modular, allowing you to test each component independently.

Test the Scraper:

python scraper.py

Test the Content Generator:

python content_generator.py

Test the Full Pipeline Locally:

python main.py

📂 Project Structure
.
├── .github/workflows/main.yml  # GitHub Actions workflow for automation
├── .env                        # Stores secret API keys (not committed)
├── .gitignore                  # Specifies files for Git to ignore
├── README.md                   # This file
├── requirements.txt            # List of Python dependencies
├── scraper.py                  # Module for scraping Product Hunt
├── content_generator.py        # Module for generating post content with Gemini AI
├── linkedin_poster.py          # Module for creating drafts on LinkedIn
└── main.py                     # Main script to orchestrate the entire pipeline
