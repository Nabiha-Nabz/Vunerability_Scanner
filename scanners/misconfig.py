import requests
from colorama import Fore, Style

def test_security_misconfigurations(url):
    admin_panels = ['/admin', '/wp-admin', '/login', '/dashboard']
    for panel in admin_panels:
        response = requests.get(url + panel)
        if response.status_code == 200:
            print(Fore.RED + f"[!] Security Misconfiguration: Admin panel accessible at {url + panel}" + Style.RESET_ALL)