from dataclasses import dataclass
from typing import List

from cache import setup_cache

setup_cache()  # must run before htmlsession import
from requests_html import HTML, HTMLSession


@dataclass
class Metric:
    """A metric."""

    label: str
    value: str

    def __str__(self) -> str:
        return f"{self.value.rjust(7)}  {self.label}"


def fetch() -> HTML:
    """Retrieve html of metrics overview page."""
    url = "https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home"
    session = HTMLSession()
    response = session.get(url)
    return response.html


def parse(html: HTML) -> List[Metric]:
    """Scrape metrics tiles from page."""
    stats_cards = html.find(".stats-cards__container", first=True)
    tiles = stats_cards.find(".stats-cards__item")
    metrics = [
        Metric(
            label=tile.find(".stats-cards__label", first=True).text,
            value=tile.find(".stats-cards__number", first=True).text,
        )
        for tile in tiles
    ]
    return metrics


def clean(metrics: List[Metric]) -> List[Metric]:
    """Post-process tile labels."""
    for i in metrics:
        i.label = (
            i.label.lower()
            .replace("number of", "")
            .replace("in ohio", "")
            .replace("expanded case definition (probable)", "expanded cases")
            .replace("expanded death definition (probable)", "expanded deaths")
            .title()
            .replace("Cdc", "CDC")
            .replace("Icu", "ICU")
            .strip()
        )
    return metrics


def display(metrics: List[Metric]) -> None:
    """Output metrics tiles to console."""
    divider_indices = (2, 3, 6, 7, 9)
    for idx, i in enumerate(metrics):
        print(i, end=("\n\n" if idx in divider_indices else "\n"))


def main() -> None:
    html = fetch()
    metrics = parse(html)
    metrics = clean(metrics)
    display(metrics)


if __name__ == "__main__":
    main()
