from typing import List

from requests_html import HTML

from .models import Metric


def _parse_tile(tile) -> Metric:
    metric = Metric(
        label=tile.find(".stats-cards__label", first=True).text,
        value=tile.find(".stats-cards__number", first=True).text,
    )
    return metric


def parse(html: HTML) -> List[Metric]:
    """Scrape metrics tiles from page."""
    stats_cards = html.find(".stats-cards__container", first=True)
    tiles = stats_cards.find(".stats-cards__item")
    metrics = [_parse_tile(x) for x in tiles]
    return metrics
