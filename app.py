from dataclasses import dataclass

from requests_html import HTMLSession


@dataclass
class Metric:
    """A metric."""

    label: str
    value: str

    def __str__(self):
        return f"{self.value.rjust(7)}  {self.label}"


def fetch():
    """Retrieve html of metrics overview page."""
    url = "https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home"
    session = HTMLSession()
    response = session.get(url)
    return response.html


def parse(html):
    """Scrape metrics tiles from page."""
    stats_cards = html.xpath(
        '//*[@id="odx-main-content"]/article/section[2]/div', first=True
    )
    tiles = stats_cards.find(".odh-ads__item")[:8]
    metrics = [
        Metric(
            label=tile.find(".odh-ads__item-summary", first=True).text,
            value=tile.find(".odh-ads__item-title", first=True).text,
        )
        for tile in tiles
    ]
    return metrics


def clean(metrics):
    """Post-process tile labels."""
    for i in metrics:
        i.label = (
            i.label.replace("Number of", "")
            .replace("in Ohio", "")
            .title()
            .replace("Icu", "ICU")
            .strip()
        )
    return metrics


def display(metrics):
    """Output metrics tiles to console."""
    for idx, i in enumerate(metrics):
        print(i, end=("\n\n" if idx in [3, 5] else "\n"))


def main():
    html = fetch()
    metrics = parse(html)
    metrics = clean(metrics)
    display(metrics)


if __name__ == "__main__":
    main()
