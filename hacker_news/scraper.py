import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all('tr', class_='athing')
print("Number of articles found:", len(articles))
for article in articles:
    title_tag = article.find('span', class_='titleline')
    if not title_tag:
        continue
    link = title_tag.find('a')
    title = link.text.strip()
    article_url = link['href']
    
    subtext = article.find_next_sibling('tr')
    score = subtext.find('span', class_='score')
    points = score.text if score else "0 points"
    user = subtext.find('a', class_='hnuser')
    author = user.text if user else "Unknown"
    comments_tag = subtext.find_all('a')[-1].text
    
    print(f"Title: {title}")
    print(f"URL: {url}")
    print(f"Points: {points}")
    print(f"Author: {author}")
    print(f"Comments: {comments_tag}")
    print("-" * 50)
   
