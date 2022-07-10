from typing import List

from .cache import setup_cache
from .display import clean, display
from .fetch import fetch
from .models import Metric
from .parse import parse


def main() -> None:
    html = fetch()
    metrics = parse(html)
    metrics = clean(metrics)
    display(metrics)


if __name__ == "__main__":
    main()
