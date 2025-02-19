import requests
from bs4 import BeautifulSoup

def check(url: str, word: str, page) -> int:
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

    return count
page = [1, 2, 3]
url = "https://polkadot.subsquare.io/treasury/child-bounties?parentBountyId=50"
word = "lucky"

for page in page:

    count = check(url, word, page)
    print(f"{word} appears {count} times.")