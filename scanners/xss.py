import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def test_xss(url, form):
    payload = "<script>alert('XSS')</script>"
    data = {}
    for input_tag in form.find_all('input'):
        input_name = input_tag.get('name')
        input_type = input_tag.get('type', '').lower()
        if input_type == 'text':
            data[input_name] = payload
    response = requests.post(url, data=data)
    if payload in response.text:
        print(Fore.RED + f"[!] XSS vulnerability found with payload: {payload}" + Style.RESET_ALL)