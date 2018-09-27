from collections import namedtuple
import click
from requests_html import Element, HTMLSession




class Article:
    def __init__(self, html_node: Element) -> None:
        self._parts = html_node.text.split("\n")
        self.time = self._extract_time()
        self.title = self._extract_title()
        self.link = list(html_node.absolute_links)[2]

    def __str__(self):
        return f"{self.time} {self.title}"

    def __repr__(self):
        return f"{self.time} {self.title}"

    def _extract_time(self) -> str:
        return self._parts[0]

    def _extract_title(self) -> str:
        return self._parts[1]


@click.command()
@click.option("--lang", default="ro", type=click.Choice(["ro", "ru", "en"]), )
def main(lang:str):
    session = HTMLSession()
    r = session.get(f"https://news.yam.md/{lang}/")

    raw_articles = r.html.find("div.news-list-row.story-row-container")
    articles = [Article(elem) for elem in raw_articles]

    print(articles)

if __name__ == "__main__":
    main()
