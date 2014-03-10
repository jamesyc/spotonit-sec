import re
import urlparse
import requests

# use django regex to check if the url is valid
def check_url(url):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if url_regex.match(url) is None:
        return False
    else:
        return True

# checks if url is valid; if it is, download the page
def get_url(url):
    # do a url check
    if not check_url(url):
        raise ValueError("not an URL")
    # try downloading the url
    url_data = requests.get(url)
    if int(url_data.status_code) != 200:
        raise Exception("url invalid")
    # if it downloads, return the html
    return url_data.content

# create absolute url from relative url
def generate_page_url(current_url, relative_url):
    return urlparse.urljoin(current_url, relative_url)

# check if 2 urls are from the same domain
def check_same_domain(url1, url2):
    parsed_uri1 = urlparse.urlparse(url1)
    domain1 = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri1)
    parsed_uri2 = urlparse.urlparse(url2)
    domain2 = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri2)
    if domain1.lower() == domain2.lower():
        return True
    else:
        return False

# extract all the links from a content node
def extract_links(node):
    all_links = []
    link_list = node.find_all('a')
    for link in link_list:
        all_links.append(link.get('href'))
    return all_links

