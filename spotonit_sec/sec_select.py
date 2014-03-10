import bs4
import requests
import spotonit_sec
import sys

def select(event_url):
    '''
    Selects a "parent" url to search for events, given an event

    Keyword arguments:
    event_url -- url of one event

    Returns: list of strings, url of pages that contain links to multiple events

    '''

    # validate url, get page from url
    url_html = spotonit_sec.get_url(event_url)

    # use beautifulsoup on webpage
    soup = bs4.BeautifulSoup(url_html)
    links = soup.find_all('a')

    # search for events or calendar link
    parent_url_list = []
    all_url_list = []
    for a in links:
        all_url_list.append(a.get('href'))
        if a.get_text().lower().find("event") != -1:
            parent_url_list.append(a.get('href'))
        if a.get_text().lower().find("calendar") != -1: 
            parent_url_list.append(a.get('href'))

    # if we have links to pages that contain events, return them now
    events_pages_urls = []
    if len(parent_url_list) >= 1:
        for parent_url in parent_url_list:
            absolute_url = spotonit_sec.generate_page_url(event_url, parent_url)
            events_pages_urls.append(absolute_url)
        return events_pages_urls

    # no event page found, now check for links on same site
    print "warning, this section is slow"
    for individual_url in all_url_list:
        if spotonit_sec.check_same_domain(individual_url, event_url):
            # check individual page titles to look for events
            absolute_url = spotonit_sec.generate_page_url(event_url, individual_url)
            individual_html = spotonit_sec.get_url(absolute_url)
            individual_title = bs4.BeautifulSoup(individual_html).title.string.lower()
            if individual_title.find("event") != -1:
                events_pages_urls.append(absolute_url)
            if individual_title.find("calendar") != -1:
                events_pages_urls.append(absolute_url)
    return events_pages_urls


# run module as script, for crappy testing
if __name__ == '__main__':
    # test_urls = ["http://calendar.boston.com/lowell_ma/events/show/274127485-mrt-presents-shakespeares-will", 
    #     "http://www.sfmoma.org/exhib_events/exhibitions/513", 
    #     "http://www.workshopsf.org/?page_id=140&id=1328", 
    #     "http://events.stanford.edu/events/353/35309/"]

    test_urls = sys.argv[1:]
    for url in test_urls:
        try:
            print select(url)
        except:
            # something broke, but ignored for most tests
            pass