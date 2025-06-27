import requests
from bs4 import BeautifulSoup
from langchain.schema import Document
from urllib.parse import urljoin

def scrape_website(url: str, max_depth: int = 1) -> list:
    visited = set()
    to_visit = [(url, 0)]
    documents = []

    while to_visit:
        current_url, depth = to_visit.pop(0)
        if current_url in visited or depth > max_depth:
            continue

        try:
            response = requests.get(current_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)

            documents.append(Document(
                page_content=text,
                metadata={"source": current_url}
            ))

            visited.add(current_url)

            for link in soup.find_all('a', href=True):
                absolute_url = urljoin(current_url, link['href'])
                if absolute_url not in visited:
                    to_visit.append((absolute_url, depth + 1))

        except Exception:
            continue

    return documents