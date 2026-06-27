from django.core.management.base import BaseCommand
from hacker_news.models import News

import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = "Scrapes news from Hacker News and saves it to the database"

    def handle(self, *args, **kwargs):

        url = "https://news.ycombinator.com/"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("tr", class_="athing")

        print("Number of articles found:", len(articles))

        for article in articles:

            title_tag = article.find("span", class_="titleline")

            if not title_tag:
                continue

            link = title_tag.find("a")

            title = link.text.strip()
            article_url = link["href"]

            subtext = article.find_next_sibling("tr")

            score = subtext.find("span", class_="score")
            points = int(score.text.split()[0]) if score else 0

            user = subtext.find("a", class_="hnuser")
            author = user.text if user else "Unknown"

            comments = 0

            links = subtext.find_all("a")

            if links:
                last_link = links[-1].text

                if "comment" in last_link:
                    try:
                        comments = int(last_link.split()[0])
                    except ValueError:
                        comments = 0

            News.objects.get_or_create(
                url=article_url,
                defaults={
                    "title": title,
                    "points": points,
                    "author": author,
                    "comments": comments,
                }
            )

        self.stdout.write(
            self.style.SUCCESS("News scraped successfully!")
        )