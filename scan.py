import requests
from bs4 import BeautifulSoup

page = 1
url = "urls.txt"
word = "lucky"

def check(url: str, word: str, page) -> int:
    while page < 4:
        full_url = url + f"&page={page}"
        print(full_url)
        try:
            response = requests.get(full_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the pageL {e}")
            return 0
        
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        count = text.lower().count(word.lower())
        page+=1
        print(f"{word} appears {count} times.")
    print()
    return count

try:
    with open(url, "r") as file:
        site_urls = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"Error: {url} not found!")
    exit()
print("File Opened")

for site_url in site_urls:
    count = check(site_url, word, page)
