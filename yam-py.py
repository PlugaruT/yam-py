from collections import namedtuple
from typing import List

import click
from colorama import init
from requests_html import Element, HTMLSession

elements = List[Element]


class Article:
    def __init__(self, html_node: Element) -> None:
        self._parts = html_node.text.split("\n")
        self.time = self._extract_time()
        self.title = self._extract_title()
        self.link = self._extract_link(html_node.absolute_links)

    def __str__(self):
        return f"{self.time} {self.title}"

    def __repr__(self):
        return f"{self.time} {self.title}"

    def _extract_time(self) -> str:
        return self._parts[0]

    def _extract_title(self) -> str:
        return self._parts[1]

    def _extract_link(self, links: list) -> str:
        return next(x for x in links if self._is_matching(x))

    def _is_matching(self, link: str) -> str:
        # TODO [Tudor] Find a better way of finding the right link
        return "/s/" in link


def fetch_page(session: HTMLSession, page: int, lang: str) -> elements:
    response = session.get(f"https://news.yam.md/{lang}/get_more_news/0/{page}")
    return response.html.find("div.news-list-row.story-row-container")


@click.command()
@click.option(
    "--lang",
    default="ro",
    type=click.Choice(["ro", "ru", "en"]),
    help="Language to be used when fetching list of articles.",
)
@click.option(
    "--pages",
    default=1,
    type=click.INT,
    help="Number of pages to fetch. Each page represents 30 more articles.",
)
def main(lang: str, pages: int):
    session = HTMLSession()

    raw_articles = []
    for page in range(0, pages):
        raw_articles.extend(fetch_page(session, page, lang))

    articles = [Article(elem) for elem in raw_articles]
    for article in articles[::-1]:
        click.echo(click.style(f"{article.time} ", fg="green"), nl=False)
        click.echo(click.style(f"<{article.title}> ", fg="bright_blue"), nl=False)
        click.echo(click.style(f"{article.link}", fg="white"))


if __name__ == "__main__":
    init()
    main()
