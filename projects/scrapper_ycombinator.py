"""
YCombinator News Scrapper
"""

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    page = requests.get("https://news.ycombinator.com/")

    soup = BeautifulSoup(page.text, "html.parser")

    headlines = soup.find_all('span', class_='titleline')
    # headlines = soup.find_all('td', class_='title')
    upvotes = soup.find_all('span', class_='score')

    for i, title_line in enumerate(headlines):
        link = title_line.find('a')
        upvote_num = upvotes[i].text

        print(f"{link.text} | {upvote_num}")
