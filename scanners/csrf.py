from bs4 import BeautifulSoup
from colorama import Fore, Style

def test_csrf(form):
    csrf_token = form.find('input', {'name': 'csrf_token'})
    if not csrf_token:
        print(Fore.RED + "[!] CSRF vulnerability: No CSRF token found in form." + Style.RESET_ALL)