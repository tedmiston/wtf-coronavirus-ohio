from pathlib import Path

import requests_cache


def setup_cache() -> None:
    """
    The requests_cache package monkey patches `requests.Session` (used by requests_html) so `requests_cache.install_cache` must be called before `requests_html.HTMLSession` is imported.
    """
    cache_path_dir = Path.home() / ".wtf-covid-19-ohio"
    cache_path_dir.mkdir(exist_ok=True)
    cache_path = cache_path_dir / "cache"
    requests_cache.install_cache(str(cache_path), backend="sqlite", expire_after=300)
