from .sec_lister import lister
from .sec_select import select

def sec(event_url):
    '''
    Returns a list of events, given an event url to start from.

    Keyword arguments:
    event_url -- url of one event

    Returns: list of strings, the url of events

    '''
    events_page_url_list = select(event_url)
    return lister(events_page_url_list, 10)