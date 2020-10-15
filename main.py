import requests
from bs4 import BeautifulSoup
INDEED_URL = 'https://www.indeed.com/jobs?q=python&limit=50'

indeed_resul = requests.get(INDEED_URL)

indeed_soup = BeautifulSoup(indeed_resul.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination = pagination.find_all('a')
spans = []
for page in pages:
    spans.append(page.find("span"))
print(spans[:-1])
