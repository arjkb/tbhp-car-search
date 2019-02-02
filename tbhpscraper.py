from bs4 import BeautifulSoup
import requests

def search(carname, reviews):
    results = dict()
    for k in reviews:
        if carname.lower() in k.lower():
            results[k] = reviews[k]
    return results

def get_soup(link):
    r = requests.get(link)
    if r.status_code != requests.codes.ok:
        return None
    return BeautifulSoup(r.text, 'html.parser')

def get_pagination_links(soup):
    # get list of all links to be navigated to
    links = set()
    for link in soup.find_all('a'):
        link_title = link.get('title')
        if(str(link_title).startswith("Show results")):
            links.add(link.get('href'))
    return links

def get_reviews(baselink):
    soup = get_soup(baselink)
    if soup == None:
        print("Error fetching page")
        exit(0)

    navigation_pages = set()
    navigation_pages.add(baselink)
    reviews = dict()

    navigation_pages.update(get_pagination_links(soup))

    # now go to each page, and get the vehicle review list
    for page in navigation_pages:
        soup = get_soup(page)
        if soup != None:
            for link in soup.find_all('a'):
                link_id = link.get('id')
                if str(link_id).startswith('thread'):
                    # print(link.text, link.get('href'))
                    reviews[link.text] = link.get('href')

    # print(reviews)
    # search("mercedes", review)
    return reviews