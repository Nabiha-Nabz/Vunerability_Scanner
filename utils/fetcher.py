import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_forms(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('form')

def crawl_website(base_url, max_pages=10):
    visited = set()
    to_visit = set([base_url])
    all_pages = set()

    with tqdm(total=max_pages, desc="Crawling") as pbar:
        while to_visit and len(all_pages) < max_pages:
            url = to_visit.pop()
            if url in visited:
                continue

            html = fetch_html(url)
            if html:
                visited.add(url)
                all_pages.add(url)
                pbar.update(1)

                soup = BeautifulSoup(html, 'html.parser')
                for link in soup.find_all('a', href=True):
                    full_url = urljoin(base_url, link['href'])
                    if full_url not in visited and full_url not in to_visit:
                        to_visit.add(full_url)

    return list(all_pages)