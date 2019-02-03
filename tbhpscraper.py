from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
import requests

def merge_dict(ds):
    z = dict()
    for d in ds:
        z.update(d)
    return z
    
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
    links = list()
    for link in soup.find_all('a'):
        link_title = link.get('title')
        if(str(link_title).startswith("Show results")):
            links.append(link.get('href'))
    return links

def get_vehicle_review_from_page(page_url):
    reviews = dict()
    soup = get_soup(page_url)
    if soup != None:
        for link in soup.find_all('a'):
            link_id = link.get('id')
            if str(link_id).startswith('thread'):
                # print(link.text, link.get('href'))
                reviews[link.text] = link.get('href')
    return reviews

def get_reviews(baselink):
    soup = get_soup(baselink)
    if soup == None:
        print("Error fetching page")
        exit(0)

    navigation_pages = list()
    navigation_pages.append(baselink)
    reviews = dict()

    navigation_pages.extend(get_pagination_links(soup))

    # now go to each page, and get the vehicle review list
    pool = ThreadPool(8)
    results = pool.map(get_vehicle_review_from_page, navigation_pages)
    pool.close()
    pool.join()

    reviews = merge_dict(results)
    # print(reviews)
    # search("mercedes", review)
    return reviews