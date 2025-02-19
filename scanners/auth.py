from bs4 import BeautifulSoup
from colorama import Fore, Style

def test_broken_authentication(form):
    password_input = form.find('input', {'type': 'password'})
    if not password_input:
        print(Fore.RED + "[!] Broken Authentication: No password input found in form." + Style.RESET_ALL)