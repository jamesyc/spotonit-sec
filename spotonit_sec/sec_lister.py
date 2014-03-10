import bs4
import requests
import spotonit_sec
import re
import random

def lister(events_page_url_list, num_events=10):
    '''
    Returns a list of possible events, given a "parent" url.

    Keyword arguments:
    events_pages_urls -- list of pages containing related events
    num_events -- number of events in list

    Returns: list of strings, the url of events

    '''

    # keep on adding events until it reaches num_events
    event_url_list = []
    seen_urls = []
    while len(event_url_list) < num_events:
        # if no more event pages, break
        if len(events_page_url_list) == 0:
            break
        # check if we already have seen this event page
        events_page = events_page_url_list.pop(0)
        if events_page in seen_urls:
            continue
        seen_urls.append(events_page)
        # download event page, and run beautifulsoup
        events_html = spotonit_sec.get_url(events_page)
        events_soup = bs4.BeautifulSoup(events_html)
        # go thru main content nodes and grab URLs, these are usually events
        big_url_list = []
        for node in events_soup.findAll(attrs={'class': re.compile(r".*content.*")}):
            big_url_list.extend(spotonit_sec.extract_links(node))
        # for node in events_soup.findAll(attrs={'id': re.compile(r".*content.*")}):
        #     big_url_list.extend(spotonit_sec.extract_links(node))
        for node in events_soup.findAll(attrs={'class': re.compile(r".*main.*")}):
            big_url_list.extend(spotonit_sec.extract_links(node))
        for node in events_soup.findAll(attrs={'id': re.compile(r".*main.*")}):
            big_url_list.extend(spotonit_sec.extract_links(node))
        for node in events_soup.findAll(attrs={'id': re.compile(r".*calendar.*")}):
            big_url_list.extend(spotonit_sec.extract_links(node))
        for node in events_soup.find_all('tr'):
            big_url_list.extend(spotonit_sec.extract_links(node))
        # remove dupes
        big_url_list = list(set(big_url_list))
        # convert relative links to absolute links
        absolute_url_list = []
        for link in big_url_list:
            absolute_url_list.append(spotonit_sec.generate_page_url(events_page, link))
        # remove non urls (javascript, etc)
        big_url_list = filter(spotonit_sec.check_url, absolute_url_list)
        event_url_list.extend(big_url_list)

    # remove dupes
    event_url_list = list(set(event_url_list))
    random.shuffle(event_url_list,random.random)
    # not enough events, fill up the list
    while len(event_url_list) < num_events:
        event_url_list.append("")
    return event_url_list[:num_events]


# run module as script, for crappy testing
if __name__ == '__main__':

    # test_urls = ["http://calendar.boston.com/lowell_ma/events/show/274127485-mrt-presents-shakespeares-will", 
    #     "http://www.sfmoma.org/exhib_events/exhibitions/513", 
    #     "http://www.workshopsf.org/?page_id=140&id=1328", 
    #     "http://events.stanford.edu/events/353/35309/"]
    
    test_urls = sys.argv[1:]
    import sec_select
    for url in test_urls:
        print lister(sec_select.select(url))

