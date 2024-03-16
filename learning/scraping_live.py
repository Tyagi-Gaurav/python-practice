# Checkout robots.txt for the website
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

page = response.text
soup = BeautifulSoup(page, "html.parser")

all_rows = soup.find_all(name="tr", attrs="athing")
links = []
for row in all_rows:
    all_spans = row.findChildren("span", {"class": "titleline"})
    for span in all_spans:
        anchor_link = span.select_one("a")
        # print (anchor_link.get_text())
        row_id = row["id"]
        score_element = soup.select_one(selector=f"#score_{row_id}")
        if score_element:
            score = int(score_element.get_text().strip(" points"))
        else:
            score = 0
        links.append({"title": anchor_link.get_text(), "score": score})

links = sorted(links, key=lambda item: item["score"], reverse=True)
print (links)
