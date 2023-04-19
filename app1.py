from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('h1').text
    content = ' '.join([p.text for p in soup.find_all('p')])
    
    return {'title': title, 'content': content}

# List of article URLs to scrape
urls = [
    "https://www.example.com/article1",
    "https://www.example.com/article2",
    # ...
]

# Scrape articles and store them in a DataFrame
articles = [scrape_article(url) for url in urls]
data = pd.DataFrame(articles)
