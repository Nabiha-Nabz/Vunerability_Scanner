from colorama import Fore, Style

def test_sensitive_data_exposure(url):
    if not url.startswith('https'):
        print(Fore.RED + "[!] Sensitive Data Exposure: Website is not using HTTPS." + Style.RESET_ALL)