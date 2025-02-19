import threading
import logging
from urllib.parse import urljoin
from utils.fetcher import fetch_html, fetch_forms, crawl_website
from scanners.sql_injection import test_sql_injection
from scanners.xss import test_xss
from scanners.csrf import test_csrf
from scanners.sensitive_data import test_sensitive_data_exposure
from scanners.misconfig import test_security_misconfigurations
from scanners.auth import test_broken_authentication
from colorama import Fore, Style

# Configure logging
logging.basicConfig(filename='scan.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def scan_page(url):
    print(Fore.GREEN + f"[*] Scanning: {url}" + Style.RESET_ALL)
    html = fetch_html(url)
    if html:
        forms = fetch_forms(html)
        for form in forms:
            action = form.get('action')
            if action:
                form_url = urljoin(url, action)
                test_sql_injection(form_url, form)
                test_xss(form_url, form)
                test_csrf(form)
                test_broken_authentication(form)
            else:
                test_sql_injection(url, form)
                test_xss(url, form)
                test_csrf(form)
                test_broken_authentication(form)

        test_sensitive_data_exposure(url)
        test_security_misconfigurations(url)

def scan_website(base_url, max_threads=5):
    pages = crawl_website(base_url)
    threads = []

    for page in pages:
        thread = threading.Thread(target=scan_page, args=(page,))
        threads.append(thread)
        thread.start()

        # Limit the number of concurrent threads
        if len(threads) >= max_threads:
            for thread in threads:
                thread.join()
            threads = []

    # Wait for remaining threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = input("Enter the website URL to scan: ")
    scan_website(url)