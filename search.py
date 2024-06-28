import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def get_top_articles(keyword):

    api_key = os.getenv("API_KEY")
    cx = os.getenv("CX")

    search_url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={keyword}&gl=us"
    response = requests.get(search_url)

    if response.status_code == 200:
        search_results = response.json()
        urls = [item['link'] for item in search_results.get('items', [])]
        return urls
    else:
        print(f"Error: {response.status_code}")
        return []

# Function to get article schema
def get_article_schema(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else 'No title found'

        # Extract headings
        headings = {'H1': [], 'H2': [], 'H3': []}
        for h in headings.keys():
            headings[h] = [element.get_text().strip() for element in soup.find_all(h.lower())]
        
        return {
            'title': title,
            'headings': headings
        }
    except requests.RequestException as e:
        print(f"Error: Unable to fetch the URL {url}. Exception: {e}")
        return None


if __name__ == "__main__":
    try:
        urls = get_top_articles("crime in USA")
        for url in urls:
            print(url)
    except ValueError as e:
        print(e)
