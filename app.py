from dataclasses import dataclass

from requests_html import HTMLSession


@dataclass
class Stat:
    label: str
    value: str

    def __str__(self):
        return f"{self.value.rjust(7)}  {self.label}"


def fetch():
    url = "https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home"
    session = HTMLSession()
    response = session.get(url)
    stats_cards = response.html.xpath(
        '//*[@id="odx-main-content"]/article/section[2]/div', first=True
    )
    tiles = stats_cards.find(".odh-ads__item")[:8]
    stats = []
    for idx, tile in enumerate(tiles):
        value = tile.find(".odh-ads__item-title", first=True).text
        label = tile.find(".odh-ads__item-summary", first=True).text
        label = (
            label.replace("Number of", "")
            .replace("in Ohio", "")
            .title()
            .replace("Icu", "ICU")
            .strip()
        )
        stat = Stat(label=label, value=value)
        stats.append(stat)
    return stats


def display(stats):
    for idx, i in enumerate(stats):
        print(i, end=("\n\n" if idx in [3, 5] else "\n"))


def main():
    stats = fetch()
    display(stats)


if __name__ == "__main__":
    main()
