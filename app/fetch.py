from .cache import setup_cache

setup_cache()  # must run before htmlsession import
from requests_html import HTML, HTMLSession


def fetch() -> HTML:
    """Retrieve html of metrics overview page."""
    url = "https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home"
    session = HTMLSession()
    response = session.get(url)
    return response.html
